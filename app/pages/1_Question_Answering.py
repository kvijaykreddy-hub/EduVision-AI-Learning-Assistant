import streamlit as st

from eduvision_ai.services.qa_service import QAService

st.set_page_config(
    page_title="Question Answering",
    page_icon="❓",
)

st.title("❓ Question Answering")

st.write(
    "Ask any educational question and get an AI-powered answer."
)

question = st.text_area(
    "Enter your question:",
    height=180,
    placeholder="Example: Explain the concept of Machine Learning.",
)

st.caption(f"Characters: {len(question)}")

service = QAService()

if st.button(
    "Get Answer",
    type="primary",
    disabled=not question.strip(),
):

    with st.spinner("Generating answer..."):

        try:
            result = service.ask(question)

            st.success(
                f"Answer generated successfully in "
                f"{result.response_time:.2f} seconds."
            )

            st.caption(f"Model: {result.model}")

            st.markdown("### Answer")

            st.container(border=True).write(result.content)

        except Exception as e:
            st.error(f"Error: {e}")