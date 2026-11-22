# Bảng task (nguồn sự thật về "ai đang làm gì")

Mọi thành viên/agent **đọc file này trước khi làm**, nhận task theo quy trình ở `AGENTS.md` §0.
Chỉ sửa dòng task của mình (và thêm dòng mới ở cuối bảng). Ngày theo định dạng `DD/MM HH:MM`.

**Trạng thái:** `todo` (trống, ai cũng nhận được) · `doing` (đã có người nhận, **không đụng vào**) ·
`blocked` (ghi lý do) · `done` (ghi 1 dòng kết quả + file liên quan).

**Người nhận:** `Kiên`, `Nam`, `Sơn`, `Tri`, `Trung`, có thể kèm agent, vd. `Sơn/Claude`.

## Đang mở

| ID | Task | Người nhận | Trạng thái | Phụ thuộc | Cập nhật / kết quả |
|---|---|---|---|---|---|
| T02 | BT 22/11 – Mục 1: chọn đoạn mã có câu lệnh điều kiện (không quá đơn giản), đưa vào `bt-short-nhom/22-11/src/` | | todo | – | |
| T03 | BT 22/11 – Mục 2: thiết kế test case (nêu rõ tool dùng nếu có) | | todo | T02 | |
| T04 | BT 22/11 – Mục 3: đánh giá độ bao phủ của bộ test (statement/branch/condition…) | | todo | T03 | |
| T05 | BT 22/11 – Mục 4: so sánh khả năng sinh test của các công cụ / tiêu chí khác nhau | | todo | T02 | |
| T06 | BT 22/11 – Mục 5: kiểm tra lại bằng phân tích trực tiếp, tổng hợp ý kiến nhóm | | todo | T03, T04 | |
| T07 | BT 22/11 – Hoàn thiện báo cáo `bt-short-nhom/22-11/report/`, build PDF, nộp | | todo | T02–T06 | |
| T10 | BTL – Đọc 3 hướng đề tài (`docs/btl-de-tai.md`), mỗi người đề xuất 1 hướng + lý do | | todo | – | |
| T11 | BTL – Chốt đề tài, đăng ký với GV, cập nhật `btl/README.md` | | todo | T10 | |

## Đã xong

| ID | Task | Người làm | Kết quả |
|---|---|---|---|
| T01 | Setup repo: cấu trúc thư mục, AGENTS.md, README, template LaTeX báo cáo/slide, script | Sơn/Claude | Template build được bằng tectonic (XeLaTeX); `scripts/`, `templates/` |
