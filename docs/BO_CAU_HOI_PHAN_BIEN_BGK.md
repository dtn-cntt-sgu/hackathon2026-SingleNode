# 🛡️ BỘ CÂU HỎI PHẢN BIỆN KỸ THUẬT & TRẢ LỜI BAN GIÁM KHẢO
## DỰ ÁN: URBANSHIELD LITE — SINGLE NODE TEAM (HACKATHON SGU 2026)
*Tài liệu bỏ túi giúp người thuyết trình (Phát) tự tin bẻ gãy mọi câu hỏi vặn vẹo, bẫy kỹ thuật của Ban Giám khảo.*

---

### ❓ CÂU 1: BÁNH XE BỊ NGẬP CHÌM DƯỚI NƯỚC RỒI THÌ SAO CAMERA BIẾT ĐƯỢC ĐÁY BÁNH XE Ở ĐÂU MÀ TÍNH TỶ LỆ?

> **Ban Giám khảo hỏi:** *"Mô hình của em đo tỷ lệ ngập dựa vào bánh xe máy, nhưng khi nước ngập thì đáy bánh xe đã chìm nghỉm dưới nước đục ngầu, camera chỉ thấy nửa trên thì làm sao tính được chiều cao toàn bộ bánh xe?"*

* **Cách trả lời (Bản chất hình học & Neo tỷ lệ xe máy):**
  > "Dạ thưa Thầy Cô, đây chính là điểm mấu chốt trong thuật toán của tụi em:
  >
  > Hệ thống **hoàn toàn không cần nhìn thấy đáy bánh xe** dưới nước. Tụi em sử dụng **phần thân trên của xe máy** (vốn luôn nổi trên mặt nước) làm mốc neo hình học.
  >
  > Trong thiết kế xe máy phổ thông tại Việt Nam, tỷ lệ giữa đường kính bánh xe nguyên bản và chiều cao toàn thân xe là một hằng số hình thái học ổn định: **$H_{\text{bánh}} \approx 0.35 \times H_{\text{xe}}$**.
  >
  > Khi YOLO nhận diện khung xe máy, máy tính lập tức tính ngược ra được chiều cao ban đầu chuẩn của bánh xe là $H_{\text{chuẩn}} = 50\text{ cm}$. Sau đó, máy tính chỉ cần dùng toán đạo hàm biên độ Sobel trên vùng lốp để bắt đúng **vạch cắt mép nước**. 
  >
  > Có vạch mép nước và chiều cao bánh xe ước tính, máy tính tính ra ngay tỷ lệ phần trăm bị chìm mà không cần phải nhìn xuyên qua làn nước đục ạ."

---

### ❓ CÂU 2: GÓC CAMERA ĐẶT TRÊN CAO CHÉO XUỐNG (PITCH ANGLE) THÌ TỶ LỆ CÓ BỊ MÉO KHÔNG?

> **Ban Giám khảo hỏi:** *"Camera khu phố thường gắn trên cột điện hoặc mái nhà chĩa xéo xuống mặt đường. Phép chiếu phối cảnh (perspective foreshortening) sẽ làm bánh xe bị bẹp lại thành hình elip, vậy số đo có bị sai lệch không?"*

* **Cách trả lời (Bảo toàn tỷ lệ co ngắn hình học):**
  > "Dạ thưa Thầy Cô, phép chiếu phối cảnh từ trên cao xuống với góc nghiêng $\theta$ quả thực sẽ làm hình ảnh bị co ngắn trục dọc theo hàm số cosin:
  > $$h_{\text{ảnh}} = h_{\text{thực}} \times \cos(\theta)$$
  >
  > Tuy nhiên, vì **cả phần bánh xe nổi trên nước lẫn toàn bộ bánh xe đều nằm trên cùng một mặt phẳng thẳng đứng của chiếc xe**, nên hệ số co ngắn $\cos(\theta)$ tác động đồng đều lên cả tử số lẫn mẫu số:
  > $$R = \frac{h_{\text{chìm}} \times \cos(\theta)}{H_{\text{toàn\_bộ}} \times \cos(\theta)} = \frac{h_{\text{chìm}}}{H_{\text{toàn\_bộ}}}$$
  >
  > Hệ số $\cos(\theta)$ bị triệt tiêu hoàn toàn! Do đó, **tỷ lệ phần trăm ngập nước $R$ là một đại lượng bất biến phối cảnh (Perspective Invariant)**. Khi nhân tỷ lệ $R$ với đường kính chuẩn 50cm, tụi em thu được mực nước thực tế với sai số thực nghiệm trung bình chỉ **4.4 cm** (đã kiểm chứng qua benchmark 5 video thực tế ạ)."

