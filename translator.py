import streamlit as st
from googletrans import Translator
translator = Translator()
word = st.text_input('Gimme a word\t')
  translation = translator.translate(word, dest = st.text_input('Gimme a language using the first two letters\t'))
  st.write(translation.text)
