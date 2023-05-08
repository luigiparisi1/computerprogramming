import streamlit as st
import stanza
from googletrans import Translator

translator = Translator()
input_text = st.text_input('Please, insert text here')
dest_lang = st.text_input('Select a language')

if (input_text and dest_lang):
 output_text = translator.translate(input_text, dest=dest_lang)
 st.write(output_text.text)
 analysed_text = (output_text.text)
if dest_lang:
 stanza.download(dest_lang)
 lan_nlp = stanza.Pipeline(f"{dest_lang}")
 text = lan_nlp(analysed_text)
 for i, sent in enumerate(analysed_text.sentences):
    st.write("[Sentence {}]".format(i+1))
    for word in sent.words:
        st.write("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")
else:
 st.write("No language detected")

    

#    import streamlit as st
#from googletrans import Translator
#st.header('Qua si traducono cose')
#translator = Translator()
#word = st.text_input('Scrivi quello che te pare ')
#dest_lang = st.text_input('Dimme na lingua (oppure er codice)')
#if (word and dest_lang) :
#  translation = translator.translate(word, dest = dest_lang )
#  st.write(translation.text)