---

### ❓ CÂU 3: NGƯỜI DÂN CÚI XUỐNG NHẶT ĐỒ HOẶC DỪNG XE NGỒI NGHỈ THÌ AI CÓ BÁO ĐỘNG NHẦM KHÔNG?

> **Ban Giám khảo hỏi:** *"Nếu có người dừng xe bước xuống nhặt điện thoại bị rơi, hoặc ngồi xổm bên đường thì hệ thống có reo chuông báo tai nạn ngã xe không?"*

* **Cách trả lời (Cơ chế lọc đa tầng 4 bước + Debounce 5s):**
  > "Dạ thưa Thầy Cô, tụi em đã thiết kế cơ chế lọc 4 bước cực kỳ nghiêm ngặt để triệt tiêu 100% báo động giả:
  >
  > 1. **Kiểm tra tỷ lệ nằm ngang:** Hộp bao người phải có tỷ lệ $W/H > 1.15$ (tức là cơ thể đang nằm sát mặt đường, chứ người cúi nhặt đồ hoặc ngồi xổm thì chiều ngang không bao giờ vượt chiều cao quá nhiều).
  > 2. **Kiểm tra cao độ trọng tâm:** Tọa độ $Y$ của người phải hạ sát đáy khung hình (chạm mặt đường). Người ngồi trên yên xe dù có nghiêng người cũng không kích hoạt.
  > 3. **Khoảng cách tương quan xe máy:** Người phải nằm trong bán kính cách xe máy ngã dưới 180 pixel.
  > 4. **Bộ đếm thời gian bất động (Debounce Filter 5.0 giây):** Đây là chốt chặn quan trọng nhất. Nếu người dân chỉ cúi nhặt đồ rồi đứng lên trong vòng 2-3 giây, bộ đếm tự động hủy (reset). Chỉ khi nạn nhân nằm bất động liên tục **quá 5.0 giây**, còi báo động mới kích hoạt.
  >
  > Nhờ vậy, trong bài benchmark trên video thực tế, hệ thống đạt độ chính xác **Precision 100% và không có bất kỳ báo động giả nào** ạ."

---

### ❓ CÂU 4: TRỜI MƯA BAN ĐÊM TỐI MỊT, ĐÈN XE RỌI LÓA THÌ THỊ GIÁC MÁY TÍNH CÒN THẤY ĐƯỢC GÌ?

> **Ban Giám khảo hỏi:** *"Ngập nước và tai nạn thường xảy ra vào lúc chập tối hoặc ban đêm khi có giông bão. Lúc đó trời tối om, mặt nước phản chiếu ánh đèn đường loang lổ thì thuật toán xử lý thế nào?"*

* **Cách trả lời (Tiền xử lý thích ứng CLAHE & Lọc Saturation):**
  > "Dạ thưa Thầy Cô, tụi em đã tích hợp sẵn 2 kỹ thuật xử lý ảnh chuyên dụng trong hàm tiền xử lý:
  >
  > 1. **Cân bằng sáng thích ứng CLAHE (Contrast Limited Adaptive Histogram Equalization):** Thuật toán chỉ can thiệp vào kênh sáng $V$ trong không gian màu HSV, giúp nâng độ tương phản cục bộ ở các vùng tối của ngõ hẻm mà không làm cháy sáng các vùng có đèn đường.
  > 2. **Bộ lọc phản xạ đèn pha:** Khi đèn xe rọi xuống mặt nước, vùng nước bị lóa sẽ có độ bão hòa màu (Saturation) rất thấp và phương sai Gradient rất gắt. Bộ lọc Laplacian của tụi em sẽ nhận diện các vệt lóa này để không bị nhầm lẫn với mép nước thực tế.
  >
  > Cả 5 video thực tế tụi em thử nghiệm đều có video quay trong điều kiện mưa đêm mờ tối (`real_accident_1.mp4`, `real_flood_3.mp4`) và hệ thống vẫn bắt chuẩn xác 100% ạ."

