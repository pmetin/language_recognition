# Language recognition app

This app automatically recognizes the language of a text input and displays statistics about it. The longer the text, the better the prediction. It will suggest a second possible language when appropriate.

It can be used through a Streamlit web interface (*available here, you might have to wake it up though*): 

https://language-recognition.streamlit.app/ 

The app mainly uses the langdetect python library for language prediction: https://pypi.org/project/langdetect/#description 

All dependencies are available in `requirements.txt`:
```
streamlit==1.52.2
langdetect==1.0.9
pandas==2.3.3
matplotlib==3.10.7
```
