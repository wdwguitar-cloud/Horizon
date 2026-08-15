from __future__ import annotations

import argparse
import json
import logging
import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

import feedparser
import httpx
from openai import OpenAI


GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search"


@dataclass
class CandidateItem:
    title: str
    url: str
    source_name: str
    published_at: datetime
    query_id: str
    query_name: str
    query_priority: str
    snippet: str
    matches: dict[str, list[str]]
    heuristic_score: float


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def parse_published(entry: Any) -> datetime | None:
    parsed = entry.get("published_parsed") or entry.get("updated_parsed")
    if parsed:
        return datetime(
            parsed.tm_year,
            parsed.tm_mon,
            parsed.tm_mday,
            parsed.tm_hour,
            parsed.tm_min,
            parsed.tm_sec,
            tzinfo=timezone.utc,
        )
    return None


def fetch_google_news(query_cfg: dict[str, Any], lookback_hours: int, max_items: int) -> list[dict[str, Any]]:
    query = f'{query_cfg["query"]} when:{lookback_hours}h'
    params = {
        "q": query,
        "hl": "zh-CN",
        "gl": "CN",
        "ceid": "CN:zh-Hans",
    }
    url = f"{GOOGLE_NEWS_RSS_URL}?{urlencode(params)}"
    response = httpx.get(url, timeout=30.0, follow_redirects=True)
    response.raise_for_status()
    feed = feedparser.parse(response.text)
    entries: list[dict[str, Any]] = []
    for entry in feed.entries[:max_items]:
        entries.append(entry)
    return entries


def extract_source_name(entry: Any) -> str:
    source = entry.get("source")
    if isinstance(source, dict) and source.get("title"):
        return normalize_whitespace(str(source["title"]))
    title = getattr(source, "title", None)
    if title:
        return normalize_whitespace(str(title))
    return "Google News"


def extract_snippet(entry: Any) -> str:
    return normalize_whitespace(
        str(entry.get("summary") or entry.get("description") or "")
    )


def compile_keyword_patterns(keyword_layers: dict[str, list[str]]) -> dict[str, list[tuple[str, re.Pattern[str]]]]:
    compiled: dict[str, list[tuple[str, re.Pattern[str]]]] = {}
    for layer, keywords in keyword_layers.items():
        compiled[layer] = []
        for keyword in keywords:
            compiled[layer].append((keyword, re.compile(re.escape(keyword), re.IGNORECASE)))
    return compiled


def find_matches(text: str, compiled: dict[str, list[tuple[str, re.Pattern[str]]]]) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {"core": [], "scenario": [], "risk": []}
    for layer, patterns in compiled.items():
        for keyword, pattern in patterns:
            if pattern.search(text):
                matches[layer].append(keyword)
    return matches


def should_exclude(text: str, exclude_keywords: list[str]) -> bool:
    lowered = text.lower()
    return any(keyword.lower() in lowered for keyword in exclude_keywords)


def heuristic_score(matches: dict[str, list[str]], query_priority: str, published_at: datetime) -> float:
    priority_bonus = {"core": 4.0, "scenario": 2.5, "risk": 1.0}.get(query_priority, 0.0)
    recency_hours = max(1.0, (datetime.now(timezone.utc) - published_at).total_seconds() / 3600)
    recency_bonus = max(0.0, 3.0 - min(recency_hours / 24.0, 3.0))
    return (
        len(matches["core"]) * 3.0
        + len(matches["scenario"]) * 2.0
        + len(matches["risk"]) * 0.8
        + priority_bonus
        + recency_bonus
    )


def build_candidates(config: dict[str, Any]) -> list[CandidateItem]:
    compiled = compile_keyword_patterns(config["keyword_layers"])
    seen: set[str] = set()
    items: list[CandidateItem] = []
    for query_cfg in config["queries"]:
        entries = fetch_google_news(
            query_cfg,
            int(config["lookback_hours"]),
            int(config["max_per_query"]),
        )
        for entry in entries:
            title = normalize_whitespace(str(entry.get("title") or ""))
            url = normalize_whitespace(str(entry.get("link") or ""))
            if not title or not url:
                continue
            dedup_key = url.lower()
            if dedup_key in seen:
                continue
            published_at = parse_published(entry)
            if published_at is None:
                continue
            snippet = extract_snippet(entry)
            combined_text = f"{title}\n{snippet}\n{query_cfg['name']}"
            if should_exclude(combined_text, config["exclude_keywords"]):
                continue
            matches = find_matches(combined_text, compiled)
            if not any(matches.values()):
                continue
            score = heuristic_score(matches, query_cfg["priority"], published_at)
            items.append(
                CandidateItem(
                    title=title,
                    url=url,
                    source_name=extract_source_name(entry),
                    published_at=published_at,
                    query_id=query_cfg["id"],
                    query_name=query_cfg["name"],
                    query_priority=query_cfg["priority"],
                    snippet=snippet,
                    matches=matches,
                    heuristic_score=score,
                )
            )
            seen.add(dedup_key)
    items.sort(key=lambda item: (-item.heuristic_score, -item.published_at.timestamp()))
    return items


