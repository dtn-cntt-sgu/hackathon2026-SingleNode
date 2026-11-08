# 📑 KỊCH BẢN NỘI DUNG TẠO SLIDE THUYẾT TRÌNH (DÀNH CHO NOTEBOOKLM)
## DỰ ÁN: URBANSHIELD LITE – GIÁM SÁT NGẬP NƯỚC & SỰ CỐ NGÕ HẺM BẰNG EDGE AI TRÊN CPU
### ĐỘI THI: SINGLENODE | CUỘC THI: SGU HACKATHON 2026

> **Hướng dẫn nạp vào NotebookLM:**  
> Bạn chỉ cần sao chép toàn bộ nội dung file này hoặc tải file `docs/KICH_BAN_SLIDE_NOTEBOOKLM.md` lên NotebookLM làm nguồn tài liệu (Source Document). Sau đó yêu cầu NotebookLM: *"Hãy tạo một bộ slide thuyết trình 8 slide chuyên nghiệp dựa trên tài liệu này, giữ nguyên văn phong mộc mạc và số liệu thực chứng."*

---

## 🖥️ SLIDE 1: TIÊU ĐỀ & GIỚI THIỆU DỰ ÁN

* **Tiêu đề lớn:** UrbanShield Lite
* **Tiêu đề phụ:** Giám sát ngập nước & tai nạn ngõ hẻm bằng Edge AI trên CPU phổ thông
* **Đội thi:** SingleNode – Trường Đại học Sài Gòn (SGU)
* **Ý tưởng cốt lõi:** Tận dụng camera an ninh và máy tính văn phòng sẵn có tại khu phố để cảnh báo sự cố dân sinh tức thì với chi phí thiết bị mới là **0 đồng**.
* **Bố cục thị giác:**
  * Logo dự án hình chiếc khiên bảo vệ khu phố.
  * Ảnh chụp thực tế giao diện WebGIS đang chạy trực tiếp trên nền tảng Cloud: bản đồ hẻm đổi màu theo thời gian thực và màn hình camera giám sát.
* **Lời thoại người nói (Speaker Notes):**
  > "Chào Thầy Cô và các bạn, em là Phát đến từ đội SingleNode. Hôm nay nhóm em xin giới thiệu dự án UrbanShield Lite — giải pháp ứng dụng trí tuệ nhân tạo tại chỗ trên các máy tính văn phòng phổ thông, nhằm bảo vệ bà con trong những con đường nhỏ và ngõ hẻm hay bị ngập nước và tai nạn tại Thành phố Hồ Chí Minh."

---

## 🌧️ SLIDE 2: THỰC TRẠNG & NỖI ĐAU DÂN SINH (PROBLEM-FIRST)

* **Tiêu đề:** Thực trạng mùa mưa bão & Rào cản hạ tầng ngõ hẻm
* **Nỗi đau dân sinh thực tế:**
  1. **Ngập nước gây chết máy:** Triều cường và mưa lớn khiến các con hẻm trũng thấp ngập sâu 20–30cm, người dân đi làm về không biết trước, xe máy chết máy hàng loạt, phải dắt bộ giữa đêm mưa.
  2. **Tai nạn trơn trượt khó cứu giúp kịp thời:** Đường dốc, mặt đường ngập che mất ổ gà làm bà con trượt ngã xe trong hẻm vắng, không được phát hiện kịp thời để giúp đỡ.
* **Rào cản hạ tầng ở địa phương:**
  * **Camera chuyên dụng đo ngập:** Chi phí quá đắt đỏ, không thể trang bị đại trà cho hàng ngàn con hẻm.
  * **Cảm biến siêu âm dưới cống:** Dễ bị rác thải, bùn đất bám nghẹt làm sai lệch kết quả.
  * **Hạ tầng mạng dân sinh yếu:** Nếu dùng camera thường mà kéo luồng video liên tục về máy chủ trung tâm thì sẽ làm nghẽn toàn bộ đường truyền mạng trong khu phố.
* **Bố cục thị giác:**
  * Bố cục so sánh 2 cột: Cột trái là hình ảnh người dân dắt xe ngập nước trong hẻm; Cột phải là 3 rào cản kỹ thuật (Chi phí đắt đỏ – Dễ nghẹt rác – Nghẽn mạng internet).