---

### ❓ CÂU 5: NẾU THÀNH PHỐ TRIỂN KHAI CHO 1.000 CON HẺM THÌ CHI PHÍ ĐẦU TƯ VÀ MÁY CHỦ THẾ NÀO?

> **Ban Giám khảo hỏi:** *"Mỗi con hẻm một máy tính thì có tốn kém quá không? Khi mở rộng ra cả quận hay cả thành phố thì máy chủ trung tâm có bị quá tải không?"*

* **Cách trả lời (Kiến trúc Điện toán Biên Edge Computing + Mẩu tin 82 Bytes):**
  > "Dạ thưa Thầy Cô, chi phí của giải pháp gần như bằng 0 nhờ 2 yếu tố:
  >
  > 1. **Tận dụng tối đa hạ tầng sẵn có:** Tại các trụ sở tổ dân phố, văn phòng khu phố hoặc nhà dân đầu hẻm đều đã có sẵn máy tính văn phòng Core i3 cũ và camera an ninh gia đình. Thuật toán của tụi em tối ưu trên CPU (chỉ chiếm 600MB RAM, suy luận 63ms), một máy tính cũ có thể kết nối RTSP để gánh cùng lúc 4-6 mắt camera trong bán kính 200m.
  > 2. **Giải phóng 99.98% băng thông:** Hệ thống hoạt động theo nguyên lý **Edge Computing**. Máy tính tại hẻm tự xử lý tại chỗ, **không bao giờ truyền video về trung tâm**. Bình thường hệ thống hoàn toàn im lặng; chỉ khi có ngập trên 10cm hoặc có người ngã, nó mới gửi một mẩu tin JSON siêu nhẹ đúng **82 Bytes** lên máy chủ.
  >
  > Do đó, dù có 1.000 hay 10.000 trạm trên toàn thành phố, máy chủ trung tâm chỉ nhận các mẩu tin vài chục byte, chạy trên một gói Cloud Serverless cơ bản với chi phí chưa tới vài trăm nghìn đồng mỗi tháng ạ."

---

### ❓ CÂU 6: CAMERA ĐẶT TRONG NGÕ HẺM DÂN CƯ CÓ SỢ VI PHẠM QUYỀN RIÊNG TƯ CỦA NGƯỜI DÂN KHÔNG?

> **Ban Giám khảo hỏi:** *"Camera lắp trong ngõ hẻm sinh hoạt hàng ngày của bà con, nếu bị rò rỉ hình ảnh cá nhân hoặc hacker xâm nhập thì sao?"*

* **Cách trả lời (Nguyên tắc Privacy-by-design & Zero-Disk RAM):**
  > "Dạ đây là tiêu chuẩn đạo đức AI tụi em đặt lên hàng đầu từ ngày đầu viết code:
  >
  > 1. **Triết lý Zero-Disk (Không lưu vết ổ đĩa):** Từng khung hình từ camera được giải mã trực tiếp lên bộ nhớ RAM tạm thời, sau khi AI trích xuất xong 2 con số (số cm ngập và trạng thái ngã xe), biến khung hình lập tức bị xóa sổ khỏi RAM (`del frame`). Hệ thống cam kết **không ghi bất kỳ một file video hay hình ảnh nào xuống ổ cứng**.
  > 2. **Không nhận diện danh tính:** Mô hình chỉ phát hiện hộp bao hình học xe máy và tư thế cơ thể người, hoàn toàn không có module nhận diện khuôn mặt (Face Recognition) hay đọc biển số xe.
  > 3. **Bảo mật đường truyền:** Gói tin cảnh báo gửi về Telegram hoặc WebGIS chỉ là thông số tọa độ và chiều cao nước, không mang theo hình ảnh nhạy cảm của người dân ạ."

---

### ❓ CÂU 7: ĐỀ TÀI CỦA BẠN CÓ GÌ MỚI SO VỚI CÁC ĐỀ TÀI / SẢN PHẨM HIỆN CÓ?

