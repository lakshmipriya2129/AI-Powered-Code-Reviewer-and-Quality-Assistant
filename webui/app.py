import streamlit as st
from utils import extract_project, run_full_analysis
from components import metrics_dashboard, review_panel
from diff_view import show_diff

from ai_review.reviewer import AIReviewer

st.set_page_config(
    page_title="CodeGuard AI Reviewer",
    layout="wide"
)

st.title(" AI Powered Code Reviewer")

uploaded = st.file_uploader(
    "Upload Project ZIP",
    type=["zip"]
)

if uploaded:

    project_path = extract_project(uploaded)

    if st.button(" Analyze Project"):

        with st.spinner("Running AI Analysis..."):

            files, analyses, reviews, metrics = \
                run_full_analysis(project_path)

        st.session_state["files"] = files
        st.session_state["reviews"] = reviews
        st.session_state["metrics"] = metrics
        st.success("Analysis Complete")

# ===========================
# DASHBOARD
# ===========================
if "metrics" in st.session_state:

    tabs = st.tabs([
        "Dashboard",
        "AI Review",
        "Auto Fix & Diff"
    ])

    # ---------------------
    # Dashboard
    # ---------------------
    with tabs[0]:
        metrics_dashboard(
            st.session_state["metrics"]
        )

    # ---------------------
    # Review
    # ---------------------
    with tabs[1]:

        for review in \
            st.session_state["reviews"]:
            review_panel(review)

    # ---------------------
    # Auto Fix + Diff
    # ---------------------
    with tabs[2]:

        reviewer = AIReviewer()

        selected = st.selectbox(
            "Select File",
            st.session_state["files"]
        )

        if st.button("Apply AI Fix"):

            with open(selected) as f:
                original = f.read()

            fixed = reviewer.auto_fix(
                selected
            )

            show_diff(original, fixed)