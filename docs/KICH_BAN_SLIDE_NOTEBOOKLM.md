# 📑 KỊCH BẢN NỘI DUNG TẠO SLIDE THUYẾT TRÌNH (DÀNH CHO NOTEBOOKLM)
## DỰ ÁN: URBANSHIELD LITE – GIÁM SÁT NGẬP NƯỚC & SỰ CỐ NGÕ HẺM BẰNG EDGE AI TRÊN CPU
### ĐỘI THI: SINGLENODE | CUỘC THI: SGU HACKATHON 2026

> **Hướng dẫn nạp vào NotebookLM:**  
> Sao chép toàn bộ nội dung file này hoặc tải file `docs/KICH_BAN_SLIDE_NOTEBOOKLM.md` lên NotebookLM làm nguồn tài liệu (Source Document). Toàn bộ nội dung kịch bản đã được tinh chỉnh chuyên sâu vào **Kiến trúc hệ thống (System Architecture)**, **Bảng công nghệ sử dụng (Technology Stack)** và **Luồng dữ liệu/thuật toán (Data & Algorithmic Pipelines)** theo đúng tiêu chí chấm điểm kỹ thuật của Ban Giám khảo.

---

## 🖥️ SLIDE 1: TRANG BÌA & TỔNG QUAN HỆ THỐNG
* **Tiêu đề lớn:** UrbanShield Lite
* **Tiêu đề phụ:** Hệ thống Giám sát Ngập nước & Sự cố Ngõ hẻm bằng Edge AI trên CPU phổ thông
* **Đội thi:** SingleNode – Trường Đại học Sài Gòn (SGU)
* **Thông điệp cốt lõi:** Kiến trúc suy luận tại biên (Edge Computing), tối ưu gói tin cảnh báo 81 Bytes & Triển khai một container trên Google Cloud Run với chi phí 0 đồng.
* **Bố cục thị giác (Nền trắng tối giản):**
  * Logo chiếc khiên bảo vệ khu phố màu xanh navy `#0F172A`.
  * Ảnh chụp thực tế giao diện WebGIS đang chạy trực tiếp: Camera AI nhận diện mốc bánh xe 50cm, vạch ngấn nước màu đỏ và bản đồ số đổi màu thời gian thực.
* **Lời thoại người nói (Speaker Notes):**
  > "Chào Thầy Cô và các bạn, em là Phát đến từ đội SingleNode. Hôm nay nhóm em xin trình bày về dự án UrbanShield Lite — giải pháp ứng dụng trí tuệ nhân tạo tại chỗ trên các máy tính CPU phổ thông có sẵn tại khu phố, nhằm phát hiện ngập nước và tai nạn giao thông tại những con đường nhỏ và ngõ hẻm hay bị ngập sâu ở Thành phố Hồ Chí Minh."

---

## 🌧️ SLIDE 2: BÀI TOÁN THỰC TẾ & THÁCH THỨC KỸ THUẬT TẠI HẠ TẦNG NGÕ HẺM
* **Tiêu đề:** Thực trạng ngõ hẻm mùa mưa & 3 bài toán kỹ thuật cần giải quyết
* **Nỗi đau dân sinh thực tế:**
  1. **Ngập nước gây chết máy:** Triều cường và mưa lớn làm đường nhỏ và hẻm trũng ngập sâu 20–40cm, bà con đi làm về không biết trước, hàng loạt xe máy bị chết máy phải dắt bộ trong đêm mưa.
  2. **Tai nạn ngã xe khó được phát hiện kịp thời:** Mặt đường dốc trơn trượt hoặc nước ngập che mất ổ gà khiến người dân dễ bị ngã xe trong hẻm vắng.
