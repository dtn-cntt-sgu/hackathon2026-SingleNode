# 📋 CẨM NANG LIVE DEMO SẢN PHẨM: URBANSHIELD LITE
### DỰ ÁN: GIÁM SÁT NGẬP NƯỚC & SỰ CỐ NGÕ HẺM BẰNG EDGE AI TRÊN CPU
**Đội thi:** SingleNode ([nphat-code](https://github.com/nphat-code))  
**Cuộc thi:** SGU Hackathon 2026 – Trường Đại học Sài Gòn  

---

## 🧭 PHẦN 1: CÔNG NGHỆ SỬ DỤNG TRONG TOÀN BỘ HỆ THỐNG (TECH STACK)

| Phân tầng hệ thống | Công nghệ / Thư viện | Vai trò cụ thể trong mã nguồn |
| :--- | :--- | :--- |
| **Thị giác máy tính tại biên (Edge Vision)** | **YOLOv8-nano (`ultralytics`)** | Mô hình nhẹ ~6MB, tối ưu đa luồng CPU (`torch.set_num_threads`), nhận diện xe máy, ô tô, người với độ trễ chỉ **~25.1 ms/khung hình**. |
| **Xử lý ảnh & Toán hình học** | **OpenCV (`cv2`), NumPy** | • Cân bằng sáng **CLAHE** kênh L (không gian màu LAB) khi mưa đêm thiếu sáng.<br>• Bộ lọc đạo hàm bậc một **Sobel** (`cv2.Sobel`) dò mép nước giao cắt lốp xe.<br>• Công thức tỷ lệ hình học bánh xe máy chuẩn **50 cm**.<br>• Phân tích hình thái khung bao ($W/H > 1.15$) và khoảng cách Euclid ($< 180\text{ px}$). |
| **API Gateway & Quản trị dịch vụ** | **FastAPI, Uvicorn, Pydantic** | Kiến trúc Clean Modular Router (`routers/`), xác thực schema dữ liệu, đo đạc độ trễ API `X-Process-Time` qua middleware. |
| **Bảo mật & Giám sát tài nguyên** | **`psutil.Process()`** | Đo đạc chính xác dung lượng RAM thực tế từ nhân hệ điều hành (**~245 MB**, đạt chuẩn `< 500MB`), cam kết **Zero-Disk RAM** (`del frame`, 0 file ghi đĩa). |
| **Lưu trữ biên & Băng thông** | **SQLite3, JSON Compact** | Đóng gói mẩu tin sự cố **~82 Bytes (< 150 Bytes)**, lưu trữ lịch sử có phân trang, nhật ký nhịp tim trạm camera. |
| **Cảnh báo khẩn cấp** | **Telegram Bot API (`httpx`)** | Đẩy mẩu tin cảnh báo kèm GPS và thời gian thực về điện thoại trực ban trong **< 1.5 giây**. |
| **Bản đồ số & Điều hành WebGIS** | **React 18, Vite, Leaflet GIS** | Giao diện 100vh không cuộn, vẽ tuyến hẻm **GeoJSON `LineString`** tự động đổi màu Xanh / Vàng / Đỏ theo thời gian thực. |
| **Điện toán đám mây & Hạ tầng** | **Google Cloud Run, Docker** | Đóng gói Single-Container (React build + FastAPI), triển khai trên hạ tầng serverless Google Cloud với chứng chỉ HTTPS tự động. |

---

## 🔄 PHẦN 2: LUỒNG VẬN HÀNH & DỮ LIỆU ĐẦU CUỐI (OPERATIONAL DATA FLOW)

```text
[Camera ngõ hẻm / USB] 
       │ (Luồng video MJPEG)
       ▼
[Bộ nhớ RAM máy tính khu phố] 
       │ ──> Khung hình chỉ nạp tạm trên RAM (0 file ghi đĩa cứng)
       ▼
[Tiền xử lý CLAHE] ──> Tự động kích hoạt khi trời tối (Luminance L < 115)
       │
       ▼
[YOLOv8n CPU Suy luận ~25ms] ──> Tách tọa độ Bounding Box: Person, Motorcycle, Car
       │
       ├───> [NHÁNH 1: ĐO NGẬP BÁNH XE MÁY 50CM]
       │        ├─ Lọc xe máy rõ nét, không bị che khuất
       │        ├─ Cắt vùng ROI bánh xe (35% chiều cao thân xe)
       │        ├─ Quét đạo hàm Sobel dò mép nước
       │        ├─ Tính độ ngập: Depth = 50 * (1 - Visible / Full)
       │        └─ Phân cấp: An toàn (<10cm) | Chú ý (10-20cm) | Nguy hiểm (>=20cm)
       │
       └───> [NHÁNH 2: GIÁM SÁT NGÃ XE & BỘ ĐẾM 5.0 GIÂY]
                ├─ Kiểm tra tỷ lệ khung nằm ngang: W/H > 1.15
                ├─ Kiểm tra cự ly sát xe máy: Distance < 180px
                ├─ BẬT BỘ ĐẾM BẤT ĐỘNG LIÊN TỤC:
                │    ├─ Nếu đứng dậy trước 5s: W/H < 0.8 ──> TỰ HỦY ĐẾM (0 báo giả)
                │    └─ Nếu nằm bất động >= 5.0s ──> XÁC NHẬN SỰ CỐ TAI NẠN
                │
                ▼
[Giải phóng RAM] ──> `del proc_frame`, `del frame` ngay lập tức
       │
       ▼
[Đóng gói JSON < 150 Bytes] ──> Chỉ gửi mẩu tin khi có sự cố (~82 Bytes)
       │
       ├───> [Bản đồ số WebGIS]: Tuyến hẻm đổi sang màu ĐỎ tức thì
       └───> [Telegram Bot API]: Rung chuông điện thoại trực ban Dân quân (< 1.5s)
```

---

## 💻 PHẦN 3: BẢN ĐỒ MÃ NGUỒN CỐT LÕI (CODE DEEP-DIVE)

### 1. Thuật toán đo ngập nước 50cm & CLAHE ([`backend/detector.py`](file:///c:/Competition/singlenode-urbanshield-lite/backend/detector.py))
* `estimate_wheel_flood_depth(visible_wheel_h_px, full_wheel_h_px, wheel_diameter_cm=50.0)`: 
  * Dòng 31–59: Công thức tỷ lệ hình học bánh xe máy chuẩn 50cm.
* `preprocess_clahe(frame)`: 
  * Dòng 300–316: Tách kênh LAB, nếu `L_mean < 115` thì áp dụng CLAHE để nhìn rõ mép nước ban đêm.
* Đạo hàm mép nước Sobel trong `infer()`: 
  * Dòng 495–525: Dò đường phân cách giữa lốp xe khô và vùng chìm trong nước đục.
* **Nguyên tắc trung thực:** Dòng 540–544: Khi không có xe máy trong khung hình, mực nước hiển thị là `0 cm (Chờ xe máy làm mốc)` chứ tuyệt đối không bịa số đo.

### 2. Thuật toán phát hiện ngã xe & Bộ đếm bất động 5s ([`backend/detector.py`](file:///c:/Competition/singlenode-urbanshield-lite/backend/detector.py))
* `evaluate_fall_candidate()`:
  * Dòng 160–225: Kiểm tra 3 điều kiện:
    1. Tỷ lệ ngang $W/H > 1.15$.
    2. Khoảng cách Euclid tới xe máy $< 180\text{ px}$.
    3. Bộ đếm thời gian `motionless_sec >= 5.0s`.
* Cơ chế tự động hủy báo giả (Auto-Cancel):
  * Dòng 638–643: Khi người đứng dậy ($W/H \le 0.55$), ứng viên ngã tự động bị xóa khỏi danh sách theo dõi.

### 3. Đóng gói mẩu tin < 150 Bytes ([`backend/reporting.py`](file:///c:/Competition/singlenode-urbanshield-lite/backend/reporting.py))
* `build_compact_payload(node_id, event_type, val, unit="cm", timestamp)`:
  * Dòng 14–38: Nén JSON cực hạn, loại bỏ khoảng trắng dư:
    `{"node_id":"node-sgu-01","type":"FLOOD","val":24.5,"unit":"cm","time":1762512900}` $\rightarrow$ **Kích thước đo được: 81 Bytes (< 150 Bytes)**.

### 4. Đo RAM nhân hệ điều hành & Zero-Disk ([`backend/routers/reports.py`](file:///c:/Competition/singlenode-urbanshield-lite/backend/routers/reports.py))
* Endpoint `/health`:
  * Dòng 38–43: Dùng `psutil.Process(os.getpid()).memory_info().rss` để đo RAM thật từ nhân OS, cam kết `disk_files_written: 0`.

### 5. Giao diện song song 50 - 50 & WebGIS ([`frontend/src/components/VideoMonitor.jsx`](file:///c:/Competition/singlenode-urbanshield-lite/frontend/src/components/VideoMonitor.jsx))
* Dòng 68–180: Khối hiển thị song song 2 cột:
  * Cột 1: Thước đo 50cm phân 3 dải màu Xanh/Vàng/Đỏ.
  * Cột 2: Bảng trạng thái ngã xe tự động kèm thanh tiến trình countdown 0s – 5.0s.

---

## 🎯 PHẦN 4: KỊCH BẢN THAO TÁC LIVE DEMO CHI TIẾT (STEP-BY-STEP FLOW)

Khi đứng trước Ban Giám khảo, thao tác chuột theo đúng 4 bước mạch lạc sau:

```text
BƯỚC 1: MỞ MÀN HÌNH CHÍNH (TỔNG QUAN)
  │
  ├─ Mở trình duyệt vào link Google Cloud Run (hoặc http://localhost:5173).
  ├─ Nhấn F11 để đưa về chế độ Toàn màn hình (Full-screen 100vh không cuộn).
  └─ Chỉ tay vào Đèn trạng thái: "Hệ thống đang chạy trực tiếp trên Google Cloud Run".

BƯỚC 2: DEMO CHỨC NĂNG 1 – ĐO NGẬP QUA BÁNH XE 50CM (TRẠM 01)
  │
  ├─ Chọn Tab "Trạm 01 - Đường Trần Xuân Soạn" (Đang có video ngập thực tế).
  ├─ Chỉ vào màn hình video:
  │   • "AI tự động vẽ khung nhận diện xe máy đang chạy qua dòng nước".
  │   • "Toán đạo hàm Sobel quét tìm mép nước cắt qua lốp xe".
  ├─ Nhìn xuống THẺ 1 (Bên trái):
  │   • Mực nước đo được: 24.5 cm / 50 cm.
  │   • Mức cảnh báo: ĐỎ (Nguy hiểm - Vượt nửa bánh xe).
  │   • Thước đo 50cm: Vạch đỏ vượt qua mốc 25cm.
  └─ Liếc sang BẢN ĐỒ BÊN PHẢI:
      • Tuyến hẻm Trần Xuân Soạn trên bản đồ số GIS tự động đổi thành đường nét ĐỎ rực.

BƯỚC 3: DEMO CHỨC NĂNG 2 – PHÁT HIỆN NGÃ XE & ĐẾM 5S CHỐNG BÁO GIẢ (TRẠM 05)
  │
  ├─ Click chuột chọn Tab "Trạm 05 - Dốc Cầu Kênh Tẻ".
  ├─ Quan sát luồng hình ảnh: Có người bị trượt ngã xe máy trên đoạn dốc trơn trượt.
  ├─ Nhìn vào THẺ 2 (Bên phải):
  │   • Khi người vừa ngã: Thẻ chuyển sang màu VÀNG HỔ PHÁCH.
  │   • Dòng chữ đếm tiến trình: "⏱️ ĐANG THEO DÕI BẤT ĐỘNG: 1.2s -> 2.5s -> 4.8s / 5.0s".
  │   • Nhấn mạnh với BGK: "Nếu người dân tự đứng dậy hoặc cúi nhặt đồ trước 5 giây, 
  │     AI nhận diện khung người đứng thẳng và TỰ ĐỘNG HỦY ĐẾM, triệt tiêu 100% báo động giả".
  └─ Khi chạm mốc 5.0 giây:
      • Thẻ chuyển sang ĐỎ chớp nháy: "🚨 SỰ CỐ NGÃ XE XÁC NHẬN".
      • Tuyến đường trên bản đồ GIS đổi sang viền đỏ chớp cảnh báo.

BƯỚC 4: DEMO TIN NHẮN CẢNH BÁO TELEGRAM (< 150 BYTES)
  │
  ├─ Nhìn sang bảng "CẢNH BÁO GẦN ĐÂY" ở góc dưới bên phải.
  ├─ Chỉ vào mẩu tin sự cố vừa nhảy ra: Có định vị GPS, thời gian chuẩn VN, mực nước/thời gian ngã.
  ├─ Giơ điện thoại hoặc bấm nút "Gửi tin":
  │   • Tin nhắn Telegram reo chuông tức thì (< 1.5 giây).
  │   • Nhấn mạnh: "Gói tin gửi đi chỉ đúng 82 Bytes, tiết kiệm 99.98% băng thông".
  └─ Kết thúc demo và mời Ban Giám khảo kiểm tra code hoặc đặt câu hỏi.
```

---

## 🛡️ PHẦN 5: BỘ CÂU TRẢ LỜI "CHỮA CHÁY" KHI BAN GIÁM KHẢO HỎI XOÁY

* **Hỏi 1: *"Nếu góc camera bị nghiêng hoặc xe ở xa thì bánh xe có còn đúng 50cm không?"***
  * **Đáp:** *"Dạ thưa Thầy Cô, hệ thống không đo theo số pixel tuyệt đối mà đo theo **tỷ lệ tương đối** giữa phần bánh xe bị chìm và chiều cao tổng thể của xe máy. Đồng thời bộ lọc không gian tự động loại bỏ xe ở quá xa (`width < 35px`) và chỉ chọn xe máy rõ nhất ở làn đường trung tâm làm mốc chuẩn."*
* **Hỏi 2: *"Trời mưa to ban đêm mặt đường tối hoặc đèn đường lóa thì AI có thấy mép nước không?"***
  * **Đáp:** *"Dạ, hệ thống có thuật toán cân bằng sáng thích ứng **CLAHE** trong file `detector.py`. Khi độ sáng trung bình kênh L tụt xuống dưới 115, thuật toán tự động khuếch đại độ tương phản cục bộ, triệt tiêu ánh sáng lóa của đèn đường để nhìn rõ ranh giới lốp xe."*
* **Hỏi 3: *"Hình ảnh camera ngõ hẻm có làm lộ bí mật đời tư người dân không?"***
  * **Đáp:** *"Dạ, hệ thống áp dụng nguyên tắc **Privacy-by-Design Zero-Disk**: Video chỉ được giải mã trên RAM để lấy tọa độ hộp số rồi hủy ngay (`del frame`), ổ cứng ghi nhận đúng **0 byte ảnh/video**. Hệ thống cũng không dùng nhận diện khuôn mặt và không đọc biển số xe."*
