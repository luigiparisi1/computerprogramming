import streamlit as st
import json, requests
keyword = st.text_input('Please insert a keyword')
criterium = st.selectbox('Please select the criterium you want to use for the search', ('Synonims', 'Antonyms', 'Sounds like', 'Means like'))
'Synonims' = rel_syn=
'Antonyms' = rel_ant=
'Sounds like' = sl=
'Means like' = ml=
url= 'https://api.datamuse.com/words? + criterium  + keyword + '&max=10'
response = requests.get(url)
dataFromDatamuse = json.loads(response.text)
st.write(dataFromDatamuse)
