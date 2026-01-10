import streamlit as st
import pandas as pd
from lang_detection import display_lang
from statistics import compute_stats, visualize_stats, top_words

# Implementation of functions from statistics.py and lang_detection.py in a Streamlit interface
st.title("Language recognition and statistics")

# main input : text that will be analyzed
text_input = st.text_area("Enter your text here: \n\n*Tip: don't forget the final dot.*")

# check whether text input exists
if text_input.strip():
    # apply and display language detection functions
    result = display_lang(text_input)
    st.success(result)
    # statistics section
    # apply and display statistic analysis
    st.subheader("Statistics")
    stats = compute_stats(text_input)
    stats_df = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
    st.dataframe(stats_df, hide_index=True)
    # visualization section
    # display statistics visually
    st.subheader("Visualization")
    fig = visualize_stats(stats)
    st.pyplot(fig)
    # top words section
    st.subheader("Top words")
    # slider to choose the number of top words dynamically
    n = st.slider("Select the number of top words to compute", min_value=1, max_value=20, value=10)
    top_words_df = top_words(text_input, n)
    st.dataframe(top_words_df, hide_index=True)