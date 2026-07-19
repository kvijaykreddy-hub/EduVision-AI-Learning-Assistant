"""
OCR (Optical Character Recognition) Workspace.
"""

import streamlit as st
from PIL import Image

from eduvision_ai.services.ocr_service import OCRService
from eduvision_ai.services.summarization_service import SummarizationService

st.set_page_config(
    page_title="OCR Workspace",
    page_icon="📄",
)

st.title("📄 OCR Workspace")
st.write(
    "Upload an image, extract text, and use AI to summarize or generate key points."
)

# ============================================================
# Session State
# ============================================================

if "ocr_response" not in st.session_state:
    st.session_state.ocr_response = None

if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

if "ocr_ai_output" not in st.session_state:
    st.session_state.ocr_ai_output = ""

if "ocr_ai_title" not in st.session_state:
    st.session_state.ocr_ai_title = ""

# ============================================================
# Upload Image
# ============================================================

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"],
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True,
    )

    st.divider()

    if st.button(
        "🔍 Extract Text",
        type="primary",
        use_container_width=True,
    ):

        service = OCRService()

        with st.spinner("Extracting text..."):

            try:

                response = service.extract_text(image)

                st.session_state.ocr_response = response
                st.session_state.ocr_text = response.content

                st.session_state.ocr_ai_output = ""
                st.session_state.ocr_ai_title = ""

                st.rerun()

            except Exception as e:

                st.error(f"Error: {e}")

# ============================================================
# Results
# ============================================================

if st.session_state.ocr_response is not None:

    response = st.session_state.ocr_response

    st.success("✅ Text extracted successfully!")

    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Response Time",
            f"{response.response_time:.2f} sec",
        )

    with col2:

        st.metric(
            "Model",
            response.model,
        )

    st.divider()

    # --------------------------------------------------------
    # Extracted Text
    # --------------------------------------------------------

    st.subheader("📄 Extracted Text")

    st.text_area(
        "OCR Output",
        value=st.session_state.ocr_text,
        height=300,
    )

    st.download_button(
        label="⬇ Download Text",
        data=st.session_state.ocr_text,
        file_name="ocr_output.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.divider()

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    st.subheader("📊 Text Statistics")

    text = st.session_state.ocr_text

    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Characters", characters)

    with col2:
        st.metric("Words", words)

    with col3:
        st.metric("Lines", lines)

    st.divider()

    # --------------------------------------------------------
    # AI Actions
    # --------------------------------------------------------

    st.subheader("🤖 AI Actions")

    summary_service = SummarizationService()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🧠 Summarize",
            use_container_width=True,
        ):

            with st.spinner("Generating summary..."):

                try:

                    result = summary_service.summarize(
                        st.session_state.ocr_text,
                        style="paragraph",
                    )

                    st.session_state.ocr_ai_title = "Summary"
                    st.session_state.ocr_ai_output = result.content

                    st.rerun()

                except Exception as e:

                    st.error(f"Error: {e}")

    with col2:

        if st.button(
            "📌 Key Points",
            use_container_width=True,
        ):

            with st.spinner("Generating key points..."):

                try:

                    result = summary_service.summarize(
                        st.session_state.ocr_text,
                        style="bullet",
                    )

                    st.session_state.ocr_ai_title = "Key Points"
                    st.session_state.ocr_ai_output = result.content

                    st.rerun()

                except Exception as e:

                    st.error(f"Error: {e}")

    # --------------------------------------------------------
    # AI Output
    # --------------------------------------------------------

    if st.session_state.ocr_ai_output:

        st.divider()

        st.subheader(f"🤖 {st.session_state.ocr_ai_title}")

        st.markdown(st.session_state.ocr_ai_output)