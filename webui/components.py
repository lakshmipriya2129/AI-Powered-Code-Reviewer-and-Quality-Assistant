import streamlit as st
import pandas as pd


def metrics_dashboard(metrics):

    df = pd.DataFrame(metrics)

    st.subheader(" Quality Dashboard")
    st.dataframe(df, use_container_width=True)

    st.bar_chart(
        df.set_index("file")["QualityScore"]
    )


def review_panel(review):

    st.subheader(f"Review: {review.file}")

    st.info(review.summary)

    for issue in review.issues:

        color = {
            "info": "🟢",
            "warning": "🟡",
            "critical": "🔴"
        }[issue.severity]

        st.write(
            f"{color} **{issue.title}** "
            f"(Line {issue.line})"
        )
        st.caption(issue.description)