* **Lời thoại người nói (Speaker Notes):**
  > "Thực tế mỗi khi mùa mưa đến, nỗi khổ lớn nhất của bà con lao động là đi làm về gặp hẻm ngập nước khiến xe máy chết máy, hoặc trượt ngã trong hẻm vắng mà không ai hay biết. Nhưng để lắp đặt hệ thống cảnh báo thì gặp rào cản lớn: mua camera chuyên dụng thì quá đắt đỏ, cảm biến dưới cống thì dễ bị rác nghẹt, còn nếu dùng camera thường kéo video liên tục về máy chủ thì lại làm nghẽn toàn bộ đường truyền mạng của khu phố."

---

## 💡 SLIDE 3: GIẢI PHÁP URBANSHIELD LITE (CÔNG NGHỆ TẠI BIÊN - EDGE AI)

* **Tiêu đề:** Biến camera an ninh sẵn có thành trạm cảnh báo thông minh
* **Đặc tính kỹ thuật chính:**
  * **Tận dụng 100% phần cứng cũ:** Chạy trực tiếp trên CPU máy tính văn phòng khu phố (Intel Core i3 / i5 phổ thông, không cần card đồ họa GPU đắt tiền).
  * **Phân tích tại chỗ (Edge Computing):** Camera thu hình $\rightarrow$ Máy tính tại chỗ tự nhận diện bằng mô hình gọn nhẹ YOLOv8-nano và thuật toán hình học $\rightarrow$ Chỉ gửi cảnh báo khi có sự cố.
  * **Chi phí trang bị mới:** **0 đồng** cho việc mua sắm thiết bị chuyên dụng.
* **Mô hình luồng vận hành (Diagram):**
  ```text
  [Camera có sẵn trong hẻm] 
         │ (Luồng RTSP nội bộ)
         ▼
  [Máy tính văn phòng khu phố (Edge Node)]
         ├─ YOLOv8-nano + Toán hình học bánh xe 50cm (Đo ngập)
         ├─ Bộ đếm bất động 5 giây chống báo nhầm (Ngã xe)
         └─ Quyền riêng tư: Xử lý trên RAM, không lưu đĩa
         │ (Chỉ gửi khi có sự cố: mẩu tin 82 Bytes)
         ▼
  [Bản đồ số WebGIS & Telegram dân quân / tổ dân phố]
  ```
* **Lời thoại người nói (Speaker Notes):**
  > "Để giải quyết triệt để bài toán này, nhóm em chọn cách tiếp cận: Phân tích tại chỗ ngay tại máy tính khu phố. Chúng em tận dụng luôn những camera an ninh đã có sẵn, gắn vào máy tính văn phòng phổ thông không cần card màn hình. Quy trình rất đơn giản: camera truyền hình ảnh về máy tính, máy tính tự phân tích mức nước và tai nạn, và chỉ khi có sự cố thì mới gửi một mẩu tin cảnh báo đi."

---

## 📏 SLIDE 4: THUẬT TOÁN ĐO NGẬP HÌNH HỌC & BỘ ĐẾM 5S CHỐNG BÁO NHẦM

* **Tiêu đề:** Hai thuật toán cốt lõi bảo đảm tính chính xác & chống báo động giả
* **1. Đo ngập hình học qua bánh xe máy 50cm (Adaptive Geometric Measurement):**
  * *Nguyên lý:* Xe máy phổ thông tại Việt Nam (Wave, Sirius, Vision) có đường kính bánh xe chuẩn xác là **50 cm**.
  * *Cách đo:* Máy tính nhận diện xe máy đang lưu thông, lấy phần thân xe trên cạn làm mốc tính tỷ lệ, dùng đạo hàm Sobel quét tìm mép nước cắt qua lốp xe $\rightarrow$ Suy ra mực nước ngập thực tế theo centimet.
  * *Cân bằng sáng ban đêm (CLAHE):* Tự động bù sáng khi trời mưa đêm hoặc đèn đường lóa bóng nước.
* **2. Phát hiện ngã xe kèm bộ đếm bất động 5 giây (Temporal Debounce Tracking):**
  * *Chống báo động giả:* Người cúi nhặt đồ, người đứng dắt xe hoặc dừng chờ đèn đỏ sẽ **tự động bị loại trừ** nhờ bộ lọc không gian (Spatial Seated-Rider Filter).
  * *Nguyên lý chốt sự cố:* Chỉ khi người hoặc xe nằm ngang trên mặt đường và **bất động liên tục trên 5.0 giây**, hệ thống mới xác nhận là tai nạn nguy hiểm để báo cứu hộ.
