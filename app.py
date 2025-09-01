import streamlit as st
from transformers import pipeline
from googletrans import Translator

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="Youth Mental Wellness AI", page_icon="🌱")
st.title("🌱 Youth Mental Wellness AI")
st.subheader("A safe space for journaling, mood reflection, and chat support")

# -----------------------------
# Load NLP models
# -----------------------------
sentiment = pipeline("sentiment-analysis")
translator = Translator()

# -----------------------------
# Journaling + Mood Reflection
# -----------------------------
st.markdown("### ✍️ Write Your Journal Entry")
journal_input = st.text_area("How are you feeling today?", "")

if st.button("Reflect on Journal"):
    if journal_input.strip():
        # Detect language and translate to English if needed
        try:
            detected_lang = translator.detect(journal_input).lang
            if detected_lang != "en":
                journal_en = translator.translate(journal_input, src=detected_lang, dest='en').text
            else:
                journal_en = journal_input
        except:
            journal_en = journal_input

        # Sentiment analysis
        result = sentiment(journal_en)[0]
        mood = result['label']
        score = round(result['score'] * 100, 2)
        st.success(f"AI Reflection: Your entry shows **{mood}** ({score}% confidence).")
    else:
        st.warning("Please enter some text to reflect on.")

# -----------------------------
# AI Companion Chat
# -----------------------------
st.markdown("### 💬 Chat with AI Companion")
user_message = st.text_input("Say something to your AI friend:")

if user_message.strip():
    response = f"I hear you saying: '{user_message}'. Remember, you are not alone. 🌸"
    st.info(response)

# -----------------------------
# Safety & Disclaimer
# -----------------------------
st.markdown("---")
st.markdown(
    "**⚠️ Disclaimer:** This app provides supportive reflections and is not a substitute for professional help. "
    "If you or someone else is in immediate danger, please contact local emergency services or a trusted mental health professional."
)
