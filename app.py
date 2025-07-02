import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎨✨ Interactive Art Therapy")
st.write("Get personalized art activity suggestions to improve your mood and express yourself creatively! 💚")

# Inputs
mood = st.text_input("💬 How do you feel right now?", placeholder="e.g., stressed, sad, anxious, bored...")
desired_emotion = st.text_input("🌟 How would you like to feel after doing art?", placeholder="e.g., calm, joyful, motivated...")
context = st.text_area("📝 Anything you'd like to share? (optional)", placeholder="e.g., had a tough day at work, feeling lonely, need motivation...")

if st.button("🎨 Get Art Activity Suggestion"):
    prompt = f"""
You are a compassionate art therapist AI. Based on the following inputs, suggest a creative art activity or exercises to help the user move from their current mood to their desired emotional state.

- Current mood: {mood}
- Desired emotion: {desired_emotion}
- Additional context: {context}

Provide a personalized art activity or multiple activity options, and also add a short encouraging or motivational message.
"""

    response = model.generate_content(prompt)
    st.subheader("🎨 Your Personalized Art Activity")
    st.write(response.text)

st.markdown("---")
st.markdown("✅ **Remember: There’s no right or wrong in art. Just express yourself freely! 💚**")
