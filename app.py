import streamlit as st
from pathlib import Path
import time

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="HealthHelper",
    page_icon="🍑",
    layout="centered"
)

# -----------------------
# Custom CSS Styling
# -----------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');

html, body, [class*="css"], .stMarkdown, .stRadio, label, p {
    font-family: 'Nunito', sans-serif !important;
    color: #4A2C2A !important;
}

.stApp {
    background: linear-gradient(160deg, #FFF0EB 0%, #FFE4D6 50%, #FFDAC7 100%) !important;
    min-height: 100vh;
}

.block-container {
    max-width: 700px !important;
    padding: 3rem 2.8rem 4rem !important;
    background: rgba(255, 255, 255, 0.75) !important;
    border-radius: 32px !important;
    margin-top: 2.5rem !important;
    box-shadow:
        0 10px 40px rgba(220, 100, 60, 0.12),
        0 2px 10px rgba(220, 100, 60, 0.08) !important;
    border: 1.5px solid rgba(255, 180, 140, 0.3) !important;
}

h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.6rem !important;
    color: #C4512A !important;
    letter-spacing: -0.5px !important;
    line-height: 1.2 !important;
}

h2 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.7rem !important;
    color: #C4512A !important;
}

h3 {
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    color: #B84A24 !important;
    letter-spacing: 0.2px !important;
}

p, .stMarkdown p {
    font-size: 1.08rem !important;
    line-height: 1.75 !important;
    color: #6B3A30 !important;
}

img {
    border-radius: 22px !important;
    box-shadow: 0 8px 30px rgba(200, 80, 40, 0.15) !important;
    border: 3px solid rgba(255, 180, 140, 0.4) !important;
}

div[data-testid="stRadio"] > label {
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    color: #B84A24 !important;
    margin-bottom: 0.4rem !important;
}

div[data-testid="stRadio"] label {
    background: #FFF5F0 !important;
    border: 2px solid #FFBDA0 !important;
    border-radius: 14px !important;
    padding: 0.65rem 1.1rem !important;
    margin-bottom: 0.5rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    font-size: 1rem !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
    color: #4A2C2A !important;
    display: block !important;
}

