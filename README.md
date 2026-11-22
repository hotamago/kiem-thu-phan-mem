# Kiểm chứng và Thẩm định phần mềm – Nhóm 8

Repo làm việc chung của **Nhóm 8**, học phần **Kiểm chứng và Thẩm định phần mềm** (Software
Verification & Validation), hệ cao học, Trường CNTT&TT – ĐHBK Hà Nội.

| STT | Họ và tên | MSHV | Ghi chú |
|---|---|---|---|
| 1 | Trần Đức Tuấn Kiên | 20252780M | Nhóm trưởng |
| 2 | Hoàng Văn Nam | 20261263M | |
| 3 | Nguyễn Hoàng Sơn | 20261127M | |
| 4 | Nguyễn Quang Tri | 20252779M | |
| 5 | Nguyễn Nho Trung | 20261235M | |

> **Thành viên mới vào repo:** đọc [`AGENTS.md`](AGENTS.md) (quy ước làm việc, bắt buộc với cả
> người lẫn agent) và [`docs/tasks.md`](docs/tasks.md) (ai đang làm gì) trước khi bắt đầu.

## Cấu trúc thư mục

```
.
├── AGENTS.md                  # quy ước chung cho thành viên + agent (CLAUDE.md trỏ tới file này)
├── docs/
│   ├── info.md                # thông tin nhóm, link danh sách lớp
│   ├── tasks.md               # bảng task: nhận việc / cập nhật / xong
│   ├── de-tai-bai-tap-lon.md  # tóm tắt 3 hướng đề tài BTL của giảng viên
│   ├── latex.md               # hướng dẫn viết & biên dịch báo cáo/slide
│   └── org/                   # (chỉ ở máy, gitignored) slide + đề gốc của giảng viên
├── bai-tap-nhom/              # bài tập nhóm ngắn trên lớp, mỗi buổi một thư mục DD-MM/
│   └── 22-11/                 # task.md (đề) · assets/ (ảnh đề) · report/ · src/ · tests/ · results/
├── bai-tap-lon/               # bài tập lớn (chưa chọn đề tài) – report/, slide/, mã nguồn
├── templates/
│   ├── report/                # template báo cáo LaTeX (XeLaTeX, style HUST đỏ/trắng)
│   └── slide/                 # template slide Beamer 16:9
└── scripts/
    ├── new_doc.py             # tạo báo cáo/slide mới từ template
    ├── build_tex.sh           # biên dịch LaTeX -> PDF (tectonic / latexmk)
    ├── overleaf_zip.py        # đóng gói thư mục LaTeX để upload Overleaf
    └── render_pdf.py          # render trang PDF -> PNG để soát bố cục
```

## Bắt đầu nhanh

```bash
git clone git@github.com:hotamago/kiem-thu-phan-mem.git
cd kiem-thu-phan-mem

# Tạo báo cáo cho buổi bài tập mới
python3 scripts/new_doc.py report bai-tap-nhom/29-11/report \
  --kind "BÁO CÁO BÀI TẬP NHÓM TRÊN LỚP" --title "Tên bài" --short "BT 29/11"

# Biên dịch (cần tectonic hoặc TeX Live – xem docs/latex.md)
scripts/build_tex.sh bai-tap-nhom/29-11/report

# Không cài LaTeX: đóng gói rồi upload lên Overleaf (Compiler: XeLaTeX)
python3 scripts/overleaf_zip.py bai-tap-nhom/29-11/report
```

## Quy trình làm việc (tóm tắt)

1. `git pull --rebase` → mở `docs/tasks.md` → nhận task `todo` (điền tên, `doing`) → commit + push ngay.
2. Làm việc, commit nhỏ, push thường xuyên. Mỗi người viết phần của mình trong file
   `sections/<phần>.tex` riêng.
3. Xong: chuyển task sang "Đã xong" kèm kết quả chính + file liên quan → push.

Chi tiết và các quy tắc khác (không bịa số liệu, không commit tài liệu của giảng viên, …): xem
[`AGENTS.md`](AGENTS.md).

## Bài tập & tiến độ

| Bài | Thư mục | Trạng thái |
|---|---|---|
| BT nhóm 22/11 – Thiết kế test case & đánh giá độ bao phủ cho mã có câu lệnh điều kiện | [`bai-tap-nhom/22-11`](bai-tap-nhom/22-11) | đang làm |
| Bài tập lớn | [`bai-tap-lon/`](bai-tap-lon) | chưa chọn đề tài – xem [`docs/de-tai-bai-tap-lon.md`](docs/de-tai-bai-tap-lon.md) |
