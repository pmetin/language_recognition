import streamlit as st
from lang_detection import display_lang
from statistics import compute_stats, visualize_stats

st.title("Language recognition")

with st.form(key="my_form"):
    text_input = st.text_area("Enter your text here: ")
    submit_button = st.form_submit_button("Detect language")

    if submit_button and len(text_input) > 0:
        result = display_lang(text_input)
        st.success(result)

        stats = compute_stats(text_input)
        # st.dataframe(pd.DataFrame(stats.items(), columns=["Metric", "Value"]))
        st.subheader("Statistics")
        st.write(stats)
        st.subheader("Visualization")
        fig = visualize_stats(stats)
        st.pyplot(fig)