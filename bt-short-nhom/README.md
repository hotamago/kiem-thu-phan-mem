# Bài tập nhóm ngắn trên lớp

Mỗi buổi một thư mục `DD-MM/` (ngày giao bài):

```
DD-MM/
├── task.md       # đề bài (chép nguyên văn) + ảnh/đính kèm của GV
├── report/       # báo cáo LaTeX -> report/main.pdf là bản nộp
├── src/          # mã nguồn đối tượng kiểm thử
├── tests/        # test case / mã test
└── results/      # kết quả chạy: coverage, mutation, ảnh chụp công cụ
```

Tạo báo cáo cho buổi mới:

```bash
python3 scripts/new_doc.py report bt-short-nhom/DD-MM/report \
  --kind "BÁO CÁO BÀI TẬP NHÓM TRÊN LỚP" --title "..." --short "BT DD/MM"
```

Đề thường yêu cầu nộp: **Nhóm số**, **Danh sách HV tham gia**, rồi lần lượt các mục 1, 2, 3… –
trang bìa và bảng "Thông tin nhóm" của template đã có sẵn hai phần đầu. Chia việc qua
`docs/tasks.md`, checklist nộp ở `AGENTS.md` §7.

| Buổi | Nội dung | Báo cáo |
|---|---|---|
| [22-11](22-11/task.md) | Thiết kế test case, đánh giá độ bao phủ cho mã có câu lệnh điều kiện | `22-11/report/` |
