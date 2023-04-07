import streamlit as st
from googletrans import Translator
st.header('This is my beautiful translator')
translator = Translator()
word = st.text_input('Gimme a word')
dest_lang = st.text_input('Gimme any language')
# if (word and dest_lang): dovrei metterlo ma non capisco perché
translation = translator.translate(word, dest = dest_lang )
st.write(translation.text)
