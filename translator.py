import streamlit as st
from googletrans import Translator
translator = Translator()
word = st.text_input('Gimme a word\t')
dest_lang = st.text_input('Gimme a language using the first two letters\t')
if (word and dest_lang):
  translation = translator.translate(word, dest = dest_lang )
  st.write(translation.text)
