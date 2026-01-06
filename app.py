import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cấu hình trang web
st.set_page_config(
    page_title="Duyên hải Miền Trung 2026 - to4lol.xyz",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS nâng cao cho giao diện thuyết trình
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #0c4a6e;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-title {
        font-size: 1.5rem;
        color: #0284c7;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .card {
        padding: 2rem;
        border-radius: 1rem;
        background: white;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #0ea5e9;
        margin-bottom: 1.5rem;
        color: #1e293b;
    }
    
    .metric-card {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    
    /* Fix lỗi vỡ ảnh và làm đẹp ảnh */
    .stImage > img {
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        transition: transform 0.3s ease !important;
        object-fit: cover !important;
        width: 100% !important;
        min-height: 250px;
        background-color: #e2e8f0; /* Màu nền khi ảnh chưa tải */
    }

    .stImage > img:hover {
        transform: translateY(-5px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ĐIỀU HƯỚNG ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/100/lighthouse.png", width=80)
    st.title("🌐 to4lol.xyz")
    st.markdown("---")
    app_mode = st.selectbox(
        "Chọn chương mục thuyết trình:",
        ["01. Mở đầu & Tổng quan", 
         "02. Vị trí & Đặc điểm Tự nhiên", 
         "03. Phân tích Kinh tế 2026", 
         "04. Du lịch & Di sản", 
         "05. Hạ tầng & Kết nối", 
         "06. Tầm nhìn & Kết luận"]
    )
    st.markdown("---")
    st.info("📊 **Dữ liệu:** Cập nhật dự báo quý I/2026")
    st.caption("© 2026 Nhóm Nghiên cứu Tổ 4 - to4lol")

# --- HÀM TIỆN ÍCH HIỂN THỊ ẢNH ---
def display_image(url, cap):
    try:
        st.image(url, caption=cap, use_container_width=True)
    except:
        st.error(f"Không thể tải hình ảnh: {cap}. Vui lòng kiểm tra kết nối mạng.")

# --- NỘI DUNG CHÍNH ---

if app_mode == "01. Mở đầu & Tổng quan":
    st.markdown('<p class="main-title">🌊 DUYÊN HẢI MIỀN TRUNG</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Cực tăng trưởng kinh tế biển bền vững 2026</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class="card">
        <h3>LỜI MỞ ĐẦU</h3>
        Vùng Duyên hải Miền Trung bao gồm 14 tỉnh, thành phố từ Thanh Hóa đến Bình Thuận. 
        Đây là dải đất đóng vai trò "mặt tiền" của Việt Nam hướng ra Biển Đông. 
        Bước sang năm 2026, vùng đã chuyển mình mạnh mẽ từ một dải đất chịu nhiều thiên tai thành 
        <b>trung tâm kinh tế xanh</b>, nơi hội tụ của năng lượng tái tạo và logistics toàn cầu.
        <br><br>
        Dự án <b>to4lol.xyz</b> được xây dựng nhằm cung cấp cái nhìn toàn diện về tiềm năng 
        và bước tiến thần tốc của khu vực này trong kỷ nguyên mới.
        </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric-card">🚀 <b>GRDP Vùng</b><br><span style="font-size:1.5rem; color:#0284c7;">+8.5%</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-card">👥 <b>Dân số</b><br><span style="font-size:1.5rem; color:#0284c7;">~21 Triệu</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-card">🏗️ <b>Khu Kinh tế</b><br><span style="font-size:1.5rem; color:#0284c7;">12 Trọng điểm</span></div>', unsafe_allow_html=True)
            
    with col2:
        display_image("https://images.unsplash.com/photo-1596422846543-75c6fc18a594?q=80&w=1000&auto=format&fit=crop", "Toàn cảnh bờ biển miền Trung hiện đại")

elif app_mode == "02. Vị trí & Đặc điểm Tự nhiên":
    st.header("📍 Vị trí Chiến lược & Thiên nhiên")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("1. Vị trí Địa chính trị")
        st.write("""
        - **Hành lang Kinh tế Đông - Tây:** Kết nối biển với Lào, Thái Lan và Myanmar.
        - **Cửa ngõ Tây Nguyên:** Là lối ra biển gần nhất của vùng nguyên liệu lớn nhất nước.
        - **Chiến lược Biển:** Chiếm hơn 50% số lượng các cảng nước sâu của Việt Nam.
        """)
        display_image("https://images.unsplash.com/photo-1528127269322-539801943592?q=80&w=1000&auto=format&fit=crop", "Địa hình núi sát biển đặc trưng")

    with col2:
        st.subheader("2. Tài nguyên & Khí hậu")
        with st.expander("Khí hậu khắc nghiệt nhưng giàu năng lượng", expanded=True):
            st.write("""
            Dù chịu nhiều bão lũ, nhưng nắng và gió là 'đặc sản' giúp miền Trung dẫn đầu về năng lượng sạch. 
            Ninh Thuận và Bình Thuận hiện chiếm 40% công suất điện tái tạo cả nước.
            """)
        with st.expander("Địa hình vũng vịnh sâu"):
            st.write("""
            Nhiều vịnh sâu như Cam Ranh, Vũng Rô, Chân Mây cho phép đón các tàu trọng tải lớn nhất thế giới (>200.000 DWT).
            """)
        display_image("https://images.unsplash.com/photo-1466611653911-95282fc3656b?q=80&w=1000&auto=format&fit=crop", "Cánh đồng điện gió tại Ninh Thuận")

elif app_mode == "03. Phân tích Kinh tế 2026":
    st.header("📈 Phân tích Động lực Kinh tế")
    
    st.markdown("""
    <div class="card">
    Kinh tế Miền Trung năm 2026 dựa trên 3 trụ cột: <b>Công nghiệp nặng (Lọc dầu, Thép) - Kinh tế Biển (Cảng, Thủy sản) - Du lịch dịch vụ cao cấp.</b>
    </div>
    """, unsafe_allow_html=True)

    econ_data = pd.DataFrame({
        'Địa phương': ['Thanh Hóa', 'Đà Nẵng', 'Quảng Ngãi', 'Bình Định', 'Khánh Hòa', 'Ninh Thuận'],
        'Tăng trưởng (%)': [9.2, 10.5, 8.8, 7.9, 11.2, 9.5],
        'Vốn FDI (Triệu USD)': [1200, 850, 2100, 450, 1600, 700]
    })
    
    tab1, tab2 = st.tabs(["📊 Biểu đồ Tăng trưởng", "💰 Thu hút Đầu tư FDI"])
    
    with tab1:
        fig_grdp = px.bar(econ_data, x='Địa phương', y='Tăng trưởng (%)', 
                          text_auto='.1f', title="Tốc độ tăng trưởng GRDP dự báo năm 2026",
                          color='Tăng trưởng (%)', color_continuous_scale='Blues')
        st.plotly_chart(fig_grdp, use_container_width=True)
        
    with tab2:
        fig_fdi = px.pie(econ_data, values='Vốn FDI (Triệu USD)', names='Địa phương', 
                        hole=.4, title="Cơ cấu thu hút FDI trong vùng",
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_fdi, use_container_width=True)

elif app_mode == "04. Du lịch & Di sản":
    st.header("🏖️ Hệ sinh thái Du lịch & Văn hóa")
    
    st.info("💡 Miền Trung là nơi duy nhất tại Việt Nam sở hữu 5 di sản văn hóa thế giới được UNESCO công nhận trên một cung đường.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - **Quần thể di tích Cố đô Huế:** Biểu tượng lịch sử phong kiến.
        - **Phố cổ Hội An:** Thương cảng mang đậm nét giao thoa văn hóa Đông - Tây.
        - **Thánh địa Mỹ Sơn:** Những đền tháp Chăm Pa nghìn năm tuổi.
        - **Vườn Quốc gia Phong Nha - Kẻ Bàng:** 'Vương quốc hang động' toàn cầu.
        - **Không gian Văn hóa Cồng chiêng:** Sự kết nối với đồng bào vùng cao.
        """)
        display_image("https://images.unsplash.com/photo-1583417319070-4a69db38a482?q=80&w=1000&auto=format&fit=crop", "Vẻ đẹp trường tồn của Cố đô Huế")
            
    with col2:
        st.markdown("### 💎 Chỉ số Du lịch")
        st.success("Lượt khách: 45 Triệu/năm")
        st.success("Doanh thu: ~150.000 Tỷ VNĐ")
        display_image("https://images.unsplash.com/photo-1559592490-348633c74825?q=80&w=1000&auto=format&fit=crop", "Bờ biển Nha Trang - Khánh Hòa")

elif app_mode == "05. Hạ tầng & Kết nối":
    st.header("🛣️ Hạ tầng Giao thông: Mạch máu vùng")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hệ thống Cao tốc & Đường bộ")
        st.write("""
        Tuyến cao tốc Bắc - Nam đi qua toàn bộ các tỉnh miền Trung đã hoàn thiện, 
        giúp việc giao thương từ Thanh Hóa đến Bình Thuận chỉ còn mất 1/2 thời gian so với trước đây.
        """)
        st.progress(100, text="Hoàn tất Cao tốc Bắc - Nam")
        display_image("https://images.unsplash.com/photo-1545143333-6382b1e58473?q=80&w=1000&auto=format&fit=crop", "Hạ tầng giao thông kết nối hiện đại")

    with col2:
        st.subheader("Cảng biển & Logistics")
        st.write("""
        Cảng Liên Chiểu (Đà Nẵng) và Cảng Cam Ranh (Khánh Hòa) trở thành 
        hai mắt xích không thể thiếu trong chuỗi cung ứng hàng hải quốc tế năm 2026.
        """)
        display_image("https://images.unsplash.com/photo-1494412519320-aa613dfb7738?q=80&w=1000&auto=format&fit=crop", "Hoạt động bốc dỡ hàng hóa tại cảng thông minh")

elif app_mode == "06. Tầm nhìn & Kết luận":
    st.header("🏁 Kết luận: Tầm nhìn 2030 - 2045")
    st.balloons()
    
    st.markdown("""
    <div class="card">
    <h3>THÔNG ĐIỆP KẾT LUẬN</h3>
    Duyên hải Miền Trung không còn là "vùng đệm" mà đã vươn lên trở thành <b>đầu tàu kinh tế mới</b> của Việt Nam. 
    Với sự kết hợp giữa bảo tồn di sản và đổi mới công nghệ, vùng đất này đang hiện thực hóa khát vọng hùng cường.
    <br><br>
    Cảm ơn thầy cô và các bạn đã theo dõi bài thuyết trình trên <b>to4lol.xyz</b>!
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Mục tiêu 2030")
        st.write("- Trở thành vùng kinh tế phát triển năng động nhất Đông Nam Á.")
        display_image("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1000&auto=format&fit=crop", "Đô thị biển xanh và thông minh")
    with c2:
        st.subheader("Cam kết 2045")
        st.write("- Phát thải ròng bằng 0 (Net Zero) nhờ năng lượng tái tạo.")
        display_image("https://images.unsplash.com/photo-1518467166778-b88f373ffec7?q=80&w=1000&auto=format&fit=crop", "Bảo tồn hệ sinh thái biển bền vững")

st.markdown("<br><hr><center><b>to4lol.xyz</b> | Hệ thống Thuyết trình Kinh tế Vùng | Version 2.2.0 (Stable)</center>", unsafe_allow_html=True)