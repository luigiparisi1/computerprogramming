import nltk
from googletrans import Translator
translator = Translator()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import streamlit as st
import nltk
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

def get_word_definition(word):
    synset = wordnet.synsets(word)
    if len(synset) > 0:
        definition = synset[0].definition()
        return definition
    else:
        return None

def get_word_pos(word):
    pos = pos_tag(word_tokenize(word))
    return pos[0][1]

def show_word_info(word):
    definition = get_word_definition(word)
    pos = get_word_pos(word)
    if definition is not None:
        st.info(f"{word} ({pos}): {definition}")
    else:
        st.info(f"{word} ({pos}): Definition not found.")

def main():
    text = st.text_input("Inserisci il testo")
    dest_lang = st.text_input('Inserisci una lingua di destinazione')
    
    if text and dest_lang:
        translation = translator.translate(text, dest = dest_lang)
        words = word_tokenize(translation.text)
        for word in words:
            if st.button(word):
                show_word_info(word)

if __name__ == "__main__":
    main()
    
    
#    import streamlit as st
#from googletrans import Translator
#st.header('Qua si traducono cose')
#translator = Translator()
#word = st.text_input('Scrivi quello che te pare ')
#dest_lang = st.text_input('Dimme na lingua (oppure er codice)')
#if (word and dest_lang) :
#  translation = translator.translate(word, dest = dest_lang )
#  st.write(translation.text)