* **3 Rào cản kỹ thuật tại hạ tầng địa phương:**
  * **Rào cản 1 - Đường truyền mạng:** Kéo video liên tục về máy chủ đám mây làm nghẽn toàn bộ đường truyền mạng ngõ hẻm (ngốn khoảng 450 MB/giờ/camera).
  * **Rào cản 2 - Chi phí phần cứng:** Mua camera chuyên dụng đo ngập hoặc lắp máy trạm gắn card đồ họa GPU rời thì quá đắt đỏ, ngân sách tổ dân phố không kham nổi.
  * **Rào cản 3 - Quyền riêng tư:** Người dân lo ngại hình ảnh sinh hoạt riêng tư trong ngõ hẻm bị lưu trữ tùy tiện lên máy chủ bên ngoài.
* **Bố cục thị giác:**
  * Chia 3 cột thẻ trắng viền xám mảnh: Cột 1 (Nghẽn mạng 450 MB/h) – Cột 2 (Phần cứng GPU đắt đỏ) – Cột 3 (Nguy cơ lộ video riêng tư).
* **Lời thoại người nói (Speaker Notes):**
  > "Thực tế là mỗi khi mùa mưa đến, những con đường nhỏ và ngõ hẻm hay bị ngập sâu khiến bà con bị chết máy hoặc ngã xe rất nguy hiểm. Nhưng nếu mua camera chuyên dụng thì quá đắt đỏ, còn dùng camera thường kéo video liên tục về máy chủ thì lại làm nghẽn toàn bộ đường truyền mạng. Do đó, nhóm em đặt ra bài toán: phải đưa toàn bộ khâu phân tích AI về chạy tại chỗ trên máy tính văn phòng bình thường, và chỉ gửi đi một mẩu tin văn bản ngắn khi có sự cố."

---

## 🏛️ SLIDE 3: KIẾN TRÚC TỔNG THỂ HỆ THỐNG (SYSTEM ARCHITECTURE BLUEPRINT)
* **Tiêu đề:** Kiến trúc 3 tầng phân tách bất đồng bộ (Decoupled Edge-Cloud Architecture)
* **Sơ đồ kiến trúc chi tiết (3 Tầng):**
  * **Tầng 1 - Thu nhận tại biên (Edge Ingestion):**
    * Camera an ninh / Webcam USB dân sinh $\rightarrow$ Luồng RTSP/MJPEG 28.5 FPS nội bộ.
  * **Tầng 2 - Nhân suy luận Edge đa luồng (Decoupled Threading Core):**
    * **Luồng hiển thị video (Stream Loop):** Duy trì 28.5 FPS mượt mà cho cán bộ trực ban theo dõi trực tiếp.
    * **Hàng đợi AI bất đồng bộ (ThreadPoolExecutor):** Đẩy từng frame vào hàng đợi phân tích độc lập, hoàn toàn không làm giật lag hay tụt FPS luồng camera.
    * **Bộ nhớ đệm xoay vòng trên RAM (RAM Ring-Buffer):** Xử lý ma trận ảnh trên RAM và giải phóng tức thì (Zero-Disk write).
    * **Cơ sở dữ liệu nhúng SQLite (WAL Mode):** Ghi nhật ký cực nhanh, phân trang limit/offset, tự động dọn dẹp sau 90 ngày (Data Retention).
  * **Tầng 3 - Đám mây & Điều phối cảnh báo (Cloud & Alerting):**
    * Gói tin JSON nén 81 Bytes $\rightarrow$ Bot Telegram tự động gửi tin nhắn báo động kèm tọa độ GPS.
    * Cổng kết nối WebGIS bản đồ số trên Google Cloud Run (Single-Container Serverless).
* **Bố cục thị giác:**
  * Sơ đồ khối kiến trúc 3 tầng từ trái qua phải (Tầng thu nhận $\rightarrow$ Tầng Edge AI Core đa luồng $\rightarrow$ Tầng Cloud Alert).
* **Lời thoại người nói (Speaker Notes):**
  > "Trên slide là sơ đồ kiến trúc tổng thể của hệ thống. Nhóm em thiết kế tách biệt hoàn toàn giữa luồng phát video và luồng trí tuệ nhân tạo: máy tính khu phố vừa hiển thị video 28.5 khung hình một giây cho bảo vệ trực ban theo dõi mượt mà, vừa đưa các khung hình vào hàng đợi AI để phân tích ngầm mà không bị đứng hình. Toàn bộ hình ảnh chỉ xử lý trên bộ nhớ RAM rồi xóa ngay, không ghi đè một tệp video nào xuống ổ cứng."

