"""Tạo báo cáo/slide mới từ template (chỉ dùng thư viện chuẩn).

    python3 scripts/new_doc.py report bt-short-nhom/29-11/report \
        --kind "BÁO CÁO BÀI TẬP NHÓM TRÊN LỚP" --title "..." --subtitle "..." --short "..."
    python3 scripts/new_doc.py slide btl/slide --title "..." --short "..."

Copy templates/<report|slide>/ sang thư mục đích (phải chưa tồn tại hoặc rỗng) rồi điền các
macro \\DocKind, \\DocTitle, \\DocSubtitle, \\DocShort, \\DocDate, \\DocLecturer trong file .tex chính.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = {"report": "main.tex", "slide": "slides.tex"}
FIELDS = ["kind", "title", "subtitle", "short", "date", "lecturer"]


def set_macro(text: str, name: str, value: str) -> str:
    """Replace the body of `\\newcommand{\\<name>}{...}` (single line) with `value`."""
    pattern = re.compile(r"(\\newcommand\{\\" + name + r"\}\{)[^\n]*?(\})(\s*(%[^\n]*)?)$", re.M)
    new, n = pattern.subn(lambda m: m.group(1) + value + m.group(2) + m.group(3), text, count=1)
    if n == 0:
        print(f"  (bỏ qua: template không có \\{name})")
    return new


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("type", choices=sorted(MAIN))
    ap.add_argument("dest", help="thư mục đích, vd. bt-short-nhom/29-11/report")
    for f in FIELDS:
        ap.add_argument(f"--{f}")
    ap.add_argument("--toc", action="store_true", help="(report) in mục lục")
    args = ap.parse_args()

    src = ROOT / "templates" / args.type
    dest = Path(args.dest).resolve()
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"Thư mục đích đã có nội dung: {dest}")
    shutil.copytree(src, dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.pdf", "*.log"))

    main_tex = dest / MAIN[args.type]
    text = main_tex.read_text(encoding="utf-8")
    for f in FIELDS:
        value = getattr(args, f)
        if value is not None:
            text = set_macro(text, "Doc" + f.capitalize(), value)
    if args.toc:
        text = text.replace(r"\newif\iftoc \tocfalse", r"\newif\iftoc \toctrue")
    main_tex.write_text(text, encoding="utf-8")
    print(f"Đã tạo {dest.relative_to(ROOT) if dest.is_relative_to(ROOT) else dest}")
    print(f"Biên dịch: scripts/build_tex.sh {args.dest}")


if __name__ == "__main__":
    main()
