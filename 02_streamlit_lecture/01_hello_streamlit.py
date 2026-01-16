"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "wide" 또는 "wide"
)

# 제목 표시
st.title("🎉 이동현")

# 간단한 텍스트 출력
st.write("연습중이에용.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 이동현")
st.write("직업: 물리치료 공부중인 대학생")
st.write("관심사: 응아하기, 씻기, 먹기")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
    st.success("반갑습니다! 🎊")


if st.button("비밀 메시지 확인하기"):
    st.warning("이 메시지는 1895년 프랑스에서 시작되어... 🤫 ")
# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
