import nltk
from googletrans import Translator
translator = Translator()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
@@ -29,12 +31,25 @@ def show_word_info(word):

def main():
    text = st.text_input("Inserisci il testo")
    dest_lang = st.text_input('Inserisci una lingua di destinazione')

    if text:
        words = word_tokenize(text)
    if text and dest_lang:
        translation = translator.translate(text, dest = dest_lang)
        words = word_tokenize(translation)
        for word in words:
            if st.button(word):
                show_word_info(word)

if __name__ == "__main__":
    main()