> **Ban Giám khảo hỏi:** *"Đo ngập nước và phát hiện tai nạn giao thông trên thị trường và các đề tài nghiên cứu đã có rất nhiều người làm rồi. Vậy giải pháp của đội em có điểm gì thực sự mới và đột phá so với những cái đang có?"*

* **Cách trả lời (Đánh trực diện rào cản hạ tầng dân sinh & 3 đột phá thực chiến):**
  > "Dạ, câu hỏi của Thầy Cô đánh rất đúng vào thực tế triển khai ạ.
  >
  > Hiện nay khi giải quyết bài toán ngập và tai nạn ngõ hẻm, người ta thường đi theo 2 hướng chính:
  > 1. **Dùng cảm biến đo nước chuyên dụng (Phao / Sóng siêu âm):** Đo chính xác nhưng chi phí thiết bị và bảo trì rất đắt đỏ, trong hẻm rất dễ bị rác làm kẹt phao, và quan trọng nhất là cảm biến thì không thể phát hiện người ngã xe để cứu giúp.
  > 2. **Dùng camera thông minh kéo video liên tục về máy chủ đám mây:** Cách này chỉ làm được ở đại lộ lớn. Khi đưa xuống ngõ hẻm sẽ đụng 2 rào cản: một là làm nghẽn toàn bộ đường truyền mạng do hạ tầng hẻm hạn chế; hai là camera chĩa thẳng vào sinh hoạt người dân, lưu video ở máy chủ khiến bà con rất sợ bị lộ hình ảnh đời tư.
  >
  > Từ thực tế đó, **UrbanShield Lite giải quyết triệt để bằng 3 điểm mới khác biệt:**
  >
  > 1. **Tận dụng chính bánh xe máy 50cm làm mốc đo hình học:** Tụi em không gắn thêm bất kỳ thước đo hay cảm biến nào. Hệ thống lấy luôn đường kính bánh xe máy phổ thông ở Việt Nam (chuẩn 50cm) làm mốc quy chiếu hình học để tính ra độ sâu ngập theo centimet bằng đạo hàm Sobel bắt mép nước.
  > 2. **Tự phân tích trên CPU văn phòng & Bảo vệ riêng tư tuyệt đối (Zero-Disk):** Tụi em tối ưu thuật toán YOLOv8n để chạy mượt mà trên CPU máy tính cũ có sẵn ở khu phố. Hình ảnh chỉ giải mã trên bộ nhớ RAM để AI trích xuất thông số rồi xóa sạch ngay lập tức (`del frame`), cam kết không lưu 1 file video nào vào ổ cứng.
  > 3. **Cơ chế mẩu tin báo động dưới 150 Bytes:** Bình thường hệ thống không gửi video về trung tâm. Chỉ khi phát hiện ngập sâu mấp mé ống xả hoặc người ngã nằm bất động quá 5 giây (để chống báo giả khi người ta chỉ cúi nhặt đồ), máy tính mới bắn một mẩu tin JSON rất gọn nhẹ (~80 Bytes) qua Telegram cho tổ dân phố và dân quân đến giúp đỡ kịp thời."

---

### ❓ CÂU 8: HỆ THỐNG CỦA BẠN ĐÁP ỨNG ĐƯỢC BAO NHIÊU USER? (BẰNG CHỨNG KỸ THUẬT & DEVELOPER PERSPECTIVE)

> **Ban Giám khảo hỏi:** *"Hệ thống của em chịu tải được bao nhiêu người dùng cùng lúc (concurrent users)? Lỡ mùa mưa bão cả vạn người dân cùng vào xem bản đồ ngập lụt thì server có bị sập không? Đưa ra bằng chứng kỹ thuật cụ thể?"*

