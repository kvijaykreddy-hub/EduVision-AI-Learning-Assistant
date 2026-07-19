"""
Interactive Quiz Generator Page.
"""

import streamlit as st

from eduvision_ai.services.quiz_service import QuizService
from eduvision_ai.utils.quiz_utils import calculate_score

st.set_page_config(
    page_title="Quiz Generator",
    page_icon="📝",
)

st.title("📝 Quiz Generator")

st.write(
    "Generate an interactive multiple-choice quiz from your study material."
)

# ============================================================
# Session State Initialization
# ============================================================

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "llm_response" not in st.session_state:
    st.session_state.llm_response = None

if "quiz_generated" not in st.session_state:
    st.session_state.quiz_generated = False

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = []

# ============================================================
# Input Section
# ============================================================

study_material = st.text_area(
    "Study Material",
    height=250,
    placeholder="Paste your study notes, textbook content or article here...",
)

difficulty = st.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard",
    ],
)

num_questions = st.slider(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5,
)

service = QuizService()

# ============================================================
# Generate Quiz
# ============================================================

if st.button(
    "Generate Quiz",
    type="primary",
    disabled=not study_material.strip(),
):

    with st.spinner("Generating quiz..."):

        try:

            response, questions = service.generate_quiz(
                text=study_material,
                difficulty=difficulty,
                num_questions=num_questions,
            )

            st.session_state.llm_response = response
            st.session_state.quiz_questions = questions
            st.session_state.quiz_generated = True
            st.session_state.quiz_submitted = False
            st.session_state.score = 0
            st.session_state.user_answers = []

            # Clear previous radio selections
            for key in list(st.session_state.keys()):
                if key.startswith("question_"):
                    del st.session_state[key]

            st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")

# ============================================================
# Display Quiz
# ============================================================

if st.session_state.quiz_generated:

    response = st.session_state.llm_response
    questions = st.session_state.quiz_questions

    st.success(
        f"Quiz generated successfully in "
        f"{response.response_time:.2f} seconds."
    )

    st.caption(f"Model: {response.model}")

    st.divider()

    user_answers = []

    for index, question in enumerate(questions):

        with st.container(border=True):

            st.markdown(f"### Question {index + 1}")

            st.write(question.question)

            selected = st.radio(
                "Choose your answer:",
                question.options,
                key=f"question_{index}",
                disabled=st.session_state.quiz_submitted,
            )

            user_answers.append(
                question.options.index(selected)
            )

    st.session_state.user_answers = user_answers

    st.info(
        "Answer all questions and click **Submit Quiz**."
    )

# ============================================================
# Submit Quiz
# ============================================================

    if st.button(
        "Submit Quiz",
        type="primary",
    ):

        score = calculate_score(
            questions,
            user_answers,
        )

        st.session_state.score = score
        st.session_state.quiz_submitted = True

        st.rerun()

# ============================================================
# Results Section
# (Continues in Part B)
# ============================================================
# ============================================================
# Results Dashboard
# ============================================================

    if st.session_state.quiz_submitted:

        score = st.session_state.score

        total = len(questions)

        percentage = (score / total) * 100

        st.divider()

        st.success("🏆 Quiz Completed!")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Score",
                f"{score}/{total}",
            )

        with col2:
            st.metric(
                "Correct",
                score,
            )

        with col3:
            st.metric(
                "Accuracy",
                f"{percentage:.0f}%",
            )

        st.progress(percentage / 100)

        st.divider()

        st.subheader("📋 Quiz Review")

        for index, question in enumerate(questions):

            user_answer = st.session_state.user_answers[index]

            correct = (
                user_answer == question.answer
            )

            with st.container(border=True):

                if correct:

                    st.success(
                        f"✅ Question {index + 1}"
                    )

                    st.write(question.question)

                    st.markdown(
                        f"**Your Answer:** "
                        f"{question.options[user_answer]}"
                    )

                else:

                    st.error(
                        f"❌ Question {index + 1}"
                    )

                    st.write(question.question)

                    st.markdown(
                        f"**Your Answer:** "
                        f"{question.options[user_answer]}"
                    )

                    st.markdown(
                        f"**Correct Answer:** "
                        f"{question.options[question.answer]}"
                    )

                st.info(question.explanation)

# ============================================================
# Action Buttons
# ============================================================

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            if st.button("🔄 Try Again"):

                st.session_state.quiz_submitted = False
                st.session_state.score = 0

                for i in range(len(questions)):
                    key = f"question_{i}"
                    if key in st.session_state:
                        del st.session_state[key]

                st.rerun()

        with col2:

            if st.button("📝 Generate New Quiz"):

                st.session_state.quiz_questions = []
                st.session_state.llm_response = None
                st.session_state.quiz_generated = False
                st.session_state.quiz_submitted = False
                st.session_state.user_answers = []
                st.session_state.score = 0

                for key in list(st.session_state.keys()):
                    if key.startswith("question_"):
                        del st.session_state[key]

                st.rerun()