div[data-testid="stRadio"] label:hover {
    background: #FFE4D6 !important;
    border-color: #E8714A !important;
    transform: translateX(5px) !important;
    box-shadow: 0 4px 14px rgba(220, 100, 60, 0.15) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #E8714A 0%, #C4512A 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.7rem 2.4rem !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.3px !important;
    cursor: pointer !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 5px 18px rgba(200, 80, 40, 0.35) !important;
    margin-top: 1rem !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 28px rgba(200, 80, 40, 0.45) !important;
    background: linear-gradient(135deg, #F07D58 0%, #D45E35 100%) !important;
}

.stButton > button:active {
    transform: translateY(-1px) !important;
}

div[data-testid="stAlert"] {
    border-radius: 16px !important;
    border: none !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    padding: 1rem 1.3rem !important;
}

.stImage figcaption, .stImage > div > small {
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.88rem !important;
    color: #B07060 !important;
    font-style: italic !important;
    margin-top: 0.4rem !important;
}

/* ── Emoji feedback card ── */
.emoji-card {
    background: linear-gradient(135deg, #FFF0EB, #FFE4D6);
    border: 2px solid #FFBDA0;
    border-radius: 24px;
    padding: 1.8rem;
    text-align: center;
    margin: 1.2rem 0;
    box-shadow: 0 6px 20px rgba(220, 100, 60, 0.12);
}

.emoji-big {
    font-size: 4rem;
    display: block;
    margin-bottom: 0.5rem;
    animation: bounceIn 0.8s ease;
}

.emoji-label {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    color: #C4512A;
    font-weight: 700;
    display: block;
    margin-bottom: 0.3rem;
}

.emoji-sub {
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    color: #6B3A30;
}

@keyframes bounceIn {
    0%   { transform: scale(0.3); opacity: 0; }
    50%  { transform: scale(1.15); opacity: 1; }
    75%  { transform: scale(0.95); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Page setup
# -----------------------
st.title("HealthHelper - Quick Survey")

st.write(
    "This website will ask you a few questions about health habits. "
    "Please answer honestly. Your data is safe and used for research."
)

# Image
img_path = Path(__file__).parent / "happy-person-png-23624.png"
st.image(img_path, caption="You after completing the survey!")

st.header("Are you ready to continue?")

# -----------------------
# Session State
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "q1"

if "answers" not in st.session_state:
    st.session_state.answers = {}

# -----------------------
# Question 1
# -----------------------
if st.session_state.page == "q1":

    st.subheader("Question 1: How often do you exercise?")

    choice = st.radio(
        "Select one:",
        ["Never", "1-2 times a week", "3-5 times a week", "Daily"]
    )

    if st.button("Next"):
        st.session_state.answers["exercise"] = choice
        st.session_state.page = "q2"
        st.rerun()

# -----------------------
# Question 2
# -----------------------
elif st.session_state.page == "q2":

    st.subheader("Question 2: How do you usually feel during the day?")

    choice = st.radio(
        "Select one:",
        ["Tired", "Energetic", "Neutral"]
    )

    if st.button("Next"):
        st.session_state.answers["energy"] = choice
        st.session_state.page = "q3"
        st.rerun()

# -----------------------
# Question 3
# -----------------------
elif st.session_state.page == "q3":

    st.subheader("Question 3: Do you track your health regularly?")

    choice = st.radio(
        "Select one:",
        ["Yes", "No"]
    )

    if st.button("Finish"):
        st.session_state.answers["tracking"] = choice
        st.session_state.page = "result"
        st.rerun()

# -----------------------
# Results Pages
# -----------------------
elif st.session_state.page == "result":

    st.title("Survey Result 🎉")

    answers = st.session_state.answers

    # -----------------------
    # Animated emoji feedback
    # -----------------------
    exercise = answers.get("exercise", "")
    energy = answers.get("energy", "")
    tracking = answers.get("tracking", "")

    # Determine emoji + label based on answers
    if exercise == "Daily" and energy == "Energetic":
        emoji = "🏆"
        label = "Health Champion!"
        sub = "You're absolutely crushing it. Keep up the amazing work."
    elif exercise in ["3-5 times a week", "Daily"] and tracking == "Yes":
        emoji = "💪"
        label = "Strong & On Track!"
        sub = "Great habits and great awareness — a winning combo."
    elif exercise in ["1-2 times a week"] and energy == "Energetic":
        emoji = "🌱"
        label = "Growing Strong!"
        sub = "You're off to a good start. A little more consistency and you'll thrive."
    elif exercise == "Never" and energy == "Tired":
        emoji = "🌅"
        label = "Ready for a Fresh Start!"
        sub = "Everyone starts somewhere. Small steps lead to big changes."
    elif energy == "Tired":
        emoji = "😴"
        label = "Time to Recharge!"
        sub = "Rest is important, but some movement might boost your energy too."
    elif tracking == "No":
        emoji = "📋"
        label = "Let's Get Organized!"
        sub = "Tracking your habits can make a huge difference in staying motivated."
    else:
        emoji = "😊"
        label = "Doing Pretty Well!"
        sub = "You have some solid habits — keep building on them!"

    # Display the animated emoji card
    st.markdown(f"""
    <div class="emoji-card">
        <span class="emoji-big">{emoji}</span>
        <span class="emoji-label">{label}</span>
        <span class="emoji-sub">{sub}</span>
    </div>
    """, unsafe_allow_html=True)

    # Simple decision logic
    if answers["exercise"] in ["Never", "1-2 times a week"] or answers["tracking"] == "No":
        st.warning("HealthHelper could help improve your routine!")
    else:
        st.success("You already have strong habits! HealthHelper could still help with tracking.")

    # 💡 Personalized Tips
    st.subheader("💡 Your Personalized Tip")

    if answers["exercise"] == "Never":
        st.write("Start small! Try a 10-minute walk every day 🚶")

    elif answers["exercise"] == "1-2 times a week":
        st.write("Good start! Try adding one more workout each week 💪")

    elif answers["exercise"] == "3-5 times a week":
        st.write("Nice work! Keep being consistent 🔥")

    elif answers["exercise"] == "Daily":
        st.write("Amazing! You're doing great, keep it up 🏆")

    # Extra tip based on tracking
    if answers["tracking"] == "No":
        st.write("📊 Try tracking your habits to stay motivated!")

    if st.button("Restart Survey"):
        st.session_state.page = "q1"
        st.session_state.answers = {}
        st.rerun()
