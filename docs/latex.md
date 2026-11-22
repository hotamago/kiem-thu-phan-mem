# Viết báo cáo / slide bằng LaTeX

Template: `templates/report/` (báo cáo, `main.tex`) và `templates/slide/` (Beamer 16:9,
`slides.tex`), style HUST đỏ/trắng, biên dịch bằng **XeLaTeX**.

## Tạo – biên dịch – kiểm tra

```bash
# 1. Tạo từ template (thư mục đích phải chưa có hoặc rỗng)
python3 scripts/new_doc.py report bt-short-nhom/29-11/report \
  --kind "BÁO CÁO BÀI TẬP NHÓM TRÊN LỚP" --title "Tên bài" --subtitle "..." --short "BT 29/11"
python3 scripts/new_doc.py slide btl/slide --title "..." --short "BTL"

# 2. Biên dịch -> PDF cạnh file .tex
scripts/build_tex.sh bt-short-nhom/29-11/report

# 3. (tuỳ chọn) render trang PDF ra PNG để soát bố cục
uv run scripts/render_pdf.py bt-short-nhom/29-11/report/main.pdf 1 2
```

Sau khi tạo: sửa khối **THÔNG TIN TÀI LIỆU** đầu `main.tex` nếu cần, thay `sections/content.tex`
(file ví dụ) bằng nội dung thật; mỗi phần lớn nên là một file `sections/<phần>.tex` riêng.

## Cài đặt trình biên dịch

- **tectonic** (khuyên dùng, một file ~30 MB, tự tải gói khi cần – lần đầu chạy mất vài phút):
  tải bản `x86_64-unknown-linux-musl` từ <https://github.com/tectonic-typesetting/tectonic/releases>,
  giải nén và đặt file `tectonic` vào `~/.local/bin/`. macOS: `brew install tectonic`.
- **TeX Live**: `sudo apt install texlive-xetex texlive-lang-other texlive-fonts-extra latexmk`.
- **Overleaf** (không cần cài gì): `python3 scripts/overleaf_zip.py <thư-mục>` → upload
  `build/overleaf/<tên>.zip` (New Project → Upload Project) → Menu → Compiler: **XeLaTeX**.

## Lưu ý

- Comment/chuỗi **tiếng Việt có dấu trong `lstlisting`** bị lỗi thứ tự chữ (hạn chế của gói
  `listings`). Viết comment trong code bằng tiếng Anh hoặc không dấu.
- `\todo{...}` hiện chữ đỏ trong PDF – bản nộp không được còn.
- Font TeX Gyre gọi theo tên file nên chạy được trên tectonic/Overleaf/TeX Live mà không cần font hệ thống.
