import streamlit as st
import random

# Title
st.title("🌱 Youth Mental Wellness AI")

st.write("Your confidential space for mental wellness support. 💙")

# -----------------------------
# 1. AI Chat Support (Mock)
# -----------------------------
st.header("💬 AI Chat Support")

user_input = st.text_input("What's on your mind today?")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please type a message.")
    else:
        # Mock empathetic response (in real app: connect to Gemini/Vertex AI API)
        responses = [
            "I hear you. It sounds tough, but you’re not alone 💙",
            "That must be difficult. Remember to take a deep breath 🌿",
            "You’re doing your best, and that’s enough 🌟",
            "Thanks for sharing. Would you like me to suggest some calming activities?"
        ]
        st.success(random.choice(responses))

# -----------------------------
# 2. Mood Check-In
# -----------------------------
st.header("😊 Daily Mood Check-In")

mood = st.radio(
    "How are you feeling today?",
    ["😃 Happy", "🙂 Okay", "😔 Sad", "😟 Stressed", "😴 Tired"]
)

if st.button("Save Mood"):
    st.info(f"Your mood '{mood}' has been saved! 💾 (Prototype demo)")

# -----------------------------
# 3. Resource Suggestions
# -----------------------------
st.header("📘 Self-Care Resources")

if mood in ["😔 Sad", "😟 Stressed", "😴 Tired"]:
    st.write("Here are some quick self-care tips for you:")
    st.markdown("- 🌬️ Try 2 minutes of deep breathing")
    st.markdown("- 📝 Write your feelings in a journal")
    st.markdown("- ☎️ If overwhelmed, please call your local mental health helpline")
else:
    st.write("Keep up the positive vibes! Here are some activities:")
    st.markdown("- 🎶 Listen to your favorite song")
    st.markdown("- 🚶 Go for a short walk")
    st.markdown("- 💬 Talk with a friend or family member")
