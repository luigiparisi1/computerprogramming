import streamlit as st
from googletrans import Translator
st.header('This is my beautiful translator')
translator = Translator()
word = st.text_input('Gimme a word\t')
dest_lang = st.selectbox('Select a language', ('German', 'Russian', 'Greek'))
if (word and dest_lang):
  translation = translator.translate(word, dest = dest_lang )
  st.write(translation.text)