def build_ai_payload(items: list[CandidateItem]) -> list[dict[str, Any]]:
    payload: list[dict[str, Any]] = []
    for index, item in enumerate(items, start=1):
        payload.append(
            {
                "id": index,
                "title": item.title,
                "source": item.source_name,
                "query": item.query_name,
                "snippet": item.snippet[:280],
                "matches": item.matches,
            }
        )
    return payload


def extract_json_object(text: str) -> dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("AI response did not contain JSON")
    return json.loads(text[start : end + 1])


def enrich_with_ai(items: list[CandidateItem], config: dict[str, Any]) -> tuple[str, list[dict[str, str]]]:
    api_key = os.getenv(config["ai"]["api_key_env"], "").strip()
    if not api_key:
        return fallback_overview(items), fallback_annotations(items)

    client = OpenAI(
        api_key=api_key,
        base_url=config["ai"]["base_url"],
    )
    payload = build_ai_payload(items)
    system_prompt = (
        "你是传统文化行业观察助手。"
        "你不会删减候选项，只负责把每条内容压缩成适合飞书阅读的短摘要。"
        "请输出严格 JSON，不要使用 Markdown 代码块。"
    )
    user_prompt = {
        "task": "请为每条候选内容生成一句摘要和一句对从业者可能有什么用，保持简短务实。",
        "requirements": {
            "language": "zh",
            "overview": "20到60字，总结今天整体观察",
            "summary": "每条18到45字",
            "why_it_matters": "每条12到32字",
            "tone": "像行业助手，不夸张，不空话",
        },
        "items": payload,
        "output_schema": {
            "overview": "string",
            "items": [
                {
                    "id": 1,
                    "summary": "string",
                    "why_it_matters": "string",
                }
            ],
        },
    }
    response = client.chat.completions.create(
        model=config["ai"]["model"],
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_prompt, ensure_ascii=False)},
        ],
    )
    content = response.choices[0].message.content or ""
    parsed = extract_json_object(content)
    by_id = {entry["id"]: entry for entry in parsed.get("items", []) if "id" in entry}
    annotations: list[dict[str, str]] = []
    for idx, item in enumerate(items, start=1):
        annotation = by_id.get(idx, {})
        annotations.append(
            {
                "summary": normalize_whitespace(str(annotation.get("summary") or fallback_summary(item))),
                "why_it_matters": normalize_whitespace(
                    str(annotation.get("why_it_matters") or fallback_why(item))
                ),
            }
        )
    overview = normalize_whitespace(str(parsed.get("overview") or fallback_overview(items)))
    return overview, annotations


def fallback_summary(item: CandidateItem) -> str:
    if item.snippet:
        return item.snippet[:42]
    return item.title[:42]


def fallback_why(item: CandidateItem) -> str:
    if item.matches["core"] and item.matches["scenario"]:
        return "兼具业务关键词和转化场景，值得优先关注。"
    if item.matches["core"]:
        return "贴近核心业务词，适合作为行业观察线索。"
    if item.matches["scenario"]:
        return "更偏内容与转化场景，可留意实操玩法。"
    return "属于低权重观察项，可作为补充参考。"


def fallback_overview(items: list[CandidateItem]) -> str:
    if not items:
        return "今日未发现高相关行业线索。"
    core_hits = sum(1 for item in items if item.matches["core"])
    scenario_hits = sum(1 for item in items if item.matches["scenario"])
    return f"今日共整理 {len(items)} 条线索，核心业务相关 {core_hits} 条，内容与转化相关 {scenario_hits} 条。"


def fallback_annotations(items: list[CandidateItem]) -> list[dict[str, str]]:
    return [{"summary": fallback_summary(item), "why_it_matters": fallback_why(item)} for item in items]


def format_match_badges(matches: dict[str, list[str]]) -> str:
    parts: list[str] = []
    for layer in ("core", "scenario", "risk"):
        if matches[layer]:
            label = {"core": "核心词", "scenario": "场景词", "risk": "风险观察"}[layer]
            parts.append(f"**{label}**: {'、'.join(matches[layer][:4])}")
    return " | ".join(parts)


