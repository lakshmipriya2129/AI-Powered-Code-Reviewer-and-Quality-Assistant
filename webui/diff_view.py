import difflib
import streamlit as st


def show_diff(original, modified):

    diff = difflib.HtmlDiff().make_table(
        original.splitlines(),
        modified.splitlines(),
        fromdesc="Original",
        todesc="AI Fixed",
        context=True
    )

    st.components.v1.html(
        diff,
        height=600,
        scrolling=True
    )