import streamlit as st
from lang_detection import display_lang

st.title("Language recognition")

with st.form(key="my_form"):
    text_input = st.text_area("Enter your text here: ")
    submit_button = st.form_submit_button("Detect language")

    if submit_button:
        result = display_lang(text_input)
        st.success(result)