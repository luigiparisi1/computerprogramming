import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()
st.header('Welcome to the worst text analyser ever!')
input_text = st.text_area('Please, insert text here')
dest_lang = st.text_input('Select a language')

if (input_text and dest_lang):
 output_text = translator.translate(input_text, dest=dest_lang)
 st.write(output_text.text)
 analysed_text = (output_text.text)
else:
 st.write ("Waiting...")
if (input_text and dest_lang):
 stanza.download(dest_lang)
 lan_nlp = stanza.Pipeline(f"{dest_lang}", processors = "tokenize, mwt" )
 text = lan_nlp(analysed_text)

if input_text:
 for i, sent in enumerate(text.sentences):
  sentence_text = sent.text
  if st.button(f"Sentence {i+1}: {sentence_text}"):
            st.write(f"Sentence {i+1}:")
            for word in sent.words:
             if st.button(word.text):
                st.info(f"{word.lemma}\t{word.pos}", icon = 'i')
             else:
              pass
  else:
    pass
else:
    st.write("No language selected.")
  
# COSE DA CAPIRE (CHIEDERE AL PROF): L'APP LANCIA UN ERRORE OGNI VOLTA CHE NELLA STESSA FRASE INCONTRA UNA PAROLA DUPLICATA
# INVECE DI APRIRE IL BOX CON LE INFO RICHIESTE ALLA LINEA 28 L'APP CHIUDE L'INTERA FRASE

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