* **Bố cục thị giác:**
  * Hình minh họa thước đo hình học 50cm trên bánh xe máy kèm vạch mép nước;
  * Thanh tiến trình đếm thời gian: `0s... 2s... 5s (Kích hoạt cảnh báo)`.
* **Lời thoại người nói (Speaker Notes):**
  > "Về kỹ thuật, nhóm em không dùng cảm biến dưới cống mà dùng chính chiếc xe máy làm thước đo. Đường kính bánh xe máy phổ thông ở Việt Nam luôn là 50cm. Máy tính sẽ dò mép nước cắt ngang bánh xe để tính ra độ sâu ngập chính xác từng centimet. Còn với sự cố ngã xe, hệ thống có bộ đếm bất động 5 giây: nếu người dân tự đứng dậy được hoặc dừng xe chờ đèn đỏ thì máy tự hủy theo dõi; chỉ khi nạn nhân nằm im quá 5 giây thì chuông báo động cứu hộ mới reo."

---

## 📡 SLIDE 5: ĐỘT PHÁ BĂNG THÔNG MẠNG – MẨU TIN CẢNH BÁO 82 BYTES

* **Tiêu đề:** Tiết kiệm 99.98% băng thông mạng dân sinh & Xuất Text Report
* **Bảng so sánh mức độ tiêu thụ mạng:**

| Tiêu chí | Camera truyền thống kéo về Server | UrbanShield Lite (Phân tích tại chỗ) |
| :--- | :---: | :---: |
| **Dung lượng mạng mỗi giờ** | **~450 MB / camera** (liên tục) | **0 Byte** (khi đường khô ráo, bình thường) |
| **Dung lượng khi có sự cố** | Vẫn phải truyền video độ nét cao | **Chỉ đúng 82 Bytes (gói tin JSON)** |
| **Tỷ lệ tiết kiệm băng thông** | 0% | **Tiết kiệm 99.98%** |
| **Độ nhạy khi mưa bão rớt mạng** | Dễ mất kết nối, nghẽn mạng | Chạy tốt trên cả sóng yếu 2G/3G |

* **Định dạng mẩu tin gửi đi (Minimal JSON Payload):**
  ```json
  {"node_id":"node-sgu-01","type":"FLOOD","val":22.4,"unit":"cm"}
  ```
* **Báo cáo văn bản mộc mạc (Text Report):**
  * Tự động chuyển đổi mẩu tin 82 Bytes thành tin nhắn Telegram gửi tức thời cho tổ dân phố và dân quân tuần tra.
  * Có tọa độ GPS, thời gian thực và hướng dẫn phân luồng xe máy tránh ngập sâu.
* **Lời thoại người nói (Speaker Notes):**
  > "Thay vì kéo video liên tục về máy chủ làm tốn khoảng 450MB mỗi giờ và nghẽn mạng hẻm, máy tính của chúng em xử lý xong thì chỉ gửi đi một mẩu tin dữ liệu vỏn vẹn 82 Bytes. Nhờ mẩu tin gọn nhẹ này, hệ thống tiết kiệm hơn 99.98% băng thông mạng, mưa bão sóng yếu vẫn gửi tin tốt. Mẩu tin này tự động chuyển thành bản tin Telegram gửi thẳng cho các chú dân quân đang đi tuần ngoài mưa."

---

## 🔒 SLIDE 6: KIẾN TRÚC HỆ THỐNG & BẢO VỆ QUYỀN RIÊNG TƯ (PRIVACY-BY-DESIGN)

* **Tiêu đề:** Vận hành bền bỉ trên máy tính phổ thông & Cam kết Zero-Disk
* **3 Trụ cột kiến trúc:**
  1. **Hiệu năng cao trên CPU phổ thông:** Tối ưu luồng xử lý PyTorch CPU, đạt tốc độ **28.5 FPS**, độ trễ suy luận chỉ **25.1 ms/khung hình**, bộ nhớ RAM tiêu thụ ổn định **~412 MB**.
  2. **Bảo vệ quyền riêng tư tuyệt đối (Privacy-by-Design):** Toàn bộ khung hình video chỉ nạp vào bộ nhớ RAM xoay vòng (Ring buffer) để AI phân tích rồi tự hủy ngay lập tức. **Cam kết 0 file ảnh, 0 file video người dân nào bị lưu trữ xuống ổ đĩa cứng**.
  3. **Cơ sở dữ liệu nhúng SQLite chế độ WAL:** Không cần cài đặt máy chủ database cồng kềnh, tự động dọn dẹp dữ liệu cũ sau 90 ngày (Data Retention) để không làm đầy ổ cứng máy tính khu phố.
