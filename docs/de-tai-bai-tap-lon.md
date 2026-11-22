# Bài tập lớn – tóm tắt 3 hướng đề tài của giảng viên

Nguồn: `docs/org/Dinh_huong_{1,2,3}_*.pdf` (chỉ có ở máy, không đưa lên git). Đây là bản tóm tắt
để nhóm chọn đề tài – chi tiết và thang điểm đầy đủ xem PDF gốc. Nhóm **chưa chọn**.

Yêu cầu chung cả 3 hướng: có **thực nghiệm thật + số liệu đo**, có **phương pháp đối chứng
(baseline)**, giải thích được kết quả, tái lập được từ mã nguồn; không chấm cao chỉ vì "gọi được
API LLM"; không dùng số liệu giả lập.

## Hướng 1 – LLM-based Test Generation (sinh test bằng LLM để tăng độ bao phủ)

- **Bài toán:** dùng LLM sinh test case chất lượng cao (coverage lớn, phát hiện lỗi).
- **Đối tượng kiểm thử:** tự chọn 1 chương trình Java/Python có 3–5 hàm, có if/else, vòng lặp,
  ngoại lệ (vd. quản lý tài khoản, giỏ hàng, GPA, ngân hàng, đặt vé).
- **Tối thiểu 2 chiến lược:** (1) Direct LLM generation; (2) **Coverage-guided** – chạy test, đo
  coverage, đưa nhánh chưa phủ cho LLM sinh thêm, lặp lại.
- **Đo:** statement, branch, function coverage (JaCoCo / coverage.py); **mutation score** (PIT /
  mutmut); số test, thời gian sinh/chạy, chi phí LLM.
- **So sánh 4 phương pháp:** P1 thủ công, P2 random, P3 direct LLM, P4 coverage-guided LLM; chạy
  nhiều lần để tính đến tính ngẫu nhiên.
- **RQ1–RQ6:** mức coverage của LLM; coverage-guided có hơn direct không; LLM có phát hiện lỗi tốt
  hơn random không; phản hồi nhánh chưa phủ có giúp không; quan hệ số test – coverage – mutation
  score; chi phí có xứng đáng không.
- **Nộp:** source, prompts, test suite sinh ra, kết quả chạy, coverage report, mutation report,
  bảng so sánh, script tái lập, báo cáo khoa học. Demo trực tiếp vòng lặp coverage-guided.
- **Điểm (10):** tổng quan 1 · thiết kế phương pháp 2 · công cụ + thực nghiệm 2 · coverage &
  mutation 2 · so sánh/thảo luận 2 · báo cáo/tái lập 1.
- Gần nhất với nội dung bài tập trên lớp (test case, coverage). Phạm vi rõ, dễ đo.

## Hướng 2 – AI-assisted Model Checking (AI hỗ trợ kiểm chứng mô hình)

- **Bài toán:** tích hợp LLM vào quy trình model checking; kết luận cuối cùng **phải do model
  checker xác nhận** (SPIN/Promela khuyến nghị; NuSMV, TLA+/TLC…).
- **Chọn 1 hoặc kết hợp các hướng con:** (1) LLM sinh mô hình từ mô tả (≥ 3 hệ thống);
  (2) LLM sinh thuộc tính LTL/CTL (≥ 20 yêu cầu); (3) **LLM phân tích counterexample** và đề xuất
  sửa (≥ 10 counterexample) – *GV khuyến nghị*; (4) giảm state space; (5) workflow tích hợp.
- **Bài toán mẫu:** producer–consumer, mutual exclusion, đèn giao thông, dining philosophers,
  lập lịch real-time.
- **So sánh:** Manual vs AI-direct vs AI-iterative vs AI+Human (tối thiểu 1 AI + 1 baseline);
  chọn ≥ 3 RQ; phải phân tích ít nhất 1 trường hợp AI thất bại.
- **Điểm (10):** tổng quan 1,5 · bài toán & phương pháp 1,5 · mô hình + tích hợp AI 2 ·
  thực nghiệm 2 · phân tích 2 · báo cáo/mã/demo 1.
- Cần học thêm Promela/LTL; phù hợp nếu nhóm thích formal methods.

## Hướng 3 – Agentic Software Testing (AI Agent tự động kiểm thử)

- **Bài toán:** xây AI Agent (hoặc multi-agent) chạy quy trình: phân tích yêu cầu → lập kế hoạch
  → sinh test → sinh mã test → thực thi → phân tích → báo cáo.
- **8 hướng con:** sinh test từ SRS · sinh mã test & thực thi · GUI testing (Playwright/Selenium)
  · API testing (OpenAPI) · chẩn đoán lỗi từ log · multi-agent · regression test selection ·
  đánh giá độ tin cậy của agent (precision/recall/F1 trên lỗi cài sẵn).
- **GV khuyến nghị:** multi-agent tự lập kế hoạch, sinh, thực thi, tự đánh giá; hoặc API testing
  agent từ OpenAPI; hoặc self-reflective testing agent.
- **Thực nghiệm gợi ý:** hệ thống quản lý sinh viên nhỏ (7 chức năng), 40–60 test, 10–15 lỗi cài
  chủ đích, ≥ 3 lần chạy mỗi cấu hình; có ground truth độc lập.
- **Điểm (100):** tổng quan 15 · phương pháp & kiến trúc 15 · hệ thống 25 · thực nghiệm & đối
  chứng 15 · phân tích định lượng 15 · độ tin cậy/hạn chế 10 · báo cáo & demo 5.
- Khối lượng code lớn nhất (agent framework, ứng dụng đối tượng); chia việc cho 5 người dễ.

## Cấu trúc báo cáo chung (cả 3 hướng gần giống nhau)

1. Introduction (động lực, bài toán, mục tiêu, RQ, đóng góp)
2. Background & Related Work
3. Proposed Approach
4. Experimental Design (đối tượng, môi trường, baseline, chỉ số, quy trình)
5. Results & Discussion (trả lời từng RQ, threats to validity)
6. Conclusion & Future Work
