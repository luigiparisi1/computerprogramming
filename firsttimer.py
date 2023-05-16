import streamlit as st
import stanza
stanza.download("it")
it_nlp =  stanza.Pipeline('it')
text = st.write("inserisci frase qui")
if text:
    sentence = it_nlp(text)
    for i, sent in enumerate(sentence.sentences):
    st.write("[Sentence {}]".format(i+1))
    for word in sent.words:
        st.info("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")