---

## 🛠️ SLIDE 4: CÔNG NGHỆ SỬ DỤNG & LỰA CHỌN KỸ THUẬT (TECHNOLOGY STACK)
* **Tiêu đề:** Bảng công nghệ tinh gọn & Lý do lựa chọn kỹ thuật
* **Bảng phân hệ công nghệ chi tiết:**

| Phân hệ | Công nghệ sử dụng | Lý do kỹ thuật & Ưu thế |
| :--- | :--- | :--- |
| **Edge AI & Computer Vision** | Ultralytics YOLOv8-nano (`imgsz=320`), OpenCV Headless | Mô hình siêu gọn 3.2M tham số, suy luận CPU đạt ~32ms; thuật toán Sobel tìm mép nước và CLAHE bù sáng ban đêm |
| **Backend API Gateway** | Python 3.10, FastAPI APIRouter, Uvicorn ASGI, SQLite WAL | Kiến trúc Clean Architecture phân tách module; SQLite WAL chống xung đột ghi đồng thời; thư viện `psutil` đo RAM thực tế |
| **Frontend & WebGIS** | React 18, Vite, TailwindCSS, Leaflet WebGIS | Giao diện tải dưới 1 giây; số hóa tuyến đường ngập bằng định dạng chuẩn quốc tế GeoJSON LineString đổi màu trực quan |
| **Cloud & DevOps** | Google Cloud Run, Docker, GitHub Actions, Playwright E2E, Pytest | Triển khai 1 container duy nhất; Serverless tự co giãn từ 0 instance, miễn phí 100%; bộ test tự động 24/24 bài đạt chuẩn |

* **Lời thoại người nói (Speaker Notes):**
  > "Về mặt công nghệ, nhóm em chủ động chọn mô hình YOLOv8-nano nhỏ gọn nhất chỉ 3.2 triệu tham số để chạy nhẹ nhàng trên CPU. Kết hợp với các thuật toán thị giác máy tính truyền thống như đạo hàm Sobel tìm mép nước và cân bằng sáng thích ứng CLAHE ban đêm. Ở phía giao diện, nhóm dùng React và bản đồ số Leaflet để vẽ trực tiếp các tuyến đường ngõ hẻm theo định dạng chuẩn GeoJSON."

---

## 🌊 SLIDE 5: LUỒNG THUẬT TOÁN 1 – ĐO NGẬP HÌNH HỌC QUA BÁNH XE MÁY 50CM
* **Tiêu đề:** Pipeline đo mực nước ngập: Tận dụng vật chuẩn di động dân sinh
* **Sơ đồ 4 bước xử lý tuần tự (Algorithmic Pipeline):**
  1. **Bước 1 - Phân loại bề mặt (Surface Classification):**
     * Trích xuất vùng nửa dưới khung hình, tính phương sai toán tử Laplacian ($\nabla^2$).
     * Mặt đường nhựa khô ráo có vân nhám cao (`lap_var > 3800.0`) $\rightarrow$ Xác nhận Khô ráo (0 cm).
     * Mặt nước ngập có tính chất phản xạ và gợn sóng (`lap_var <= 3000.0`) $\rightarrow$ Kích hoạt đo đạc.
  2. **Bước 2 - Lọc vật thể chuẩn trong hành lang giao thông:**
     * Nhận diện xe máy đang lưu thông trong lòng đường (`aspect_ratio <= 1.85`).
     * Kiểm tra độ che khuất ngang (`overlap > 40%`) để loại xe đi phía sau, chỉ lấy xe rõ nhất ở tiền cảnh.
  3. **Bước 3 - Trích xuất chân bánh xe & Đạo hàm Sobel:**
     * Cắt vùng chân bánh xe (35% chiều cao phía dưới).
     * Áp dụng bộ lọc đạo hàm Sobel theo trục dọc $G_y = \frac{\partial I}{\partial y}$ quét từ trên xuống dưới để tìm đỉnh biến thiên cường độ sáng lớn nhất — chính là vị trí mép nước cắt qua lốp xe.
  4. **Bước 4 - Quy đổi hình học & Bộ làm mịn EMA:**
     * Áp dụng công thức hình học mốc 50cm:
       $$\text{Độ ngập (cm)} = 50\text{ cm} \times \left(1 - \frac{\text{Chiều cao lốp còn nổi}}{\text{Toàn bộ chiều cao lốp}}\right)$$
     * Làm mịn biến động bằng hàm làm mịn mũ EMA ($0.7 \text{ EMA cũ} + 0.3 \text{ đo mới}$).
     * Duy trì bộ đệm giữ mẫu (Sample & Hold) 6.0 giây để chống chớp nháy khi xe vừa chạy qua.
