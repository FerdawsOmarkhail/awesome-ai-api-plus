import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT_CSV = ROOT / "data" / "apis-launch-30.csv"
OUTPUT_MD = ROOT / "docs" / "top-10-recommended.md"


CATEGORY_BONUS = {
    "video": 5,
    "multimodal-llm": 4,
    "music-audio": 3,
    "agent-infra": 2,
}

TYPE_BONUS_RULES = {
    "Text-to-video": 4,
    "Text/Image-to-video": 5,
    "Multi-model gateway API": 4,
    "Multimodal LLM": 4,
    "LLM observability": 3,
}

PRICING_BONUS = {
    "Free/Paid": 4,
    "Free": 3,
    "Paid/Trial": 2,
    "Paid": 1,
}

SOURCE_BONUS = {
    "official": 4,
    "github": 3,
}


def score_row(row: dict) -> int:
    base = 70
    category = row["category"]
    api_type = row["type"]
    pricing = row["pricing"]
    source = row["source"]

    score = base
    score += CATEGORY_BONUS.get(category, 0)
    score += PRICING_BONUS.get(pricing, 0)
    score += SOURCE_BONUS.get(source, 0)

    for key, bonus in TYPE_BONUS_RULES.items():
        if key.lower() in api_type.lower():
            score += bonus

    # Small trend bonus for known hot products
    hot_names = {"OpenAI Sora", "KLING AI", "Gemini API", "OpenRouter", "Suno", "Runway"}
    if row["name"] in hot_names:
        score += 4

    return min(score, 100)


def load_rows() -> list[dict]:
    with INPUT_CSV.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render_markdown(top10: list[dict]) -> str:
    lines = [
        "# Top 10 Recommended APIs",
        "",
        "> Generated from `data/apis-launch-30.csv` using `examples/python/generate_top10.py`.",
        ">",
        "> Heuristic score = base + category bonus + type bonus + pricing bonus + source bonus + trend bonus.",
        "",
        "| Rank | API | Category | Type | Pricing | Source | Score | Link |",
        "|---|---|---|---|---|---|---:|---|",
    ]

    for i, row in enumerate(top10, start=1):
        lines.append(
            f"| {i} | {row['name']} | {row['category']} | {row['type']} | {row['pricing']} | {row['source']} | {row['score']} | [Visit]({row['url']}) |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This ranking is for launch-stage discovery and curation, not absolute model quality benchmarking.",
            "- Re-run monthly to keep up with model and pricing changes.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_rows()
    for row in rows:
        row["score"] = score_row(row)

    rows.sort(key=lambda x: x["score"], reverse=True)
    top10 = rows[:10]
    OUTPUT_MD.write_text(render_markdown(top10), encoding="utf-8")
    print(f"Generated: {OUTPUT_MD}")


if __name__ == "__main__":
    main()

