import streamlit as st
import json, requests
st.header('Data from Datamuse')
keyword = st.text_input('Please insert a keyword')
criterium = st.selectbox('Please select the criterium you want to use for the search', ('Synonims', 'Antonyms', 'Sounds like', 'Means like'))
if criterium = 'Synonims':
  key = 'rel_syn='
elif criterium = 'Antynoms':
  key = 'rel_ant='
elif criterium = 'Sounds like':
  key = 'sl='
elif criterium = 'Means like':
  key = 'ml='
else:
  pass
url= 'https://api.datamuse.com/words?' + key  + keyword + '&max=10'
response = requests.get(url)
dataFromDatamuse = json.loads(response.text)
st.write(dataFromDatamuse)
