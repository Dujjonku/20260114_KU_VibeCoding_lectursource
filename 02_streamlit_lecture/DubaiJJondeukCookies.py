import streamlit as st

# ===============================
# 페이지 기본 설정
# ===============================
st.set_page_config(
    page_title="제품 상세 페이지 - 두바이 쫀득 쿠키",
    page_icon="🍪",
    layout="wide",
)

# 전체 페이지를 약간 카드처럼 보이게 하기 위한 스타일
st.markdown(
    """
    <style>
    /* 전체 배경 약간 회색, 가운데 카드 느낌 */
    .main {
        background-color: #f7f7f7;
    }
    .product-card {
        background-color: #ffffff;
        padding: 24px 32px 32px 32px;
        border-radius: 8px;
        border: 1px solid #e5e5e5;
    }
    .product-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .product-subtitle {
        font-size: 20px;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .price-text {
        font-size: 22px;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 4px;
    }
    .rating-text {
        color: #f5a623;
        font-size: 18px;
    }
    .rating-count {
        color: #555;
        margin-left: 6px;
        font-size: 14px;
    }
    .quantity-box {
        background-color: #f5f5f5;
        border-radius: 6px;
        padding: 8px 12px;
    }
    .stButton>button {
        border-radius: 6px;
        height: 45px;
        font-weight: 600;
    }
    /* 장바구니 버튼: 흰 배경, 회색 테두리 */
    .cart-btn button {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #d0d0d0 !important;
    }
    /* 바로구매 버튼: 빨간색 */
    .buy-btn button {
        background-color: #ff5a5f !important;
        color: white !important;
        border: 1px solid #ff5a5f !important;
    }
    /* 탭 아래쪽에 살짝 여백 */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# 1. 사이드바: 카테고리 & 가격 필터
# ===============================
st.sidebar.title("🔍 상품 필터")

category = st.sidebar.selectbox(
    "카테고리 선택",
    ["전체", "쿠키", "마카롱", "케이크", "선물세트"],
    index=1  # 기본 쿠키 선택
)

price_range = st.sidebar.slider(
    "가격 범위 선택 (원)",
    0, 50000, (10000, 30000), step=1000
)

st.sidebar.divider()
st.sidebar.info(
    f"""
**현재 필터 상태**
- 카테고리: `{category}`
- 가격: {price_range[0]:,}원 ~ {price_range[1]:,}원
"""
)

# ===============================
# 메인 카드 영역
# ===============================
# 상단 제목 (예시 이미지처럼)
st.markdown("## 제품 상세 페이지")

# 카드 레이아웃
with st.container():
    st.markdown('<div class="product-card">', unsafe_allow_html=True)

    # 상단: 이미지 / 정보 2컬럼
    img_col, info_col = st.columns([3, 4])

    # ---------- 왼쪽: 제품 이미지 ----------
    with img_col:
        st.image(
            "https://th.bing.com/th/id/OIF.l9QQagRkcu58CEJTOLCUdw?w=319&h=180&c=7&r=0&o=7&pid=1.7&rm=3",
            caption="두바이 쫀득 쿠키",
            use_container_width=True
        )

    # ---------- 오른쪽: 제품 정보 ----------
    with info_col:
        # 제품명
        st.markdown(
            '<div class="product-subtitle">🍪 <span>두바이 쫀득 쿠키</span></div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="price-text">₩19,900</div>', unsafe_allow_html=True)

        # 별점 / 리뷰수
        st.markdown(
            """
            <span class="rating-text">★★★★★</span>
            <span class="rating-count">(4.8) · 리뷰 127개</span>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # 한 줄 설명
        st.write("겉은 바삭, 속은 쫀득한 중동풍 수제 디저트 쿠키 세트")

        # 수량 선택 영역 (예시와 비슷하게)
        st.write("수량:")
        qty_col1, qty_col2, qty_col3 = st.columns([1, 2, 1])

        with qty_col2:
            # number_input을 연한 회색 박스로
            quantity = st.number_input(
                label="",
                min_value=1,
                max_value=1000,
                value=1,
                step=1,
                key="quantity_input"
            )

        # 장바구니 / 바로 구매 버튼 (2컬럼)
        st.write("")
        btn_col1, btn_col2 = st.columns(2)

        with btn_col1:
            with st.container():
                st.markdown('<div class="cart-btn">', unsafe_allow_html=True)
                cart_clicked = st.button("🧺 장바구니", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

        with btn_col2:
            with st.container():
                st.markdown('<div class="buy-btn">', unsafe_allow_html=True)
                buy_clicked = st.button("💳 바로 구매", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

        if cart_clicked:
            st.success(f"장바구니에 {quantity}개 담았습니다!")
        if buy_clicked:
            st.success(f"{quantity}개 구매를 진행한다고 가정해볼게요 🙂")

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# 아래쪽: 탭(상세설명/리뷰/배송정보) + FAQ Expander
# ===============================
st.write("")  # 여백

tab1, tab2, tab3 = st.tabs(["📄 상세설명", "💬 리뷰", "🚚 배송정보"])

# ---------- 탭 1: 상세설명 ----------
with tab1:
    st.subheader("두바이 쫀득 쿠키 상세설명")
    st.markdown(
        """
두바이의 이국적인 향신료와 달콤함을 그대로 담은 **수제 쫀득 쿠키**입니다.  
겉은 바삭하고 속은 쫀득한 식감으로, 한 입 먹는 순간 고급 디저트 카페에 온 듯한 느낌을 줍니다.

- 100% 버터 사용, 풍부한 풍미  
- 천연 바닐라빈, 시나몬, 카다멈 등 중동풍 향신료 블렌딩  
- 인공 색소 / 인공 향료 **무첨가**  
- 개별 포장으로 간편한 나눔 & 선물용으로도 좋아요
"""
    )

    st.markdown("#### 주요 특징")
    st.markdown(
        """
- ✔ 한 박스(기본 구성)당 **12개입**  
- ✔ 상온 보관 기준 **제조일로부터 14일**  
- ✔ 커피, 홍차, 민트티와 환상적인 궁합  
- ✔ 종이 패키지 + 리본 포장 (선물용 가능)
"""
    )

# ---------- 탭 2: 리뷰 ----------
with tab2:
    st.subheader("실제 구매자 리뷰")

    st.markdown(
        """
**디저트러버님**  
> 달달한데 물리지 않고, 향이 진짜 독특해요. 선물했다가 또 재구매했습니다.  
> ⭐⭐⭐⭐⭐  

**쿠키덕후님**  
> 안쪽이 쫀득해서 식감이 재밌어요. 커피랑 같이 먹으면 딱입니다.  
> ⭐⭐⭐⭐☆  

**회사간식담당님**  
> 회사 회의용 간식으로 샀는데 반응이 엄청 좋았어요! 포장도 예뻐서 만족합니다.  
> ⭐⭐⭐⭐⭐  
"""
    )

    st.write("---")
    st.markdown("#### 리뷰 남기기")

    name = st.text_input("이름")
    rating = st.slider("평점", 1, 5, 5)
    comment = st.text_area("리뷰 내용")

    if st.button("리뷰 등록"):
        if name and comment:
            st.success("리뷰가 등록되었다고 가정해볼게요! (실제 저장은 미구현)")
        else:
            st.warning("이름과 리뷰 내용을 모두 입력해 주세요.")

# ---------- 탭 3: 배송정보 ----------
with tab3:
    st.subheader("배송 및 교환·환불 안내")
    st.markdown(
        """
- 기본 배송비: **3,000원**  
- 3만원 이상 구매 시 **무료 배송**  
- 평일 오후 2시 이전 주문 시 **당일 발송** (주말·공휴일 제외)  
- 냉장 제품이 아니므로 일반 택배로 발송됩니다.

**교환 / 환불 규정**

- 제품 수령 후 **7일 이내** 고객센터로 접수해 주세요.  
- 단순 변심의 경우, 상품 가치 훼손이 없을 때에 한해 교환/환불이 가능합니다.  
- 제품 하자 및 오배송의 경우, 판매자가 왕복 배송비를 부담합니다.
"""
    )

# ---------- FAQ (Expander) ----------
st.divider()
st.header("❓ 자주 묻는 질문 (FAQ)")

with st.expander("Q1. 알레르기 유발 성분이 있나요?"):
    st.write(
        """
밀, 우유, 달걀이 포함되어 있으며, 견과류를 취급하는 시설에서 함께 생산됩니다.  
알레르기가 있으신 분들은 섭취 전 꼭 성분을 확인해 주세요.
"""
    )

with st.expander("Q2. 선물 포장도 가능한가요?"):
    st.write(
        """
기본적으로 선물용 패키지로 발송되며, 리본 포장이 포함됩니다.  
여러 명에게 보낼 경우, 주문 메모에 나눔용이라고 남겨주시면  
소분용 쇼핑백을 함께 동봉해드립니다.
"""
    )

with st.expander("Q3. 보관 방법이 어떻게 되나요?"):
    st.write(
        """
직사광선을 피하고 서늘한 곳에 보관해 주세요.  
더운 여름철에는 냉장 보관을 권장드립니다.  
냉장 보관 후에는 실온에 5~10분 두었다가 드시면 가장 맛있습니다.
"""
    )

with st.expander("Q4. 단체 주문 / 기업 선물도 가능한가요?"):
    st.write(
        """
50세트 이상 단체 주문은 별도 할인 견적이 가능합니다.  
문의는 고객센터 또는 이메일로 연락 주세요.
"""
    )
