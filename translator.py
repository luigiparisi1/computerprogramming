import streamlit as st
from googletrans import Translator
translator = Translator()
word = st.text_input('Gimme a word\t')
while word != 'quit':
  translation = translator.translate(word, dest = st.text_input('Gimme a language using the first two letters\t'))
  st.write(translation.text)
  word = st.text_input('Gimme another one. If you don\'t want another word to be translated, type "quit"\t')
