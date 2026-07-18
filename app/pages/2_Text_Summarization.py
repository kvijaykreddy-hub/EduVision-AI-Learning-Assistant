import streamlit as st

from eduvision_ai.services.summarization_service import (
    SummarizationService,
)

st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
)

st.title("📝 Text Summarization")

st.write(
    "Paste a long piece of text and generate a concise summary."
)

text = st.text_area(
    "Enter text:",
    height=300,
    placeholder="Paste your article, notes, or document here...",
)

st.caption(f"Characters: {len(text)}")

service = SummarizationService()

if st.button(
    "Generate Summary",
    type="primary",
    disabled=not text.strip(),
):

    with st.spinner("Generating summary..."):

        try:
            result = service.summarize(text)

            st.success(
                f"Summary generated successfully in "
                f"{result.response_time:.2f} seconds."
            )

            st.caption(f"Model: {result.model}")

            st.markdown("### Summary")

            st.container(border=True).write(result.content)

        except Exception as e:
            st.error(f"Error: {e}")