import streamlit as st
import random

# Streamlit 페이지 설정
st.set_page_config(page_title="오늘의 꿀팁", layout="centered", initial_sidebar_state="collapsed")

# 1. 점심 메뉴 추천 리스트 (Lunch Menu Recommendations)
lunch_menu = [
    "김치찌개 🥘",
    "된장찌개",
    "제육볶음 🌶️",
    "돈까스",
    "샐러드 (가볍게!) 🥗",
    "햄버거 🍔",
    "국밥 (든든하게!)",
    "파스타 (가끔은 분위기 있게)",
    "샌드위치 (간단하게 해결)"
]

# 2. 명언 리스트 (Quotes)
quotes = [
    "시작이 반이다.",
    "성공은 최종적인 것이 아니며, 실패는 치명적인 것이 아니다. 중요한 것은 계속하려는 용기이다. - 윈스턴 처칠",
    "미래는 현재 우리가 무엇을 하는가에 달려 있다. - 마하트마 간디",
    "가장 중요한 것은 삶을 즐기는 것, 행복한 것, 그것이 전부다. - 오드리 햅번",
    "인생은 용기의 문제이다. - 아멜리아 에어하트",
    "하루를 지배하는 자가 인생을 지배한다. - 알 수 없음"
]

# 3. 농담 리스트 (Jokes)
jokes = [
    "세상에서 가장 쉬운 숫자는? 190,000 (쉽구만)",
    "세상에서 제일 착한 사자는? 자원봉사자",
    "가장 뜨거운 옷은? 흥분",
    "왕이 넘어지면 뭐가 될까? 킹콩",
    "소금의 유통기한은? 천일염",
    "세상에서 가장 느린 차는? 우스터소스"
]

# 4. 일상생활 꿀팁 리스트 (Daily Tips)
daily_tips = [
    "따뜻한 물을 자주 마시면 건강에 좋아요! 💧",
    "잠자리에 들기 전 30분 동안 스마트폰을 멀리해 보세요.",
    "오래 앉아 있었다면 5분 스트레칭을 꼭 해주세요. 💪",
    "책상 위를 정리하면 집중력이 높아집니다.",
    "작은 목표라도 매일 달성하면 자신감이 커집니다.",
    "외출 전 미리 날씨를 확인하고 옷을 챙기세요."
]

# 모든 카테고리와 그 내용을 딕셔너리에 저장
all_categories = {
    "점심 메뉴 추천 🍽️": lunch_menu,
    "오늘의 명언 ✨": quotes,
    "오늘의 유머 😄": jokes,
    "일상생활 꿀팁 💡": daily_tips
}

# --- Streamlit UI 구성 시작 ---

st.title("✨ 오늘의 랜덤 꿀팁 생성기 ✨")
st.markdown("""
<div style='background-color: #F0F2F6; padding: 15px; border-radius: 10px;'>
    <p style='margin: 0; font-size: 16px; color: #333333;'>
        아래 버튼을 누르면 <strong>명언, 농담, 점심 메뉴, 일상 꿀팁</strong> 중 하나를 무작위로 뽑아 보여드립니다.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# 세션 상태 초기화 (팁의 카테고리와 내용 저장)
if 'tip_category' not in st.session_state:
    st.session_state.tip_category = "환영합니다!"
    st.session_state.tip_content = "버튼을 눌러 오늘의 첫 번째 꿀팁을 확인해 보세요!"

def generate_tip():
    """랜덤으로 카테고리를 선택하고 그에 맞는 팁을 세션 상태에 저장하는 함수"""
    category_name = random.choice(list(all_categories.keys()))
    selected_list = all_categories[category_name]
    selected_item = random.choice(selected_list)
    
    st.session_state.tip_category = category_name
    st.session_state.tip_content = selected_item

# 팁 생성 버튼. 버튼을 누르면 generate_tip 함수 실행 후 스크립트 재실행
if st.button("새로운 꿀팁 받기 🔄", type="primary", use_container_width=True):
    generate_tip()

# 결과 표시
st.markdown(f"## {st.session_state.tip_category}")

# 오류가 발생했던 st.success 부분을 st.markdown으로 변경하고 스타일 조정
st.markdown(f"""
<div style='background-color: #E6F7F0; /* 연한 녹색 배경 (성공 색상 계열) */
            color: #1F7A54; /* 짙은 녹색 글씨 */
            padding: 25px; 
            border-radius: 12px; 
            font-size: 24px; 
            text-align: center; 
            border: 1px solid #B3E0CC;'>
    <strong>{st.session_state.tip_content}</strong>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("powered by Streamlit & Python")
