# AGENTS.md – Quy ước chung cho thành viên và agent

File này là "hợp đồng" để 5 thành viên và agent của từng người (Claude Code, Codex, Cursor,
Copilot…) làm việc thống nhất trong cùng một repo. **Đọc hết trước khi sửa bất cứ thứ gì.**
`CLAUDE.md` chỉ import file này.

## 0. Quy trình nhận task – BẮT BUỘC trước khi làm

`docs/tasks.md` là bảng task chung: ai đang làm gì, task nào còn trống. Mục đích: 5 người (và
agent của họ) không làm trùng, không sửa đè lên nhau.

1. **Đồng bộ:** `git pull --rebase`, rồi đọc `docs/tasks.md`.
2. **Chọn task:**
   - Chỉ chọn task `todo` mà các task phụ thuộc đã `done`.
   - **Không** sửa file thuộc phạm vi task `doing` của người khác. Cần thì nhắn người đó hoặc ghi
     vào cột "Cập nhật".
3. **Nhận task ngay:**
   - Điền "Người nhận" (vd. `Sơn` hoặc `Sơn/Claude`), đổi trạng thái thành `doing`, ghi ngày giờ.
   - Commit riêng thay đổi đó (`chore(tasks): claim T05`) và **push ngay**, trước khi bắt đầu làm.
   - Push bị từ chối: `git pull --rebase`, xem lại. Task đã có người nhận thì chọn task khác.
4. **Trong lúc làm:** commit nhỏ, **push thường xuyên** (sau mỗi phần chạy được / viết xong một
   mục, tối thiểu khoảng mỗi giờ). Cập nhật cột "Cập nhật" khi có tiến triển đáng chú ý.
5. **Xong task:** chuyển dòng sang bảng "Đã xong", kèm 1 dòng kết quả chính + file liên quan
   → commit, push. Mở khoá các task đang `blocked` vì task này (nếu có).
6. **Phát sinh việc mới:** thêm dòng với ID kế tiếp, trạng thái `todo`. Việc lớn ngoài bảng phải
   thống nhất trong nhóm trước.
7. **Bị chặn / bỏ dở:** đổi thành `blocked` (ghi lý do) hoặc trả về `todo` (xoá tên) rồi push.

## 1. Bối cảnh

- Học phần **Kiểm chứng và Thẩm định phần mềm** (Software Verification & Validation), hệ cao
  học, Trường CNTT&TT – ĐHBK Hà Nội. **Nhóm 8**, 5 học viên (danh sách: `docs/info.md`).
- Hai loại bài:
  - **Bài tập nhóm ngắn trên lớp** – `bt-short-nhom/<DD-MM>/`, mỗi buổi một thư mục.
  - **Bài tập lớn (BTL)** – `btl/`. Nhóm **chưa chọn đề tài**; 3 hướng của giảng viên được tóm tắt
    trong `docs/btl-de-tai.md`.
- Tài liệu gốc của giảng viên (slide, đề BTL) chỉ để ở máy trong `docs/org/` (gitignored). Agent
  đọc bản tóm tắt trong `docs/`; cần chi tiết thì đọc PDF trong `docs/org/` nếu máy có.

## 2. Cấu trúc & nơi đặt file

| Thứ cần thêm | Đặt ở đâu |
|---|---|
| Đề một buổi bài tập ngắn | `bt-short-nhom/<DD-MM>/task.md`; ảnh/file đính kèm của đề → `.../assets/` |
| Báo cáo bài tập ngắn | `bt-short-nhom/<DD-MM>/report/` (LaTeX, tạo bằng `scripts/new_doc.py`) |
| Mã nguồn / test của bài tập ngắn | `bt-short-nhom/<DD-MM>/src/`, `.../tests/` |
| Hình dùng trong báo cáo | `.../report/figures/` (hình vẽ/ảnh chụp do nhóm tạo) |
| Kết quả chạy (coverage, mutation, log) | `.../results/` – báo cáo HTML nặng thì chỉ commit bản tóm tắt (csv/txt/ảnh) |
| BTL: mã nguồn, thực nghiệm | `btl/` (cấu trúc con chốt sau khi chọn đề tài, ghi vào `btl/README.md`) |
| BTL: báo cáo / slide | `btl/report/`, `btl/slide/` |
| Template LaTeX dùng chung | `templates/report/`, `templates/slide/` – chỉ sửa khi cả nhóm cần |
| Script tiện ích | `scripts/` (Python chỉ dùng thư viện chuẩn, hoặc khai báo phụ thuộc kiểu PEP 723 để chạy bằng `uv run`) |
| Tài liệu chung, ghi chú họp | `docs/` |

Mỗi tài liệu LaTeX là một thư mục **tự chứa** (có `main.tex`/`slides.tex`, `sections/`,
`figures/`, `tables/`, `refs.bib`) để upload thẳng lên Overleaf được.

## 3. Viết báo cáo / slide (LaTeX)

Chi tiết: `docs/latex.md`. Tóm tắt:

