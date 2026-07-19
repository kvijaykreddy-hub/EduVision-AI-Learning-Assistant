"""
Question Answering Page.
"""

import streamlit as st

from eduvision_ai.services.qa_service import QAService

st.set_page_config(
    page_title="Question Answering",
    page_icon="❓",
)

st.title("❓ Question Answering")

# ============================================================
# Session State
# ============================================================

if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

st.write(
    "Ask any educational question and get an AI-powered answer."
)

# ============================================================
# OCR Context
# ============================================================

context = ""

if st.session_state.ocr_text.strip():

    with st.expander("📄 OCR Context (Loaded Automatically)", expanded=False):

        st.info(
            "Questions will be answered using the OCR extracted text as context."
        )

        st.text_area(
            "OCR Text",
            value=st.session_state.ocr_text,
            height=200,
            disabled=True,
        )

    context = st.session_state.ocr_text

# ============================================================
# Question
# ============================================================

question = st.text_area(
    "Enter your question:",
    height=180,
    placeholder="Example: Explain the concept of Machine Learning.",
)

st.caption(f"Characters: {len(question)}")

service = QAService()

# ============================================================
# Ask Button
# ============================================================

if st.button(
    "Get Answer",
    type="primary",
    disabled=not question.strip(),
):

    with st.spinner("Generating answer..."):

        try:

            # --------------------------------------------------
            # If OCR text exists, use it as context
            # --------------------------------------------------

            if context.strip():

                prompt = f"""
Use ONLY the following document to answer the question.

Document:

{context}

Question:

{question}

If the answer is not available in the document,
say that it is not mentioned.
"""

                result = service.ask(prompt)

            else:

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