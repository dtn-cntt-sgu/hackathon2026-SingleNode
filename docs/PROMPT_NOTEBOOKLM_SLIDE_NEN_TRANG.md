# 🎨 BỘ PROMPT TẠO SLIDE NỀN TRẮNG DÀNH CHO NOTEBOOKLM
## DỰ ÁN: URBANSHIELD LITE – HACKATHON SGU 2026

> **Hướng dẫn sử dụng nhanh:**  
> 1. Mở [NotebookLM](https://notebooklm.google.com/), chọn Notebook chứa tài liệu `docs/KICH_BAN_SLIDE_NOTEBOOKLM.md` (hoặc upload file này lên làm nguồn).  
> 2. Copy toàn bộ nội dung trong khung **"PROMPT MASTER"** bên dưới và dán vào ô chat của NotebookLM.  
> 3. NotebookLM sẽ xuất ra dàn ý slide chi tiết với phong cách tối giản, nền trắng hiện đại, sẵn sàng đưa sang Google Slides, Canva hoặc PowerPoint.

---

### 📋 KHUNG PROMPT MASTER (COPY PHẦN DƯỚI ĐÂY)

```text
Dựa vào tài liệu nguồn UrbanShield Lite đã tải lên, hãy đóng vai trò là một Chuyên gia Thiết kế Slide Thuyết trình Công nghệ (Presentation Designer). Hãy xây dựng nội dung chi tiết cho một bộ slide gồm 8 slide hoàn chỉnh theo đúng phong cách "MINIMALIST WHITE BACKGROUND" (Phong cách tối giản, thanh lịch, nền trắng hiện đại) với các yêu cầu nghiêm ngặt sau:

1. QUY CHUẨN THIẾT KẾ THỊ GIÁC (VISUAL GUIDELINES - NỀN TRẮNG):
- Tone màu chủ đạo: Nền trắng tinh khiết (#FFFFFF) hoặc trắng kem nhạt (#F8FAFC), viền thẻ xám siêu mảnh (#E2E8F0) tạo cảm giác không gian thoáng đãng, chuyên nghiệp.
- Màu chữ: Chữ tiêu đề dùng màu xanh than đậm (Deep Navy #0F172A), chữ nội dung dùng xám đen (Slate #334155), độ tương phản cao, dễ đọc trên máy chiếu hội trường.
- Điểm nhấn màu sắc (Accent Colors): 
  + Màu đỏ cảnh báo (#DC2626) cho mức ngập >20cm và sự cố ngã xe 5 giây.
  + Màu xanh lá an toàn (#16A34A) cho tiết kiệm 99.98% băng thông và 0 đồng chi phí.
  + Màu xanh dương công nghệ (#2563EB) cho các mốc đo hình học bánh xe 50cm.
- Phong cách bố cục: Dạng thẻ thông tin (Card-based layout), chia cột rõ ràng, nhiều khoảng trắng (whitespace), tuyệt đối không dùng nền đen, nền tối hay gradient sặc sỡ.

2. QUY CHUẨN NGÔN TỪ & NỘI DUNG (100% VĂN NÓI MỘC MẠC & KHÔNG HYPE):
- Tuân thủ nguyên tắc Problem-First: Nêu thực trạng nỗi đau ngõ hẻm và rào cản hạ tầng trước khi giới thiệu giải pháp.
- Giữ vững tính trung thực kỹ thuật (Zero Fake Data): Sử dụng chính xác các số liệu đo đạc thực tế từ CPU/RAM (28.5 FPS, 25.1ms latency, 412MB RAM, mẩu tin 82 Bytes, 19/19 Pytest Pass).
- Cấm tiệt từ ngữ khoa trương: Không dùng tiền tố "siêu...", không dùng văn mẫu giật gân báo chí ("thời gian vàng cứu hộ"). Dùng từ mộc mạc đời thường: "gọn nhẹ", "mẩu tin cảnh báo", "máy tính khu phố".

3. YÊU CẦU XUẤT RA CHO TỪNG SLIDE (TỪ SLIDE 1 ĐẾN SLIDE 8):
Với mỗi slide, hãy trình bày đầy đủ 4 phần rõ ràng:
- [Tiêu đề Slide] & [Thông điệp cốt lõi]
- [Bố cục thị giác nền trắng]: Mô tả chi tiết cách sắp xếp các thẻ (cards), biểu đồ, icon hoặc bảng số liệu trên nền trắng.
- [Nội dung hiển thị trên Slide]: Các gạch đầu dòng ngắn gọn, súc tích, làm nổi bật số liệu then chốt.
- [Lời thoại thuyết trình (Speaker Notes)]: Viết sẵn câu văn nói tự nhiên, mộc mạc (xưng "em", gọi "Thầy Cô và các bạn") để người thuyết trình đọc liền mạch trong 20-30 giây mỗi slide.

HÃY BẮT ĐẦU TẠO CHI TIẾT 8 SLIDE NGAY BÂY GIỜ THEO CẤU TRÚC:
- Slide 1: Trang bìa – UrbanShield Lite: Giám sát ngập nước & tai nạn ngõ hẻm bằng Edge AI trên CPU.
- Slide 2: Thực trạng & Rào cản hạ tầng – Nỗi đau dân sinh ngõ hẻm mùa mưa & 3 rào cản (Giá đắt, Nghẹt rác, Nghẽn mạng).
- Slide 3: Giải pháp công nghệ tại biên (Edge AI) – Tận dụng camera an ninh và máy tính văn phòng sẵn có, chi phí 0 đồng.
- Slide 4: Hai thuật toán cốt lõi – Đo ngập hình học qua bánh xe máy 50cm (Sobel + CLAHE) & Bộ đếm bất động 5 giây chống báo nhầm.
- Slide 5: Đột phá băng thông mạng – Mẩu tin 82 Bytes (<150B) thay thế video 450 MB/h (tiết kiệm 99.98% mạng) & Tự động xuất Text Report Telegram.
- Slide 6: Kiến trúc hệ thống & Quyền riêng tư – Hiệu năng CPU 28.5 FPS (25.1ms), Cam kết Zero-Disk (xử lý trên RAM tự hủy, 0 lưu ổ đĩa), SQLite WAL.
- Slide 7: Minh bạch thực chứng & Kiểm thử – 19/19 bài Pytest Pass, kết quả thực nghiệm video TP.HCM, thẳng thắn thừa nhận giới hạn (Zero Fake Data).
- Slide 8: Khả năng ứng dụng & Kết luận – Triển khai tức thì tại hàng ngàn ngõ hẻm với chi phí 0 đồng vì sự an toàn của người dân.
```

---

### 💡 GỢI Ý BỔ SUNG CHO NOTEBOOKLM KHI MUỐN TẠO THÊM TÀI LIỆU:

* **Tạo Audio Podcast 2 người đàm luận (Audio Overview):**  
  > *"Hãy tạo một bản tóm tắt Audio Overview thảo luận giữa 2 chuyên gia về dự án UrbanShield Lite: nhấn mạnh vào tính thực tiễn cứu hộ ngõ hẻm dân sinh, giải pháp đo ngập qua bánh xe 50cm và cách tiết kiệm mạng đột phá chỉ với gói tin 82 Bytes."*

* **Tạo bảng Hỏi - Đáp phản biện cho Ban Giám khảo (Q&A Cheat-sheet):**  
  > *"Dựa vào tài liệu nguồn, hãy liệt kê 5 câu hỏi phản biện hóc búa nhất mà Ban Giám khảo có thể chất vấn nhóm về: tính chính xác khi không có xe máy, góc nghiêng camera, quyền riêng tư người dân, và cách trả lời ngắn gọn, thuyết phục trong 30 giây."*