* **Lời thoại người nói (Speaker Notes):**
  > "Đây là luồng thuật toán đo ngập nước. Thay vì bắt khu phố phải đóng cọc gắn thước đo dễ bị rác quấn trôi, hệ thống tận dụng chính những chiếc xe máy chạy qua đường làm thước đo di động 50cm. Máy tính tự nhận diện bánh xe, dùng đạo hàm Sobel tìm đường ngấn nước cắt ngang lốp xe, rồi nhân theo tỷ lệ hình học để tính ra độ sâu ngập chính xác từng centimet."

---

## 🛵 SLIDE 6: LUỒNG THUẬT TOÁN 2 – PHÁT HIỆN NGÃ XE & BỘ ĐẾM BẤT ĐỘNG 5 GIÂY
* **Tiêu đề:** Pipeline phát hiện ngã xe & Máy trạng thái chống báo động giả
* **Sơ đồ 4 bước xử lý tuần tự (Algorithmic Pipeline):**
  1. **Bước 1 - Lọc ứng viên ngã (Fall Candidates):**
     * Phát hiện người nằm ngang trên mặt đường với tỷ lệ khung bao $W/H > 1.15$ hoặc xe máy đổ nghiêng nằm gần người (khoảng cách tâm $< 180\text{ px}$).
  2. **Bước 2 - Bộ lọc loại trừ người lái xe bình thường (Seated-Rider Filter):**
     * Kiểm tra tương quan không gian: Nếu phần đầu người nhô cao trên yên xe máy đang chạy bình thường $\rightarrow$ Loại bỏ ngay, không đưa vào danh sách theo dõi.
  3. **Bước 3 - Máy trạng thái đếm thời gian (State Machine Tracker):**
     * Khởi tạo bộ đếm thời gian bất động `motionless_duration_sec`.
     * Theo dõi vị trí tâm $(\Delta x, \Delta y < 25\text{ px})$ qua từng khung hình liên tiếp.
  4. **Bước 4 - Tự hủy báo nhầm & Kích hoạt khẩn cấp:**
     * *Tự hủy báo giả:* Nếu người dân chỉ cúi xuống nhặt đồ hoặc dừng xe chống chân $< 5.0\text{ giây}$ rồi đứng dậy $\rightarrow$ Bộ đếm tự động hủy bỏ.
     * *Kích hoạt khẩn cấp:* Chỉ khi nạn nhân hoặc phương tiện nằm bất động liên tục $\ge 5.0\text{ giây}$ $\rightarrow$ Lập tức phát còi cảnh báo trực quan và gửi tin cứu hộ.
* **Lời thoại người nói (Speaker Notes):**
  > "Với tính năng cảnh báo tai nạn, rào cản lớn nhất là báo động nhầm khi người dân dừng xe chống chân hoặc cúi nhặt đồ. Nhóm em đã giải quyết triệt để bằng máy trạng thái đếm thời gian: hệ thống chỉ theo dõi trong im lặng, nếu người đó đứng dậy trước 5 giây thì tự động xóa cờ; chỉ khi nạn nhân nằm bất động quá 5 giây thì mới kích hoạt báo động khẩn cấp gửi về trạm dân phòng."

---

