"""
Image Classification Workspace.
"""

import streamlit as st
from PIL import Image

from eduvision_ai.services.image_classification_service import (
    ImageClassificationService,
)

st.set_page_config(
    page_title="Image Classification",
    page_icon="🖼️",
)

st.title("🖼️ Image Classification")

st.write(
    "Upload an image and let Gemini identify the main object with an explanation."
)

# ============================================================
# Session State
# ============================================================

if "classification_response" not in st.session_state:
    st.session_state.classification_response = None

if "classification_result" not in st.session_state:
    st.session_state.classification_result = ""

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
        "🔍 Classify Image",
        type="primary",
        use_container_width=True,
    ):

        service = ImageClassificationService()

        with st.spinner("Analyzing image..."):

            try:

                response = service.classify(image)

                st.session_state.classification_response = response
                st.session_state.classification_result = response.content

                st.rerun()

            except Exception as e:

                st.error(f"Error: {e}")

# ============================================================
# Results
# ============================================================

if st.session_state.classification_response is not None:

    response = st.session_state.classification_response

    st.success("✅ Image classified successfully!")

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

    st.subheader("🧠 Classification Result")

    st.markdown(st.session_state.classification_result)

    # --------------------------------------------------------

    st.download_button(
        label="⬇ Download Result",
        data=st.session_state.classification_result,
        file_name="classification_result.txt",
        mime="text/plain",
        use_container_width=True,
    )