def build_markdown_report(
    title: str,
    overview: str,
    items: list[CandidateItem],
    annotations: list[dict[str, str]],
    timezone_name: str,
) -> str:
    tz = ZoneInfo(timezone_name)
    date_label = datetime.now(tz).strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# {title}",
        "",
        f"> 更新时间：{date_label}",
        "",
        f"> {overview}",
        "",
    ]
    if not items:
        lines.append("今日未发现高相关行业线索。")
        return "\n".join(lines)
    for index, (item, annotation) in enumerate(zip(items, annotations), start=1):
        lines.extend(
            [
                f"## {index}. [{item.title}]({item.url})",
                f"- 来源：{item.source_name}",
                f"- 摘要：{annotation['summary']}",
                f"- 你可留意：{annotation['why_it_matters']}",
                f"- 标签：{format_match_badges(item.matches)}",
                "",
            ]
        )
    return "\n".join(lines)


def build_feishu_card(title: str, overview: str, items: list[CandidateItem], annotations: list[dict[str, str]]) -> dict[str, Any]:
    elements: list[dict[str, Any]] = [
        {
            "tag": "markdown",
            "content": f"**{title}**\n\n{overview}",
        },
        {"tag": "hr"},
    ]
    for index, (item, annotation) in enumerate(zip(items, annotations), start=1):
        badge = format_match_badges(item.matches)
        content = (
            f"**来源**：{item.source_name}\n"
            f"**摘要**：{annotation['summary']}\n"
            f"**你可留意**：{annotation['why_it_matters']}\n"
            f"**标签**：{badge}\n"
            f"[查看原文]({item.url})"
        )
        elements.append(
            {
                "tag": "collapsible_panel",
                "expanded": False,
                "header": {
                    "title": {"tag": "plain_text", "content": f"{index}. {item.title}"},
                    "icon": {
                        "tag": "standard_icon",
                        "token": "down-small-ccm_outlined",
                        "size": "16px 16px",
                    },
                    "icon_position": "right",
                    "icon_expanded_angle": -180,
                },
                "border": {"color": "grey", "corner_radius": "5px"},
                "elements": [{"tag": "markdown", "content": content}],
            }
        )
    return {
        "msg_type": "interactive",
        "card": {
            "schema": "2.0",
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {"tag": "plain_text", "content": title},
                "template": "orange",
            },
            "body": {"elements": elements},
        },
    }


def post_to_feishu(webhook_url: str, payload: dict[str, Any]) -> None:
    response = httpx.post(webhook_url, json=payload, timeout=30.0)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, dict):
        code = data.get("code", data.get("StatusCode", 0))
        if code not in (0, "0", None):
            raise RuntimeError(f"Feishu webhook failed: {data}")


def save_outputs(output_dir: Path, report: str, payload: dict[str, Any], items: list[CandidateItem], annotations: list[dict[str, str]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    date_slug = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (output_dir / f"{date_slug}-traditional-culture-watch.md").write_text(report, encoding="utf-8")
    serializable_items = []
    for item, annotation in zip(items, annotations):
        serializable_items.append(
            {
                "title": item.title,
                "url": item.url,
                "source_name": item.source_name,
                "published_at": item.published_at.isoformat(),
                "query_name": item.query_name,
                "matches": item.matches,
                "heuristic_score": item.heuristic_score,
                "summary": annotation["summary"],
                "why_it_matters": annotation["why_it_matters"],
            }
        )
    (output_dir / f"{date_slug}-traditional-culture-watch.json").write_text(
        json.dumps({"payload": payload, "items": serializable_items}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Traditional culture watch for Horizon.")
    parser.add_argument(
        "--config",
        default="data/traditional_culture_watch.json",
        help="Path to the watch config JSON.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build outputs without sending the webhook.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    config_path = Path(args.config)
    config = load_json(config_path)
    items = build_candidates(config)
    selected = items[: int(config["max_items"])]
    overview, annotations = enrich_with_ai(selected, config)
    title = f'{config["title"]} | {datetime.now(ZoneInfo(config["timezone"])).strftime("%Y-%m-%d")}'
    report = build_markdown_report(title, overview, selected, annotations, config["timezone"])
    payload = build_feishu_card(title, overview, selected, annotations)
    save_outputs(Path("data/traditional-culture-watch"), report, payload, selected, annotations)

    print(report)
    if args.dry_run:
        return 0

    webhook_url = os.getenv("HORIZON_WEBHOOK_URL", "").strip()
    if not webhook_url:
        raise RuntimeError("HORIZON_WEBHOOK_URL is not set")
    post_to_feishu(webhook_url, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