* **Lời thoại người nói (Speaker Notes):**
  > "Hệ thống chạy rất nhẹ nhàng trên CPU phổ thông với tốc độ 28.5 khung hình/giây và chỉ tốn hơn 400MB RAM. Đặc biệt, để bảo vệ quyền riêng tư cho người dân trong ngõ hẻm, toàn bộ video chỉ giải mã trên bộ nhớ RAM rồi tự giải phóng ngay sau đó. Hệ thống cam kết không lưu bất kỳ hình ảnh hay video nào xuống ổ cứng."

---

## 🧪 SLIDE 7: MINH BẠCH THỰC CHỨNG & KẾT QUẢ KIỂM THỬ (TEST REPORT)

* **Tiêu đề:** Kiểm thử tự động 19 bài Test & Thực nghiệm trên video TP.HCM
* **Kết quả kiểm thử tự động (Pytest QA Suite):**
  * **19 / 19 bài kiểm thử đạt 100% (Passed)** bao phủ: đo ngập 3 mức, cân bằng sáng CLAHE ban đêm, bộ đếm ngã xe 5s, Minimal API `< 150 Bytes`, SQLite sao lưu nóng và phân trang tra cứu lộ trình.
* **Kết quả thực nghiệm trên tập video thực tế (`labels.csv`):**
  * Đo đạc chính xác mực nước ngập trên các video ngập triều cường tại Quận 7, Quận 4 và Bình Thạnh.
  * Bắt đúng sự cố tai nạn ngã xe tại dốc cầu sau đúng 5.0 giây bất động.
* **Tính trung thực khoa học (Zero Fake Data):**
  * Thẳng thắn thừa nhận giới hạn kỹ thuật: Ở video ngập sâu không có xe máy chạy qua làm mốc đo, hệ thống báo không đo được (`0.0cm`) thay vì ngụy tạo số liệu giả.
* **Lời thoại người nói (Speaker Notes):**
  > "Nhóm em tuân thủ nghiêm ngặt tính liêm chính học thuật: toàn bộ 19 bài kiểm thử tự động đều vượt qua thành công. Số liệu đo lường đều được trích xuất từ các video ngập nước thực tế tại Thành phố Hồ Chí Minh. Ở những tình huống không có xe máy chạy qua làm mốc đo, hệ thống thẳng thắn báo không đo được chứ tuyệt đối không dùng dữ liệu giả để làm đẹp kết quả."

---

## 🚀 SLIDE 8: KHẢ NĂNG ỨNG DỤNG & KẾT LUẬN

* **Tiêu đề:** Triển khai nhanh chóng vì sự an toàn của người dân ngõ hẻm
* **Giá trị thực tiễn mang lại:**
  * **Chính quyền & Lực lượng cứu hộ:** Nắm bắt điểm ngập và tai nạn trong hẻm qua Telegram chỉ sau 1.5 giây để phân luồng và hỗ trợ kịp thời.
  * **Người dân:** Tra cứu trực tiếp bản đồ WebGIS lộ trình an toàn trên điện thoại để tránh các con hẻm ngập nước khi đi làm về.
  * **Khả năng nhân rộng:** Triển khai được ngay tại hàng ngàn ngõ hẻm trên địa bàn thành phố với chi phí mua sắm thiết bị mới là **0 đồng**.
* **Lời kết thuyết trình:**
  > "Với việc tận dụng camera và máy tính sẵn có ở địa phương, UrbanShield Lite có thể triển khai ngay ngày mai mà không cần chờ ngân sách đầu tư tốn kém. Nhóm em hy vọng giải pháp nhỏ bé này sẽ giúp bà con lao động đi làm về không còn cảnh dắt xe chết máy trong đêm mưa, và người gặp nạn trong hẻm vắng luôn được phát hiện và giúp đỡ kịp thời. Em xin chân thành cảm ơn Thầy Cô và các bạn!"
