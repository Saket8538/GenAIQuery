import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    return model

def gemini_ai_chat(model):
    st.title("Gemini AI Chat")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    input_prompt = st.text_area("Welcome to AI companion:")
    if st.button("Send"):
        response = model.generate_content(input_prompt)
        st.session_state.chat_history.append({"user": input_prompt, "gemini": response.text})

    for chat in st.session_state.chat_history:
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Gemini:** {chat['gemini']}")

# Main function
def main():
    model = configure()
    st.sidebar.title("Navigation")
    tab = st.sidebar.selectbox("Choose a tab", ["Home", "Gemini AI Chat"])

    if tab == "Gemini AI Chat":
        gemini_ai_chat(model)

if __name__ == "__main__":
    main()