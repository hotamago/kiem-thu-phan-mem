#!/usr/bin/env bash
# Biên dịch một tài liệu LaTeX (XeLaTeX) thành PDF.
#
#   scripts/build_tex.sh <thư-mục> [file.tex]
#   vd: scripts/build_tex.sh bt-short-nhom/22-11/report
#       scripts/build_tex.sh btl/slide slides.tex
#
# Mặc định file là main.tex (nếu không có thì slides.tex). PDF nằm cạnh file .tex.
# Ưu tiên tectonic (tự tải gói khi cần), sau đó latexmk -xelatex (TeX Live).
set -euo pipefail

dir="${1:?Cách dùng: scripts/build_tex.sh <thư-mục> [file.tex]}"
cd "$dir"
tex="${2:-}"
if [[ -z "$tex" ]]; then
  if [[ -f main.tex ]]; then tex=main.tex
  elif [[ -f slides.tex ]]; then tex=slides.tex
  else echo "Không thấy main.tex/slides.tex trong $dir" >&2; exit 1; fi
fi

if command -v tectonic >/dev/null 2>&1; then
  tectonic -X compile --keep-logs "$tex"
elif command -v latexmk >/dev/null 2>&1; then
  latexmk -xelatex -interaction=nonstopmode -halt-on-error "$tex"
else
  cat >&2 <<'MSG'
Chưa có trình biên dịch LaTeX. Chọn một trong các cách:
  - tectonic (gọn, ~30 MB): xem docs/latex.md mục "Cài đặt"
  - TeX Live: sudo apt install texlive-xetex texlive-lang-other texlive-fonts-extra latexmk
  - Hoặc dùng Overleaf: python3 scripts/overleaf_zip.py <thư-mục> rồi upload zip
MSG
  exit 1
fi
echo "-> $dir/${tex%.tex}.pdf"
