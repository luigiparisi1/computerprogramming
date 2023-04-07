import streamlit as st
from googletrans import Translator
st.header('Aoh, qua si traducono cose')
translator = Translator()
word = st.text_input('Scrivi quello che te pare ')
dest_lang = st.text_input('Dimme na lingua (oppure er codice)')
if (word and dest_lang) :
  translation = translator.translate(word, dest = dest_lang )
  st.write(translation.text)