- **Tạo mới:** `python3 scripts/new_doc.py report bt-short-nhom/29-11/report --kind "BÁO CÁO BÀI TẬP NHÓM TRÊN LỚP" --title "..." --short "..."`
  (slide: `python3 scripts/new_doc.py slide <thư-mục> ...`).
- **Biên dịch:** `scripts/build_tex.sh <thư-mục>` (XeLaTeX qua tectonic hoặc latexmk). Không có
  LaTeX thì dùng Overleaf: `python3 scripts/overleaf_zip.py <thư-mục>` rồi upload zip, chọn
  Compiler = XeLaTeX.
- **Kiểm tra bố cục:** `uv run scripts/render_pdf.py <file.pdf> 1 2` → PNG trong `_render/`.
- Mỗi người viết phần của mình trong **file riêng** `sections/<phần>.tex` rồi `\input` vào
  `main.tex` → ít xung đột khi merge. Phần chưa xong đánh dấu `\todo{...}` (hiện chữ đỏ trong PDF);
  bản nộp không được còn `\todo`.
- Thông tin nhóm (tên, MSHV) nằm ở `sections/titlepage.tex` và `sections/members.tex`; nguồn
  chuẩn là `docs/info.md`.
- Bảng dùng `booktabs`, hình đặt trong `figures/`, trích dẫn qua `refs.bib` (`\cite{key}`).
- **PDF:** chỉ commit PDF khi chốt một phiên bản để cả nhóm xem/nộp (commit riêng,
  `docs(report): build PDF`). Xung đột ở file PDF → lấy bên nào cũng được rồi build lại từ `.tex`
  mới nhất.

## 4. Nguyên tắc nội dung (quan trọng với môn này)

- **Không bịa số liệu.** Mọi con số coverage, mutation score, thời gian, số test… phải đo thật và
  có file kết quả/lệnh tái lập trong repo. Đề BTL ghi rõ: không dùng số liệu giả lập thay cho số
  liệu thực nghiệm.
- Ghi lại **công cụ + phiên bản + lệnh chạy** (JUnit/JaCoCo/PIT, pytest/coverage.py, EvoSuite,
  Randoop, LLM nào, prompt, temperature…). Dùng LLM sinh test → lưu prompt và output gốc.
- Trích dẫn phải có thật và đã kiểm tra bản gốc; chưa kiểm chứng thì ghi `UNVERIFIED` trong
  ghi chú, không đưa vào bản nộp.
- Đoạn mã ví dụ lấy từ sách/slide phải ghi nguồn.

## 5. Git workflow

- Nhánh chính: **`main`**, luôn biên dịch/chạy được.
  - `docs/tasks.md`, tài liệu, báo cáo: commit **thẳng vào `main`** và push ngay.
  - Code lớn hoặc có rủi ro: nhánh `feat/<tên-ngắn>` → Pull Request → merge sớm (trong ngày).
    Không giữ nhánh riêng lâu.
- Luôn `git pull --rebase` trước khi push. Không `push --force` lên `main`.
- Commit nhỏ, message tiếng Anh dạng Conventional Commits: `feat: …`, `fix: …`, `docs: …`,
  `test: …`, `chore(tasks): …`. Phạm vi gợi ý: `docs(bt-22-11): …`, `feat(btl): …`.
- **Không bao giờ commit:** slide/đề của giảng viên (`docs/org/`, `docs/*.zip`), `.env`, API key,
  file build (`*.aux`, `*.log`, `build/`, `target/`…), file lớn > 10 MB.

## 6. Ngôn ngữ & phong cách

- Tài liệu (`docs/`, README, báo cáo, slide): **tiếng Việt có dấu đầy đủ**.
- Code, tên biến, commit message: tiếng Anh; comment trong code tiếng Việt hoặc Anh đều được.
- Ngày giờ trong `docs/tasks.md`: `DD/MM HH:MM`.
- Tên file/thư mục: chữ thường, không dấu, nối bằng `-` (vd. `vi-du-days-in-month.png`); ảnh đặt
  tên theo nội dung, không để `download.png`, `image (1).png`. Thư mục theo buổi: `DD-MM`.
- File Markdown: có tiêu đề `#`, dùng danh sách/bảng/khối code thay cho văn bản dán thô; chép đề
  của giảng viên nguyên văn nhưng định dạng lại. Văn bản copy từ macOS/Notion có thể ở dạng Unicode
  tổ hợp (NFD) làm grep/tìm kiếm không khớp → chuẩn hoá về NFC trước khi commit.

## 7. Checklist nộp bài tập ngắn

Đề thường yêu cầu: **Nhóm số**, **Danh sách học viên tham gia**, rồi trả lời lần lượt các mục 1,
2, 3… của đề.

- [ ] Trang bìa + bảng "Thông tin nhóm" đúng 5 người, cột "Công việc" đã điền.
- [ ] Mỗi mục của `task.md` có một section tương ứng, đúng thứ tự.
- [ ] Số liệu có nguồn (file trong `results/` hoặc ảnh chụp công cụ).
- [ ] Không còn `\todo`; build sạch; PDF đã commit; ghi link/đường dẫn PDF vào `docs/tasks.md`.
