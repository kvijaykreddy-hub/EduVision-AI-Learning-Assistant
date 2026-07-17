import streamlit as st

st.set_page_config(
    page_title="EduVision AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduVision AI - Learning Assistant")

st.markdown("""
Welcome to **EduVision AI**.

This application demonstrates:

- 📚 Question Answering
- 📝 Text Summarization
- ❓ Quiz Generation
- 🖼️ OCR from Images
- 🧠 Image Classification

Built using:
- LangChain
- Hugging Face
- Streamlit
""")