"""Đóng gói thư mục LaTeX thành zip để upload lên Overleaf (Compiler: XeLaTeX).

    python3 scripts/overleaf_zip.py bt-short-nhom/22-11/report [btl/slide ...]

Chỉ lấy file git đang theo dõi hoặc chưa bị .gitignore loại (không lấy file build, PDF slide
của giảng viên...). Zip ghi vào build/overleaf/<đường-dẫn-nối-bằng-_>.zip (đã gitignore).
"""

import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_SUFFIXES = {".pdf", ".zip", ".log", ".aux", ".pptx"}


def pack(src: Path) -> None:
    files = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=src, capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    # main.pdf của chính tài liệu không cần đưa lên; hình PDF trong figures/ thì giữ
    files = [f for f in files if Path(f).suffix not in SKIP_SUFFIXES or f.startswith("figures/")]
    rel = src.resolve().relative_to(ROOT)
    out = ROOT / "build/overleaf" / f"{str(rel).replace('/', '_')}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(src / f, f)
    print(f"{out.relative_to(ROOT)}: {len(files)} file")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for d in sys.argv[1:]:
        pack(Path(d))
