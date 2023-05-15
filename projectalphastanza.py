import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()
st.header('Welcome to the worst text analyser ever!')
input_text = st.text_area('Please, insert text here')
dest_lang = st.text_input('Select a language')

if (input_text and dest_lang):
  try:
    output_text = translator.translate(input_text, dest=dest_lang)
    st.write(output_text.text)
    translated_text = (output_text.text)
  except ValueError:
    st.info (f"{dest_lang} is not a valid language!"}
    
else:
  st.write ("Waiting...")

if (input_text and dest_lang):
  try:
    stanza.download(dest_lang)
    lan_nlp = stanza.Pipeline(f"{dest_lang}", processors = "tokenize, mwt" )
    text = lan_nlp(translated_text)
  except stanza.pipeline.core.UnsupportedProcessorError:
   st.info ("Sorry, this language is not supported by Stanza.")
   text = False
  except ValueError:
    st.info(f"{dest_lang} is not a valid language!")
    
if text != False:
  for i, sent in enumerate(text.sentences):
    sentence_text = sent.text
    if st.button(f"Sentence {i+1}: {sentence_text}"):
           st.write(f"Sentence {i+1}:")
           for word in sent.words:
             if st.button(word.text):
                st.info(f"{word.lemma}\t{word.pos}")
             else:
               pass
    else:
      pass

  
# COSE DA CAPIRE (CHIEDERE AL PROF): L'APP LANCIA UN ERRORE OGNI VOLTA CHE NELLA STESSA FRASE INCONTRA UNA PAROLA DUPLICATA
# INVECE DI APRIRE IL BOX CON LE INFO RICHIESTE ALLA LINEA 28 L'APP CHIUDE L'INTERA FRASE
# QUANDO GLI DAI IN PASTO UNA LINGUA CHE STANZA NON SUPPORTA, INVECE DI LANCIARE ERRORE DOVREBBE USCIRE UN MESSAGGIO CHE TI DICE CHE LA LINGUA NON è SUPPORTATA

# MIGLIORAMENTI DA FARE: INTEGRA UN DIZIONARIO NELLA LINGUA DI DESTINAZIONE, DA MOSTRARE INSIEME AL LEMMA E AL POS
# COME FACCIO A RENDERLA PIù VELOCE? PERò RISPETTO A QUALCHE VERSIONE PRECEDENTE NON CRASHA, ALMENO QUESTO è POSITIVO









    

#    import streamlit as st
#from googletrans import Translator
#st.header('Qua si traducono cose')
#translator = Translator()
#word = st.text_input('Scrivi quello che te pare ')
#dest_lang = st.text_input('Dimme na lingua (oppure er codice)')
#if (word and dest_lang) :
#  translation = translator.translate(word, dest = dest_lang )
#  st.write(translation.text)
# for i, sent in enumerate(text.sentences):
 #   st.write("[Sentence {}]".format(i+1))
 #  for word in sent.words:
 #       st.write("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
  #            word.text, word.lemma, word.pos, word.head, word.deprel))
#else:
# st.write("No language detected")
