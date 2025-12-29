import streamlit as st
from language_recognition import display_lang

st.title("Language recognition")

text_input = st.text_area("Write text here: ")

if st.button("Detect language"):
    result = display_lang(text_input)
    st.success(result)