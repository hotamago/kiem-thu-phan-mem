# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.24"]
# ///
"""Render trang PDF ra PNG để kiểm tra nhanh bố cục (agent đọc được ảnh).

    uv run scripts/render_pdf.py <file.pdf> [thư-mục-ra] [trang ...]
    vd: uv run scripts/render_pdf.py bt-short-nhom/22-11/report/main.pdf 1 2

Mặc định trang 1, ảnh ghi vào <thư mục PDF>/_render/ (đã gitignore).
"""

import sys
from pathlib import Path

import pymupdf as fitz

if len(sys.argv) < 2:
    sys.exit(__doc__)
pdf = Path(sys.argv[1])
has_out = len(sys.argv) > 2 and not sys.argv[2].isdigit()
out = Path(sys.argv[2]) if has_out else pdf.parent / "_render"
pages = [int(p) for p in sys.argv[2:] if p.isdigit()] or [1]
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
print(f"{pdf.name}: {doc.page_count} trang")
for p in pages:
    path = out / f"{pdf.stem}_p{p}.png"
    doc[p - 1].get_pixmap(dpi=80).save(path)
    print(path)
