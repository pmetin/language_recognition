import streamlit as st
import pandas as pd
from lang_detection import display_lang
from statistics import compute_stats, visualize_stats, top_words

st.title("Language recognition and statistics")

text_input = st.text_area("Enter your text here: ")

if text_input.strip():
    result = display_lang(text_input)
    st.success(result)
    st.subheader("Statistics")
    stats = compute_stats(text_input)
    stats_df = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
    st.dataframe(stats_df, hide_index=True)
    st.subheader("Visualization")
    fig = visualize_stats(stats)
    st.pyplot(fig)
    st.subheader("Top words")
    n = st.slider("Select the number of top words to compute", min_value=1, max_value=20, value=10)
    top_words_df = top_words(text_input, n)
    st.dataframe(top_words_df, hide_index=True)