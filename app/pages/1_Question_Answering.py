import time

import streamlit as st

from eduvision_ai.services.llm_service import LLMService


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Question Answering",
    page_icon="🤖",
)

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("🤖 Question Answering")

st.write(
    "Ask any question and get an AI-generated answer."
)

st.divider()

# ---------------------------------------------------------
# Question Input
# ---------------------------------------------------------
question = st.text_area(
    label="Enter your question",
    placeholder="Example: Explain Retrieval-Augmented Generation (RAG).",
    height=150,
)

# Character Counter
st.caption(f"Characters: {len(question)}")

# ---------------------------------------------------------
# Submit Button
# ---------------------------------------------------------
generate = st.button(
    "🚀 Get Answer",
    type="primary",
    disabled=not question.strip(),
)

# ---------------------------------------------------------
# Process Question
# ---------------------------------------------------------
if generate:

    service = LLMService()

    with st.spinner("🤖 Gemini is thinking..."):

        start = time.perf_counter()

        try:

            answer = service.ask(question)

            end = time.perf_counter()

            response_time = end - start

            st.success(
                f"✅ Answer generated successfully in {response_time:.2f} seconds."
            )

            st.divider()

            with st.container(border=True):

                st.subheader("📖 Answer")

                st.write(answer)

        except Exception as e:

            st.error("❌ Unable to generate answer.")

            with st.expander("View Error Details"):

                st.code(str(e))