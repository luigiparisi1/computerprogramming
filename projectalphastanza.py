import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()
input_text = st.text_input('Please, insert text here')
dest_lang = st.text_input('Please, choose any language')

if input_text and dest_lang:
  output_text = translator.translate(input_text, dest=dest_lang)
  st.write(output_text.text)

if dest_lang:
  stanza.download(dest_lang)
else:
  st.write("No language detected")

lan_nlp = stanza.Pipeline("{dest_lang}")

                         
    

#    import streamlit as st
#from googletrans import Translator
#st.header('Qua si traducono cose')
#translator = Translator()
#word = st.text_input('Scrivi quello che te pare ')
#dest_lang = st.text_input('Dimme na lingua (oppure er codice)')
#if (word and dest_lang) :
#  translation = translator.translate(word, dest = dest_lang )
#  st.write(translation.text)
