import streamlit as st
import json, requests
st.header('Data from Datamuse')
keyword = st.text_input('Please insert a keyword')
criterium = st.selectbox('Please select the criterium you want to use for the search', ('rel_syn=', 'rel_ant=', 'sl=', 'ml='))
url= 'https://api.datamuse.com/words?' + criterium  + keyword + '&max=10'
response = requests.get(url)
dataFromDatamuse = json.loads(response.text)
st.write(dataFromDatamuse)
