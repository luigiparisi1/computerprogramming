import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()

st.title('Translator- Text Analyser')
st.header('Welcome to the slowest and still malfunctioning text analyser ever!')
st.write('''This app allows you to translate and then analyse a text in any language, 
as long as Stanza and Google Translate support it. To use it, just type a text in any language of your
choice. It will be automatically recognized. Then, choose a language. You can write the
name of the language in English or just type the two code-letter (e.g. for Spanish, you 
can either type "Spanish" or "es"). You will have a translation and then you can
walk through the sentences of the translated text. When clicking on a sentence,
you will have clickable single tokens. When clicking them, you will get the lemma and the part
of speech of the desired word.''')

input_text = st.text_area('Please, insert text here')
dest_lang = st.text_input('Enter a language here')

if (input_text and dest_lang):
    try:
      output_text = translator.translate(input_text, dest=dest_lang)
      translated_text = (output_text.text)
      st.write(translated_text)
     
    except ValueError:
      st.info (f"{dest_lang} is not a valid language!")
      text = False
      dest_lang = False
else:
  st.info ("Oops! Something is missing!")

text = False
if (input_text and dest_lang):
  try:
    stanza.download(dest_lang)
    lan_nlp = stanza.Pipeline(f"{dest_lang}", processors = "tokenize, mwt" )
    text = lan_nlp(translated_text)
  except stanza.pipeline.core.UnsupportedProcessorError:
   st.info ("Sorry, this language is not supported.")
   text = False
  
duplicate_avoider = 0
if text:
  for i, sent in enumerate(text.sentences):
    sentence_text = sent.text
    if st.button(f"Sentence {i+1}: {sentence_text}"):
           st.write(f"Sentence {i+1}:")
           for word in sent.words:
            if word.pos == 'PUNCT':
                    continue
            duplicate_avoider += 1
            if st.button(word.text, key = duplicate_avoider):
                st.info(f"Lemma: {word.lemma}; Part of Speech: {word.pos}")
             
    else:
        pass

# PROBLEMI  
# COSE DA CAPIRE (CHIEDERE AL PROF): L'APP LANCIA UN ERRORE OGNI VOLTA CHE NELLA STESSA FRASE INCONTRA UNA PAROLA DUPLICATA (+++RISOLTO+++)
# INVECE DI APRIRE IL BOX CON LE INFO RICHIESTE ALLA LINEA 28 L'APP CHIUDE L'INTERA FRASE (SESSION STATE? COME SI FA?)
# QUANDO GLI DAI IN PASTO UNA LINGUA CHE STANZA NON SUPPORTA, INVECE DI LANCIARE ERRORE DOVREBBE
# USCIRE UN MESSAGGIO CHE TI DICE CHE LA LINGUA NON è SUPPORTATA (+++RISOLTO+++)
# NON VISUALIZZARE IL MESSAGGIO DI ERRORE QUANDO LASCI UNO DEI DUE CAMPI VUOTO (RISOLTO)
# IGNORARE LA PUNTEGGIATURA

# MIGLIORAMENTI DA FARE: INTEGRA UN DIZIONARIO NELLA LINGUA DI DESTINAZIONE, DA MOSTRARE INSIEME AL LEMMA E AL POS
# COME FACCIO A RENDERLA PIù VELOCE? PERò RISPETTO A QUALCHE VERSIONE PRECEDENTE NON CRASHA, ALMENO QUESTO è POSITIVO
# I BOTTONI DELLE PAROLE LI VOGLIO IN ORIZZONTALE

#codice prima di provare il session state
#import streamlit as st
#import stanza
#from googletrans import Translator

#translator = Translator()
#st.header('Welcome to the worst text analyser ever!')
#input_text = st.text_area('Please, insert text here')
#dest_lang = st.text_input('Select a language')

#if (input_text and dest_lang):
 #   try:
  #    output_text = translator.translate(input_text, dest=dest_lang)
   #   st.write(output_text.text)
   #   translated_text = (output_text.text)
   # except ValueError:
    #  st.info (f"{dest_lang} is not a valid language!")
     # text = False
     # dest_lang = False
#else:
 # st.write ("Waiting...")

#if (input_text and dest_lang):
 # try:
  #  stanza.download(dest_lang)
   # lan_nlp = stanza.Pipeline(f"{dest_lang}", processors = "tokenize, mwt" )
    #text = lan_nlp(translated_text)
#  except stanza.pipeline.core.UnsupportedProcessorError:
 #  st.info ("Sorry, this language is not supported by Stanza.")
  # text = False
  
    
#if text != False:
 # for i, sent in enumerate(text.sentences):
  #  sentence_text = sent.text
   # if st.button(f"Sentence {i+1}: {sentence_text}"):
    #       st.write(f"Sentence {i+1}:")
     #      for word in sent.words:
      #       if st.button(word.text):
       #         st.info(f"{word.lemma}\t{word.pos}")
        #     else:
         #      pass
#    else:
 #     pass








    

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