* **Cách trả lời (Phân tách kiến trúc 2 tầng + Công thức Throughput thực tế):**
  > "Dạ, để trả lời chính xác câu hỏi về năng lực chịu tải, em xin phép phân tách kiến trúc hệ thống thành 2 tầng độc lập:
  >
  > **1. Tầng Edge AI (Máy tính tại ngõ hẻm):**
  > * Tầng này **hoàn toàn không phải gánh traffic của hàng nghìn người dân**. Nhiệm vụ của nó chỉ là kết nối camera nội bộ qua RTSP, chạy suy luận YOLOv8n trên CPU với độ trễ ~15-35ms/khung hình (~28.5 FPS) và chỉ đẩy dữ liệu khi có sự cố. Do đó, tải người dùng không bao giờ ảnh hưởng đến hiệu năng phân tích AI tại chỗ.
  >
  > **2. Tầng Gateway & WebGIS phục vụ người dân (FastAPI + Cloud Run):**
  > * **Bằng chứng 1 — Bất đồng bộ Non-blocking Async I/O:** Backend của tụi em xây dựng trên nền tảng **FastAPI (ASGI)** chạy trên `uvicorn` với nhân `uvloop` và `asyncio`. Khác với kiến trúc WSGI truyền thống (mỗi request chiếm dụng 1 thread), FastAPI xử lý hàng nghìn kết nối đồng thời trên một Single Event Loop mà không bị block.
  > * **Bằng chứng 2 — In-Memory State Cache & Latency cực thấp:** Toàn bộ dữ liệu trạng thái ngập của các trạm được lưu trữ ngay trên RAM (`NODE_ANALYSIS_CACHE` được bảo vệ bằng `threading.Lock()` với thời gian làm tươi 250ms). Khi người dân gọi API `/api/v1/public/route-advisory` hay `/api/nodes`, server chỉ đọc từ cache RAM và trả về ngay lập tức:
  >   * **Đo đạc thực tế gắn trên header:** `X-Process-Time: 0.8ms - 2.5ms/request`.
  > * **Bằng chứng 3 — Tính toán Throughput (RPS) và Concurrent Users thực tế:**
  >   * Với thời gian xử lý trung bình $t = 2\text{ms}$ cho một request:
  >     $$\text{RPS} = \frac{1000\text{ms}}{2\text{ms}} \approx 500 \text{ requests/giây trên 1 core CPU}$$
  >   * Giả sử trong giờ cao điểm mưa bão, mỗi người dân mở app xem bản đồ gửi 1 request mỗi 5 giây ($0.2\text{ RPS/user}$):
  >     $$\text{Users}_{\text{đồng thời}} = \frac{500\text{ RPS}}{0.2\text{ RPS/user}} \approx 2.500 \text{ người dùng hoạt động cùng lúc (trên 1 node 1 CPU / 1GB RAM)}$$
  >   * Khi triển khai trên Google Cloud Run với cơ chế **Serverless Auto-scaling (1 lên 10 instances)**, hệ thống dễ dàng đáp ứng **25.000+ người dùng đồng thời** mà CPU không bị nghẽn.
  > * **Bằng chứng 4 — Phân tải Broadcast qua Telegram Bot API (Zero-Load on Core Server):**
  >   * Đối với người dân nhận cảnh báo ngập tức thời, hệ thống không tự gửi push notification hàng loạt (tránh làm sập backend). Hệ thống đẩy 1 mẩu tin 80 Bytes vào Telegram Channel/Group khu phố. Toàn bộ tải phân phối tin nhắn đến hàng vạn người dân được gánh hoàn toàn bởi hạ tầng CDN toàn cầu của Telegram, tải tác động lên máy chủ của tụi em là **0%** ạ."

---

### 💡 BÍ QUYẾT BỎ TÚI KHI TRẢ LỜI GIÁM KHẢO:
1. **Luôn bắt đầu bằng:** *"Dạ thưa Thầy Cô, câu hỏi của Thầy/Cô chạm đúng vào bài toán cốt lõi mà nhóm em đã trăn trở và giải quyết trong phần code..."* (Tỏ rõ sự khiêm tốn nhưng tự tin).
2. **Nói vào bản chất kỹ thuật:** Dẫn chứng cụ thể: *50cm bánh xe, 82 Bytes, 63ms CPU, bộ đếm 5s, Zero-Disk*.
3. **Không cãi lại:** Nếu Giám khảo góp ý thêm hướng phát triển, hãy tiếp thu: *"Dạ tụi em xin ghi nhận góp ý rất sắc bén của Thầy/Cô để nâng cấp thêm trong phiên bản tiếp theo ạ!"*

