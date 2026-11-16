
import streamlit as st
import random

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="가위바위보 챌린지",
    page_icon="✊",
    layout="centered"
)

# -----------------------------
# 디자인 CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

.stApp {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
}

html, body, [class*="css"] {
    font-family: 'Jua', sans-serif;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4338ca;
    padding: 20px 0 5px 0;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

.score-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.07);
}

.score-number {
    font-size: 36px;
    color: #4f46e5;
    font-weight: bold;
}

.result-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.result-title {
    font-size: 32px;
    font-weight: bold;
}

.choice-emoji {
    font-size: 65px;
}

div.stButton > button {
    width: 100%;
    height: 85px;
    border-radius: 18px;
    border: 2px solid #c7d2fe;
    background-color: white;
    color: #3730a3;
    font-size: 22px;
    transition: 0.2s;
}

div.stButton > button:hover {
    background-color: #e0e7ff;
    border-color: #6366f1;
    color: #312e81;
    transform: translateY(-3px);
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 게임 데이터
# -----------------------------
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 세션 상태 초기화
if "win" not in st.session_state:
    st.session_state.win = 0

if "lose" not in st.session_state:
    st.session_state.lose = 0

if "draw" not in st.session_state:
    st.session_state.draw = 0

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

if "result" not in st.session_state:
    st.session_state.result = None

# -----------------------------
# 승패 판정 함수
# -----------------------------
def play_game(user_choice):
    computer_choice = random.choice(list(choices.keys()))

    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice

    if user_choice == computer_choice:
        st.session_state.result = "draw"
        st.session_state.draw += 1

    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        st.session_state.result = "win"
        st.session_state.win += 1

    else:
        st.session_state.result = "lose"
        st.session_state.lose += 1

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<div class="main-title">✊ 가위바위보 챌린지 ✌️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">컴퓨터를 이기고 최고의 챔피언에 도전하자! 🔥</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# 점수판
# -----------------------------
st.subheader("🏆 나의 전적")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="score-card">
        <div>🏆 승리</div>
        <div class="score-number">{st.session_state.win}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="score-card">
        <div>💀 패배</div>
        <div class="score-number">{st.session_state.lose}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="score-card">
        <div>🤝 무승부</div>
        <div class="score-number">{st.session_state.draw}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------
# 사용자 선택
# -----------------------------
st.subheader("🎮 무엇을 낼까요?")
st.write("아래 버튼 중 하나를 선택하세요!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✌️\n가위", key="scissors"):
        play_game("가위")

with col2:
    if st.button("✊\n바위", key="rock"):
        play_game("바위")

with col3:
    if st.button("✋\n보", key="paper"):
        play_game("보")

# -----------------------------
# 게임 결과
# -----------------------------
if st.session_state.result is not None:

    st.divider()
    st.subheader("⚔️ 대결 결과")

    user = st.session_state.user_choice
    computer = st.session_state.computer_choice

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="result-card">
            <h3>🙋 나</h3>
            <div class="choice-emoji">{choices[user]}</div>
            <h3>{user}</h3>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="result-card">
            <h3>🤖 컴퓨터</h3>
            <div class="choice-emoji">{choices[computer]}</div>
            <h3>{computer}</h3>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if st.session_state.result == "win":
        st.balloons()
        st.success("🎉 승리! 대단해요! 당신이 이겼습니다!")

    elif st.session_state.result == "lose":
        st.error("😭 패배! 아쉽네요. 다음에는 꼭 이겨봐요!")

    else:
        st.info("🤝 무승부! 승부를 다시 겨뤄보세요!")

    total = (
        st.session_state.win
        + st.session_state.lose
        + st.session_state.draw
    )

    if total > 0:
        win_rate = st.session_state.win / total * 100

        st.markdown(
            f"### 📊 현재 승률: {win_rate:.1f}%"
        )

        st.progress(win_rate / 100)

# -----------------------------
# 다시 시작 버튼
# -----------------------------
st.divider()

if st.button("🔄 점수 초기화하기", use_container_width=True):
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None
    st.rerun()

# -----------------------------
# 하단 안내
# -----------------------------
st.markdown("""
<div class="footer">
    ✨ 가위바위보 챌린지 | 오늘의 승자는 바로 당신! ✨
</div>
""", unsafe_allow_html=True)
