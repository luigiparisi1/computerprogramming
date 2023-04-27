import nltk
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
    
    if text:
        words = word_tokenize(text)
        for word in words:
            if st.button(word):
                show_word_info(word)

if __name__ == "__main__":
    main()
