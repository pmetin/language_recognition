import streamlit as st
import pandas as pd
from lang_detection import display_lang
from statistics import compute_stats, visualize_stats

st.title("Language recognition")

with st.form(key="my_form"):
    text_input = st.text_area("Enter your text here: ")
    submit_button = st.form_submit_button("Detect language")

    if submit_button and len(text_input) > 0:
        result = display_lang(text_input)
        st.success(result)
        st.subheader("Statistics")
        stats = compute_stats(text_input)
        df = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
        st.dataframe(df, hide_index=True)
        st.subheader("Visualization")
        fig = visualize_stats(stats)
        st.pyplot(fig)