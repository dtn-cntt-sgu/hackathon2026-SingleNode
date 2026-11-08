import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Clean White Minimalist Palette
    COLOR_BG = RGBColor(255, 255, 255)
    COLOR_CARD_BG = RGBColor(248, 250, 252)
    COLOR_CARD_BORDER = RGBColor(226, 232, 240)
    COLOR_TITLE = RGBColor(15, 23, 42)      # Deep Navy/Slate
    COLOR_BODY = RGBColor(51, 65, 85)       # Slate text
    COLOR_MUTED = RGBColor(100, 116, 139)   # Subdued gray
    COLOR_BLUE = RGBColor(37, 99, 235)      # Tech Accent
    COLOR_RED = RGBColor(220, 38, 38)       # Danger / Flood alert
    COLOR_GREEN = RGBColor(22, 163, 74)     # Success / 0 VND

    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="URBANSHIELD LITE — SGU HACKATHON 2026"):
        # Category / Kicker
        kicker_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_k = kicker_box.text_frame
        tf_k.word_wrap = True
        p_k = tf_k.paragraphs[0]
        p_k.text = category_text.upper()
        p_k.font.size = Pt(11)
        p_k.font.bold = True
        p_k.font.color.rgb = COLOR_BLUE
        p_k.font.name = "Segoe UI"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.65))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TITLE
        p_t.font.name = "Segoe UI"

    def add_card(slide, left, top, width, height, title, items, title_color=COLOR_TITLE, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        # Card background
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)

        # Content Box
        content_box = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.4))
        tf = content_box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = Pt(17)
        p0.font.bold = True
        p0.font.color.rgb = title_color
        p0.font.name = "Segoe UI"
        p0.space_after = Pt(12)

        for item in items:
            p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_BODY
            p.font.name = "Segoe UI"
            p.space_after = Pt(8)

    # ==========================================
    # SLIDE 1: COVER SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Title box
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "URBANSHIELD LITE"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p.font.name = "Segoe UI"
    p.space_after = Pt(10)

    p2 = tf1.add_paragraph()
    p2.text = "Giám sát ngập nước & sự cố ngõ hẻm bằng Edge AI trên CPU phổ thông"
    p2.font.size = Pt(22)
    p2.font.color.rgb = COLOR_TITLE
    p2.font.name = "Segoe UI"
    p2.space_after = Pt(24)

    p3 = tf1.add_paragraph()
    p3.text = "Đội thi: SingleNode  |  Cuộc thi: SGU Hackathon 2026  |  Đại học Sài Gòn"
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_MUTED
    p3.font.name = "Segoe UI"

    # 3 Highlight stat badges at the bottom
    badges = [
        ("0 ĐỒNG THIẾT BỊ", "Tận dụng camera an ninh & PC văn phòng cũ"),
        ("82 BYTES GÓI TIN", "Tiết kiệm 99.98% băng thông mạng dân sinh"),
        ("100% ZERO-DISK", "Xử lý trực tiếp trên RAM, bảo vệ quyền riêng tư")
    ]
    for i, (b_title, b_desc) in enumerate(badges):
        bx = Inches(1.0 + i * 3.9)
        by = Inches(5.2)
        bw = Inches(3.6)
        bh = Inches(1.4)
        add_card(s1, bx, by, bw, bh, b_title, [b_desc], title_color=COLOR_BLUE)

    s1.notes_slide.notes_text_frame.text = (
        "Chào Thầy Cô và các bạn, em là Phát đến từ đội SingleNode. Hôm nay nhóm em xin giới thiệu "
        "dự án UrbanShield Lite — giải pháp ứng dụng trí tuệ nhân tạo tại chỗ trên các máy tính văn phòng "
        "phổ thông, nhằm bảo vệ bà con trong những con đường nhỏ và ngõ hẻm hay bị ngập nước và tai nạn tại TP.HCM."
    )

    # ==========================================
    # SLIDE 2: THỰC TRẠNG & RÀO CẢN HẠ TẦNG
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Thực trạng mùa mưa bão & Rào cản công nghệ ở ngõ hẻm")

    # Left card: Citizen pain
    add_card(
        s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Nỗi đau dân sinh ngõ hẻm TP.HCM",
        [
            "Xe máy chết máy dắt bộ: Mưa lớn và triều cường khiến ngõ hẻm ngập sâu 20–30cm, người dân không biết trước, hàng loạt xe chết máy giữa đêm mưa.",
            "Tai nạn trơn trượt khó phát hiện: Đoạn đường dốc hoặc ngập nước che lấp ổ gà làm trượt ngã xe trong hẻm vắng, không được cứu giúp kịp thời.",
            "Lực lượng cơ sở mỏng: Tổ dân phố, dân quân khó tuần tra bao quát hàng ngàn ngõ hẻm cùng lúc khi bão đổ bộ."
        ],
        title_color=COLOR_RED
    )

    # Right card: Technical barriers
    add_card(
        s2, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2),
        "3 Rào cản kỹ thuật địa phương",
        [
            "Camera chuyên dụng đo ngập: Giá thành quá đắt đỏ, ngân sách khu phố không thể mua sắm đại trà.",
            "Cảm biến siêu âm dưới cống: Nhanh chóng bị rác thải, bùn đất bám nghẹt, dẫn đến báo số liệu sai.",
            "Hạ tầng mạng dân sinh yếu: Kéo luồng video liên tục về máy chủ trung tâm sẽ làm nghẽn toàn bộ đường truyền internet khu phố."
        ],
        title_color=COLOR_TITLE
    )

    s2.notes_slide.notes_text_frame.text = (
        "Thực tế mỗi khi mùa mưa đến, nỗi khổ lớn nhất của bà con lao động là đi làm về gặp hẻm ngập nước "
        "khiến xe máy chết máy, hoặc trượt ngã trong hẻm vắng mà không ai hay biết. Nhưng để lắp đặt hệ thống cảnh báo "
        "thì gặp rào cản lớn: mua camera chuyên dụng thì quá đắt đỏ, cảm biến dưới cống thì dễ bị rác nghẹt, "
        "còn nếu dùng camera thường kéo video liên tục về máy chủ thì lại làm nghẽn toàn bộ đường truyền mạng của khu phố."
    )

    # ==========================================
    # SLIDE 3: GIẢI PHÁP EDGE AI TẠI CHỖ
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Giải pháp UrbanShield Lite: Phân tích tại chỗ (Edge Computing)")

    s3_steps = [
        ("1. THU NHẬN HÌNH ẢNH", [
            "Tận dụng camera an ninh sẵn có trong hẻm",
            "Truyền luồng video qua mạng nội bộ khu phố",
            "Không tốn chi phí mua camera mới (0 đồng)"
        ]),
        ("2. PHÂN TÍCH TẠI CHỖ (EDGE AI)", [
            "Chạy trên CPU máy tính văn phòng phổ thông",
            "Mô hình YOLOv8-nano gọn nhẹ + Toán hình học",
            "Đo mực nước ngập & phát hiện ngã xe bất động"
        ]),
        ("3. CẢNH BÁO TỨC THÌ", [
            "Chỉ gửi mẩu tin JSON siêu nhẹ 82 Bytes",
            "Tự động xuất Text Report gửi Telegram cứu hộ",
            "Bản đồ số WebGIS đổi màu theo thời gian thực"
        ])
    ]

    for i, (title, bullets) in enumerate(s3_steps):
        add_card(s3, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8), title, bullets, title_color=COLOR_BLUE)

    s3.notes_slide.notes_text_frame.text = (
        "Để giải quyết triệt để bài toán này, nhóm em chọn cách tiếp cận: Phân tích tại chỗ ngay tại máy tính khu phố. "
        "Chúng em tận dụng luôn những camera an ninh đã có sẵn, gắn vào máy tính văn phòng phổ thông không cần card màn hình. "
        "Quy trình rất đơn giản: camera truyền hình ảnh về máy tính, máy tính tự phân tích mức nước và tai nạn, "
        "và chỉ khi có sự cố thì mới gửi một mẩu tin cảnh báo đi."
    )

    # ==========================================
    # SLIDE 4: HAI THUẬT TOÁN CỐT LÕI
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Hai thuật toán cốt lõi bảo đảm tính chính xác & chống báo động giả")

    add_card(
        s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "1. Đo ngập hình học qua bánh xe máy 50cm",
        [
            "Vật chuẩn bất biến: Bánh xe máy phổ thông tại Việt Nam luôn có đường kính chuẩn xác là 50 cm.",
            "Đạo hàm Sobel mép nước: Lấy phần thân xe trên cạn làm mốc, quét tìm đường viền cắt của mặt nước trên lốp xe để tính ra độ sâu ngập.",
            "Thích ứng ban đêm (CLAHE): Tự động cân bằng sáng thích ứng khi trời mưa đêm hoặc ánh đèn hắt bóng nước, giữ độ chính xác cao."
        ],
        title_color=COLOR_BLUE
    )

    add_card(
        s4, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2),
        "2. Bộ đếm bất động 5 giây chống báo nhầm",
        [
            "Lọc người dừng xe: Người ngồi trên xe máy dựng đứng dừng chờ đèn đỏ sẽ tự động bị loại trừ nhờ bộ lọc không gian (Seated-Rider Filter).",
            "Loại bỏ cúi nhặt đồ: Người đi bộ cúi xuống nhặt đồ hoặc dắt xe rồi đứng dậy trước 5 giây sẽ tự hủy bộ đếm.",
            "Chốt cảnh báo nguy hiểm: Chỉ kích hoạt cảnh báo cứu hộ khi nạn nhân hoặc xe nằm bất động liên tục trên 5.0 giây."
        ],
        title_color=COLOR_RED
    )

    s4.notes_slide.notes_text_frame.text = (
        "Về kỹ thuật, nhóm em không dùng cảm biến dưới cống mà dùng chính chiếc xe máy làm thước đo. "
        "Đường kính bánh xe máy phổ thông ở Việt Nam luôn là 50cm. Máy tính sẽ dò mép nước cắt ngang bánh xe "
        "để tính ra độ sâu ngập chính xác từng centimet. Còn với sự cố ngã xe, hệ thống có bộ đếm bất động 5 giây: "
        "nếu người dân tự đứng dậy được hoặc dừng xe chờ đèn đỏ thì máy tự hủy theo dõi; chỉ khi nạn nhân nằm im "
        "quá 5 giây thì chuông báo động cứu hộ mới reo."
    )

    # ==========================================
    # SLIDE 5: ĐỘT PHÁ MẠNG & TEXT REPORT
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Đột phá băng thông mạng: Mẩu tin 82 Bytes (<150B) & Text Report")

    # Left card: Bandwidth comparison
    add_card(
        s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "Tiết kiệm 99.98% băng thông mạng",
        [
            "Camera cũ kéo về server: Tiêu tốn ~450 MB mỗi giờ / camera, gây nghẽn mạng cáp quang dân sinh.",
            "UrbanShield Lite tại chỗ: Bình thường tiêu thụ 0 Byte mạng. Chỉ gửi mẩu tin khi phát hiện sự cố.",
            "Dung lượng mẩu tin: Đúng 82 Bytes (JSON Minimal API), chưa bằng dung lượng một tin nhắn SMS.",
            "Khả năng chống chọi thiên tai: Sóng 2G/3G chập chờn khi giông bão vẫn gửi trót lọt trong tích tắc."
        ],
        title_color=COLOR_GREEN
    )

    # Right card: Text report
    add_card(
        s5, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2),
        "Bản tin Telegram cho lực lượng cứu hộ",
        [
            "Mẫu A - Cảnh báo tức thời: Tự động chuyển mẩu tin 82 Bytes thành tin nhắn text gửi Telegram cho dân quân chỉ sau 1.5 giây.",
            "Thông tin thực chiến: Có vị trí hẻm cụ thể, tọa độ GPS và hướng dẫn phân luồng xe máy tránh ngập sâu.",
            "Mẫu B - Bản tin ca trực: Tổng hợp số vụ ngập nước, đỉnh triều và tai nạn trong ngày cho tổ trưởng dân phố theo dõi."
        ],
        title_color=COLOR_BLUE
    )

    s5.notes_slide.notes_text_frame.text = (
        "Thay vì kéo video liên tục về máy chủ làm tốn khoảng 450MB mỗi giờ và nghẽn mạng hẻm, máy tính của chúng em "
        "xử lý xong thì chỉ gửi đi một mẩu tin dữ liệu vỏn vẹn 82 Bytes. Nhờ mẩu tin gọn nhẹ này, hệ thống tiết kiệm "
        "hơn 99.98% băng thông mạng, mưa bão sóng yếu vẫn gửi tin tốt. Mẩu tin này tự động chuyển thành bản tin "
        "Telegram gửi thẳng cho các chú dân quân đang đi tuần ngoài mưa."
    )

    # ==========================================
    # SLIDE 6: KIẾN TRÚC & QUYỀN RIÊNG TƯ
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Kiến trúc hệ thống bền bỉ & Cam kết quyền riêng tư (Zero-Disk)")

    s6_cards = [
        ("TỐI ƯU HIỆU NĂNG CPU", [
            "Tốc độ xử lý: 28.5 FPS mượt mà",
            "Độ trễ suy luận: 25.1 ms / khung hình",
            "Mức tiêu thụ RAM: ~412 MB ổn định",
            "Không cần card đồ họa GPU đắt đỏ"
        ]),
        ("QUYỀN RIÊNG TƯ (ZERO-DISK)", [
            "Giải mã trực tiếp trên bộ nhớ RAM",
            "Tự hủy khung hình sau khi phân tích",
            "Cam kết 0 file ảnh, 0 file video lưu ổ cứng",
            "Bảo vệ hình ảnh đời tư người dân"
        ]),
        ("CƠ SỞ DỮ LIỆU NHÚNG SQLITE", [
            "Kích hoạt chế độ WAL đọc/ghi song song",
            "Hàng đợi ngoại tuyến khi rớt mạng",
            "Tự động xóa sự cố cũ sau 90 ngày",
            "Chống tràn bộ nhớ ổ đĩa máy tính"
        ])
    ]

    for i, (title, bullets) in enumerate(s6_cards):
        add_card(s6, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8), title, bullets, title_color=COLOR_TITLE)

    s6.notes_slide.notes_text_frame.text = (
        "Hệ thống chạy rất nhẹ nhàng trên CPU phổ thông với tốc độ 28.5 khung hình/giây và chỉ tốn hơn 400MB RAM. "
        "Đặc biệt, để bảo vệ quyền riêng tư cho người dân trong ngõ hẻm, toàn bộ video chỉ giải mã trên bộ nhớ RAM "
        "rồi tự giải phóng ngay sau đó. Hệ thống cam kết không lưu bất kỳ hình ảnh hay video nào xuống ổ cứng."
    )

    # ==========================================
    # SLIDE 7: KIỂM THỬ THỰC CHỨNG & MINH BẠCH
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Kiểm chứng thực nghiệm & Liêm chính học thuật (Test Report)")

    add_card(
        s7, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2),
        "19/19 Bài kiểm thử tự động (Pytest Pass)",
        [
            "Kiểm thử đo ngập: Đo chính xác 3 mức ngập qua bánh xe 50cm và kiểm tra thích ứng ban đêm với CLAHE.",
            "Kiểm thử ngã xe: Lọc bỏ người cúi nhặt đồ và xe dừng đèn đỏ < 5s; kích hoạt đúng khi nằm im >= 5s.",
            "Kiểm thử API & Dữ liệu: Gói tin < 150 Bytes, GeoJSON đổi màu, phân trang SQLite và sao lưu nóng an toàn."
        ],
        title_color=COLOR_GREEN
    )

    add_card(
        s7, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2),
        "Trung thực khoa học (Zero Fake Data)",
        [
            "Dữ liệu thực tế: Đo đạc trên tập video ngập lụt thực tế tại TP.HCM đối chiếu với bảng nhãn labels.csv.",
            "Dám nhận giới hạn: Ở video hẻm ngập sâu không có xe máy chạy qua làm mốc, hệ thống trung thực báo không đo được (0.0cm) thay vì ngụy tạo kết quả.",
            "Khả năng tái lập: Bất kỳ ai cũng có thể chạy lệnh pytest tests/ -v trực tiếp trên terminal để kiểm chứng."
        ],
        title_color=COLOR_TITLE
    )

    s7.notes_slide.notes_text_frame.text = (
        "Nhóm em tuân thủ nghiêm ngặt tính liêm chính học thuật: toàn bộ 19 bài kiểm thử tự động đều vượt qua "
        "thành công. Số liệu đo lường đều được trích xuất từ các video ngập nước thực tế tại TP.HCM. Ở những tình huống "
        "không có xe máy chạy qua làm mốc đo, hệ thống thẳng thắn báo không đo được chứ tuyệt đối không dùng dữ liệu giả để làm đẹp kết quả."
    )

    # ==========================================
    # SLIDE 8: KHẢ NĂNG ỨNG DỤNG & KẾT LUẬN
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Khả năng ứng dụng thực tế & Triển khai nhanh chóng")

    s8_cards = [
        ("CHO LỰC LƯỢNG CỨU HỘ", [
            "Nhận tin Telegram sau 1.5 giây",
            "Nắm bắt chính xác vị trí ngập và tai nạn",
            "Phân luồng xe máy kịp thời",
            "Cứu giúp người gặp nạn trong đêm mưa"
        ]),
        ("CHO BÀ CON LAO ĐỘNG", [
            "Xem trực tiếp bản đồ WebGIS trên điện thoại",
            "Biết trước các con hẻm ngập sâu để tránh",
            "Giảm thiểu tình trạng xe chết máy dắt bộ",
            "An tâm khi đi làm về lúc triều cường"
        ]),
        ("CHO CHÍNH QUYỀN ĐỊA PHƯƠNG", [
            "Triển khai ngay với chi phí thiết bị 0 đồng",
            "Tận dụng máy tính & camera hiện có",
            "Không sợ rác nghẹt làm hỏng cảm biến",
            "Dễ dàng mở rộng ra toàn bộ các phường"
        ])
    ]

    for i, (title, bullets) in enumerate(s8_cards):
        add_card(s8, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8), title, bullets, title_color=COLOR_BLUE)

    s8.notes_slide.notes_text_frame.text = (
        "Với việc tận dụng camera và máy tính sẵn có ở địa phương, UrbanShield Lite có thể triển khai ngay ngày mai "
        "mà không cần chờ ngân sách đầu tư tốn kém. Nhóm em hy vọng giải pháp nhỏ bé này sẽ giúp bà con lao động đi làm "
        "về không còn cảnh dắt xe chết máy trong đêm mưa, và người gặp nạn trong hẻm vắng luôn được phát hiện và giúp đỡ kịp thời. "
        "Em xin chân thành cảm ơn Thầy Cô và các bạn!"
    )

    # Save to files
    out_path = os.path.join(os.path.dirname(__file__), "..", "UrbanShield_Lite_SlideDeck.pptx")
    prs.save(out_path)
    print(f"[*] Successfully saved presentation to {os.path.abspath(out_path)}")

if __name__ == "__main__":
    create_deck()
