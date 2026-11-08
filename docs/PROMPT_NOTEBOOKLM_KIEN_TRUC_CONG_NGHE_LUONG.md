# 🏛️ PROMPT NOTEBOOKLM TẠO SLIDE CHUYÊN SÂU: KIẾN TRÚC, CÔNG NGHỆ & LUỒNG XỬ LÝ
## DỰ ÁN: URBANSHIELD LITE – HACKATHON SGU 2026

> **Mục tiêu prompt:** Tối ưu hóa cho Ban Giám khảo chấm điểm chuyên sâu về **Kiến trúc hệ thống (Architecture)**, **Công nghệ cốt lõi (Tech Stack)** và **Luồng dữ liệu xử lý (Data Flow Pipelines)**, giữ phong cách nền trắng tối giản (Minimalist White Background) và 100% văn nói mộc mạc, không khoa trương (Anti-hype).

---

### 📋 NỘI DUNG MASTER PROMPT (COPY VÀ DÁN TRỰC TIẾP VÀO NOTEBOOKLM)

```text
Dựa vào toàn bộ tài liệu nguồn của dự án UrbanShield Lite đã tải lên, hãy đóng vai trò là một Kỹ sư Kiến trúc Phần mềm kiêm Chuyên gia Thiết kế Thuyết trình Kỹ thuật (Lead System Architect & Presentation Designer). Hãy xây dựng nội dung chi tiết cho bộ slide gồm 8 slide thuyết trình chuyên sâu, TẬP TRUNG CHỦ ĐẠO VÀO:
1. KIẾN TRÚC HỆ THỐNG (System Architecture & Decoupled Threading).
2. CÔNG NGHỆ SỬ DỤNG (Technology Stack & Engineering Decisions).
3. LUỒNG DỮ LIỆU & LUỒNG XỬ LÝ THUẬT TOÁN (Data & Algorithmic Pipelines).

---
### QUY CHUẨN TRÌNH BÀY THỊ GIÁC (MINIMALIST WHITE SLIDE):
- Tone màu: Nền trắng (#FFFFFF) hoặc xám sáng (#F8FAFC), viền thẻ xám siêu mảnh (#E2E8F0), chia khối dạng sơ đồ hộp (Block Diagram) và quy trình mũi tên (Pipeline Flowchart).
- Màu điểm nhấn kỹ thuật:
  + Xanh dương (#2563EB): Các khối thu nhận hình ảnh, thuật toán thị giác máy tính và mốc đo 50cm.
  + Đỏ an toàn (#DC2626): Bộ phát hiện ngã xe 5s và ngưỡng báo động ngập >20cm.
  + Xanh lá cây (#16A34A): Tối ưu băng thông gói tin 81 Bytes, cam kết 0 byte ghi đĩa (Zero-Disk) và tiết kiệm 99.98% mạng.
- Ngôn từ thuyết trình (Speaker Notes): 100% văn nói mộc mạc đời thường của sinh viên CNTT (xưng "em", gọi "Thầy Cô và các bạn"). Tuyệt đối KHÔNG dùng từ khoa trương ("siêu AI", "siêu nhẹ", "thời gian vàng cứu hộ"). Số liệu trung thực trích xuất từ runtime CPU/RAM thực tế.

---
### CHI TIẾT NỘI DUNG 8 SLIDE YÊU CẦU XUẤT RA:

#### SLIDE 1: TRANG BÌA & TỔNG QUAN HỆ THỐNG
- Tiêu đề: UrbanShield Lite – Hệ thống Giám sát Ngập nước & Sự cố Ngõ hẻm bằng Edge AI trên CPU.
- Phụ đề: Kiến trúc suy luận tại biên, tối ưu băng thông 81 Bytes & Triển khai một vùng chứa trên Google Cloud.
- Khối thông tin: Đội thi SingleNode | SGU Hackathon 2026.
- Lời thoại (Speaker Notes): "Chào Thầy Cô và các bạn, em là Phát đến từ đội SingleNode. Hôm nay nhóm em xin trình bày về dự án UrbanShield Lite – giải pháp giám sát ngập lụt và tai nạn giao thông tại các con đường nhỏ và ngõ hẻm, chạy trực tiếp trên máy tính CPU phổ thông tại khu phố."

#### SLIDE 2: BÀI TOÁN THỰC TẾ & RÀO CẢN HẠ TẦNG KỸ THUẬT
- Tiêu đề: Nỗi đau dân sinh ngõ hẻm & 3 bài toán hạ tầng mạng - phần cứng
- Bố cục: 3 khối so sánh đối xứng:
  + Rào cản 1 - Đường truyền mạng: Kéo video camera liên tục về máy chủ đám mây làm nghẽn toàn bộ đường truyền ngõ hẻm (ngốn 450 MB/giờ/camera).
  + Rào cản 2 - Chi phí thiết bị: Mua camera AI chuyên dụng hoặc máy trạm gắn card đồ họa GPU rời thì quá đắt đỏ, ngân sách khu phố không kham nổi.
  + Rào cản 3 - Quyền riêng tư: Người dân lo ngại hình ảnh sinh hoạt trong ngõ hẻm bị lưu trữ tùy tiện lên máy chủ bên ngoài.
- Lời thoại (Speaker Notes): "Thực tế là mỗi khi mùa mưa đến, những con đường nhỏ và ngõ hẻm hay bị ngập sâu khiến bà con bị chết máy hoặc ngã xe rất nguy hiểm. Nhưng nếu mua camera chuyên dụng thì quá đắt đỏ, còn dùng camera thường kéo video liên tục về máy chủ thì lại làm nghẽn toàn bộ đường truyền mạng. Do đó, nhóm em đặt ra bài toán: phải đưa toàn bộ khâu phân tích AI về chạy tại chỗ trên máy tính văn phòng bình thường, và chỉ gửi đi một mẩu tin văn bản ngắn khi có sự cố."

#### SLIDE 3: KIẾN TRÚC TỔNG THỂ HỆ THỐNG (SYSTEM ARCHITECTURE BLUEPRINT)
- Tiêu đề: Kiến trúc 3 tầng phân tách bất đồng bộ (Decoupled Edge-Cloud Architecture)
- Sơ đồ trực quan:
  + Tầng 1 (Edge Ingestion): Camera an ninh / Webcam USB $\rightarrow$ Luồng RTSP/MJPEG 28.5 FPS.
  + Tầng 2 (Edge Inference Core): Kiến trúc đa luồng bất đồng bộ (Decoupled Threading):
    * Luồng phát video (Stream Loop): Luôn duy trì 28.5 FPS mượt mà cho giám sát viên.
    * Hàng đợi AI (ThreadPoolExecutor): Chạy suy luận YOLOv8n độc lập mà không bao giờ làm giật khung hình camera.
    * Vùng nhớ tạm RAM Ring-Buffer: Xử lý và giải phóng ngay lập tức (Zero-Disk write).
    * Cơ sở dữ liệu SQLite cục bộ (WAL Mode): Ghi nhật ký nhanh, phân trang limit/offset, tự động dọn dẹp sau 90 ngày.
  + Tầng 3 (Cloud & Alerting): Gói tin nén 81 Bytes $\rightarrow$ Telegram Bot Alert + Google Cloud Run Single-Container WebGIS.
- Lời thoại (Speaker Notes): "Trên slide là sơ đồ kiến trúc tổng thể của hệ thống. Nhóm em thiết kế tách biệt hoàn toàn giữa luồng phát video và luồng trí tuệ nhân tạo: máy tính khu phố vừa hiển thị video 28.5 khung hình một giây cho bảo vệ trực ban theo dõi mượt mà, vừa đưa các khung hình vào hàng đợi AI để phân tích ngầm mà không bị đứng hình. Toàn bộ hình ảnh chỉ xử lý trên bộ nhớ RAM rồi xóa ngay, không ghi đè một tệp video nào xuống ổ cứng."

#### SLIDE 4: CÔNG NGHỆ SỬ DỤNG & LỰA CHỌN KỸ THUẬT (TECHNOLOGY STACK)
- Tiêu đề: Bảng công nghệ tinh gọn & Lý do lựa chọn (Tech Stack Decisions)
- Bố cục bảng 4 cột:
  + Edge AI & Computer Vision: Ultralytics YOLOv8-nano (imgsz=320, 3.2M params), OpenCV Headless (Đạo hàm Sobel, Phương sai nhám Laplacian, Cân bằng sáng thích ứng CLAHE trên không gian màu LAB).
  + Backend Gateway: Python 3.10, FastAPI APIRouter (Clean Architecture), Uvicorn ASGI, Thư viện chuẩn psutil đo kiểm RAM hệ điều hành.
  + Frontend & WebGIS: React 18, Vite, TailwindCSS, Bản đồ số tương tác Leaflet (Hiển thị các tuyến đường ngõ hẻm bằng chuẩn GeoJSON LineString).
  + Cloud & DevOps: Google Cloud Run (Serverless tự co giãn từ 0 instance, chuẩn container Docker), GitHub Actions CI/CD, Bộ kiểm thử tự động Pytest & Playwright E2E.
- Lời thoại (Speaker Notes): "Về mặt công nghệ, nhóm em chủ động chọn mô hình YOLOv8-nano nhỏ gọn nhất chỉ 3.2 triệu tham số để chạy nhẹ nhàng trên CPU. Kết hợp với các thuật toán thị giác máy tính truyền thống như đạo hàm Sobel tìm mép nước và cân bằng sáng thích ứng CLAHE ban đêm. Ở phía giao diện, nhóm dùng React và bản đồ số Leaflet để vẽ trực tiếp các tuyến đường ngõ hẻm theo định dạng chuẩn GeoJSON."

#### SLIDE 5: LUỒNG THUẬT TOÁN 1 – ĐO NGẬP HÌNH HỌC QUA BÁNH XE MÁY 50CM
- Tiêu đề: Pipeline đo mực nước ngập: Tận dụng vật chuẩn di động dân sinh
- Các bước trong luồng xử lý:
  + Bước 1 - Phân loại bề mặt: Đo phương sai Laplacian (lap_var > 3800) để phân biệt chính xác mặt đường nhựa khô ráo với mặt nước ngập có sóng gợn.
  + Bước 2 - Lọc vật thể chuẩn: Lọc xe máy đang chạy trong hành lang giao thông (aspect_ratio <= 1.85, loại trừ xe bị che khuất).
  + Bước 3 - Trích xuất chân bánh xe: Cắt vùng ROI 35% phía dưới bánh xe và áp dụng đạo hàm Sobel theo trục dọc tìm đỉnh chuyển tiếp mép nước.
  + Bước 4 - Quy đổi hình học & Làm mịn: Áp dụng công thức hình học: Độ ngập (cm) = 50cm * (1 - tỷ lệ lộ của bánh xe). Làm mịn dữ liệu bằng bộ lọc EMA (0.7 EMA cũ + 0.3 đo mới) và duy trì bộ nhớ đệm 6 giây chống chớp nháy.
- Lời thoại (Speaker Notes): "Đây là luồng thuật toán đo ngập nước. Thay vì bắt khu phố phải đóng cọc gắn thước đo dễ bị rác quấn trôi, hệ thống tận dụng chính những chiếc xe máy chạy qua đường làm thước đo di động 50cm. Máy tính tự nhận diện bánh xe, dùng đạo hàm Sobel tìm đường ngấn nước cắt ngang lốp xe, rồi nhân theo tỷ lệ hình học để tính ra độ sâu ngập chính xác từng centimet."

#### SLIDE 6: LUỒNG THUẬT TOÁN 2 – PHÁT HIỆN NGÃ XE & BỘ ĐẾM BẤT ĐỘNG 5 GIÂY
- Tiêu đề: Pipeline phát hiện ngã xe & Máy trạng thái chống báo động giả
- Các bước trong luồng xử lý:
  + Bước 1 - Lọc ứng viên ngã: Nhận diện khung bao người nằm ngang (W/H > 1.15) hoặc xe máy đổ nghiêng nằm sát người (khoảng cách < 180px).
  + Bước 2 - Loại trừ người đang lái xe: Kiểm tra nếu phần đầu người nhô cao trên yên xe máy bình thường thì loại bỏ ngay.
  + Bước 3 - Máy trạng thái (State Machine): Bắt đầu bấm giờ thời gian bất động.
  + Bước 4 - Chống báo động giả: Nếu người dân chỉ cúi xuống nhặt đồ rơi hoặc chống chân dừng lại < 5.0 giây, bộ đếm tự động hủy bỏ. Chỉ khi bất động liên tục >= 5.0 giây, hệ thống mới phát chuông báo động và phát tin khẩn.
- Lời thoại (Speaker Notes): "Với tính năng cảnh báo tai nạn, rào cản lớn nhất là báo động nhầm khi người dân dừng xe chống chân hoặc cúi nhặt đồ. Nhóm em đã giải quyết triệt để bằng máy trạng thái đếm thời gian: hệ thống chỉ theo dõi trong im lặng, nếu người đó đứng dậy trước 5 giây thì tự động xóa cờ; chỉ khi nạn nhân nằm bất động quá 5 giây thì mới kích hoạt báo động khẩn cấp gửi về trạm dân phòng."

#### SLIDE 7: LUỒNG TRUYỀN THÔNG, TỐI ƯU BĂNG THÔNG 81 BYTES & QUYỀN RIÊNG TƯ
- Tiêu đề: Kiến trúc nén gói tin & Cam kết an toàn dữ liệu (Privacy-by-Design)
- Bố cục 2 phần:
  + Cột 1 - So sánh lưu lượng mạng:
    * Truyền video truyền thống: 450 MB / giờ $\rightarrow$ Gây nghẽn mạng ngõ hẻm.
    * Gói tin UrbanShield Lite: 81 Bytes / mẩu tin cảnh báo (giảm 99.98% băng thông). Gồm: mã trạm, loại sự cố, con số đo đạc, đơn vị và thời gian Unix timestamp.
  + Cột 2 - Cơ chế Privacy Zero-Disk:
    * Frame hình ảnh nạp vào mảng NumPy trên RAM.
    * Sau khi chạy suy luận YOLO xong, gọi lệnh xóa tường minh (`del frame`, `del lower_region`) giải phóng RAM tức thì.
    * 0 tệp hình ảnh hay video của người dân bị lưu vào ổ cứng máy tính.
- Lời thoại (Speaker Notes): "Điểm đột phá về mặt mạng là thay vì kéo luồng video nặng hàng trăm megabyte làm nghẽn đường truyền, máy tính tại ngõ hẻm chỉ gửi đi một mẩu tin cảnh báo nhỏ đúng 81 Bytes qua mạng di động. Đồng thời, toàn bộ hình ảnh chỉ xử lý tạm trên thanh RAM rồi tự hủy ngay lập tức, không lưu bất kỳ video nào của người dân vào ổ đĩa, bảo đảm tuyệt đối quyền riêng tư."

#### SLIDE 8: THỰC CHỨNG KIỂM THỬ TỰ ĐỘNG, DEPLOY CLOUD & KẾT LUẬN
- Tiêu đề: Minh bạch thực nghiệm (Zero Fake Data) & Triển khai thực tế
- Khối thông tin:
  + Kiểm thử tự động 100%: 24/24 bài test Pytest & Playwright E2E vượt qua hoàn hảo.
  + Đánh giá video thực tế TP.HCM: Độ trễ CPU 103.9ms, phát hiện ngập đạt độ sâu 30 - 43cm, không báo động giả khi đường khô ráo (0cm).
  + Đạt chuẩn tiêu chí Google Cloud: Đóng gói 1 container duy nhất chạy trên Google Cloud Run (Serverless, tự cấp phát chứng chỉ HTTPS, khu vực Singapore asia-southeast1, chi phí 0 đồng).
- Lời thoại (Speaker Notes): "Toàn bộ các số liệu nhóm báo cáo đều được kiểm chứng minh bạch qua 24 bài kiểm thử tự động và chạy thực nghiệm trên các video ngập lụt thực tế tại Thành phố Hồ Chí Minh. Dự án đã được đóng gói hoàn chỉnh lên Google Cloud Run với chi phí 0 đồng. Nhóm em xin cảm ơn Quý Thầy Cô và các bạn đã lắng nghe!"
```
