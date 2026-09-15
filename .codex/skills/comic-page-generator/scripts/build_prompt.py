#!/usr/bin/env python3
"""Build a project-grounded comic prompt from style, storyboard, and theme IDs."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA_DIR = ROOT / "data-and-prompts"
STYLE_FILE = DATA_DIR / "漫画类型_120种_GPT_Image_2.5提示词库.csv"
STORYBOARD_FILE = DATA_DIR / "分镜机制库.csv"

def find_row(path: Path, identifier: int) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            if int(row.get("id") or row.get("序号") or 0) == identifier:
                return row
    raise ValueError(f"ID {identifier} was not found in {path.name}")

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--style", type=int, required=True, help="Style ID (1–120)")
    parser.add_argument("--storyboard", type=int, required=True, help="Storyboard ID (1–80)")
    parser.add_argument("--theme", required=True, help="Story to depict")
    args = parser.parse_args()
    if not 1 <= args.style <= 120: parser.error("--style must be between 1 and 120")
    if not 1 <= args.storyboard <= 80: parser.error("--storyboard must be between 1 and 80")
    if not args.theme.strip(): parser.error("--theme cannot be empty")
    style = find_row(STYLE_FILE, args.style)
    board = find_row(STORYBOARD_FILE, args.storyboard)
    prompt = "\n\n".join([
        f"主题：{args.theme.strip()}。",
        style["GPT_Image_2_5_核心提示词"],
        f"分镜机制：{board['名称']}。{board['简短说明']} 让该分镜机制真正决定页面结构、阅读顺序、主次画格和镜头节奏。",
        "输出一张完整、单页、可阅读的漫画页面；所有画格共同讲述同一段连续事件，角色外观在各格保持一致。仅在必要处放置简短、清晰、符合主题的中文对白或音效，不要水印、UI、编号说明或分割成彼此无关的图片。",
    ])
    print(prompt)

if __name__ == "__main__": main()