## 📡 SLIDE 7: LUỒNG TRUYỀN THÔNG DỮ LIỆU, GÓI TIN 81 BYTES & QUYỀN RIÊNG TƯ ZERO-DISK
* **Tiêu đề:** Kiến trúc tối ưu băng thông mạng & Cam kết an toàn dữ liệu
* **Bố cục 2 cột so sánh trực quan:**
  * **Cột 1 - Tối ưu băng thông mạng (Tiết kiệm 99.98%):**
    * *Cách cũ:* Kéo video 1080p liên tục về đám mây $\rightarrow$ Tốn **450 MB mỗi giờ** cho mỗi camera, nghẽn mạng ngõ hẻm.
    * *UrbanShield Lite:* Khi bình thường không tốn một byte mạng nào. Khi có sự cố ngập hoặc tai nạn, chỉ gửi **đúng 81 Bytes** định dạng JSON nén:
      ```json
      {"node_id":"node-sgu-01","type":"FLOOD","val":30.9,"unit":"cm","time":1794102792}
      ```
  * **Cột 2 - Cam kết bảo vệ quyền riêng tư (Privacy-by-Design):**
    * Khung hình video từ camera chỉ giải mã tạm thời vào mảng NumPy trên bộ nhớ RAM.
    * Ngay sau khi suy luận AI xong, hàm tự động gọi `del frame` và kích hoạt bộ thu gom rác bộ nhớ.
    * **Cam kết Zero-Disk write: 0 byte hình ảnh/video người dân bị ghi xuống ổ đĩa cứng.**
* **Lời thoại người nói (Speaker Notes):**
  > "Điểm đột phá về mặt mạng là thay vì kéo luồng video nặng hàng trăm megabyte làm nghẽn đường truyền, máy tính tại ngõ hẻm chỉ gửi đi một mẩu tin cảnh báo nhỏ đúng 81 Bytes qua mạng di động. Đồng thời, toàn bộ hình ảnh chỉ xử lý tạm trên thanh RAM rồi tự hủy ngay lập tức, không lưu bất kỳ video nào của người dân vào ổ đĩa, bảo đảm tuyệt đối quyền riêng tư."

---

## 🏆 SLIDE 8: THỰC CHỨNG KIỂM THỬ TỰ ĐỘNG, DEPLOY CLOUD & KẾT LUẬN
* **Tiêu đề:** Minh bạch thực nghiệm (Zero Fake Data) & Sẵn sàng ứng dụng thực tế
* **Các bằng chứng khoa học minh bạch:**
  * **Bộ kiểm thử tự động 100%:** Toàn bộ **`24 / 24 bài test (Pytest & Playwright E2E)`** đều đạt PASSED, có ảnh chụp màn hình terminal thực tế lưu trong hồ sơ nghiệm thu.
  * **Thực nghiệm trên video ngập thực tế TP.HCM:** Độ trễ suy luận CPU chỉ **103.9 ms**, nhận diện ngập sâu **30 - 43 cm**, không báo động giả khi đường khô ráo (**0.0 cm**).
  * **Triển khai Cloud đạt chuẩn tiêu chí VII:** Đã đóng gói và chạy thực tế trên **Google Cloud Run** (Singapore `asia-southeast1`, tự cấp chứng chỉ bảo mật HTTPS, chi phí 0 đồng).
* **Lời kết thuyết trình:**
  > "Toàn bộ các số liệu nhóm báo cáo đều được kiểm chứng minh bạch qua 24 bài kiểm thử tự động và chạy thực nghiệm trên các video ngập lụt thực tế tại Thành phố Hồ Chí Minh. Dự án đã được đóng gói hoàn chỉnh lên Google Cloud Run với chi phí 0 đồng. Nhóm em hy vọng giải pháp nhỏ bé này sẽ giúp bà con lao động đi làm về không còn cảnh dắt xe chết máy trong đêm mưa, và người gặp nạn trong hẻm vắng luôn được phát hiện và giúp đỡ kịp thời. Em xin chân thành cảm ơn Quý Thầy Cô và các bạn!"
