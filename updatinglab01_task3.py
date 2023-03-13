import streamlit as st
import json, requests

APIkey = 'b0dc5ff479faf43dff849169f51ad2b0'
location = st.radio('Which city do you want to know the weather of?', ('Padova', 'Bressanone', 'Niscemi'))

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric' + '&lang=it'

response = requests.get(url) 
weatherData = json.loads(response.text)
st.write('La temperatura massima a', location, 'è di', weatherData['main']['temp_max'],'°C, la temperatura minima è di', weatherData['main']['temp_min'], '°C.')
st.write('Le condizioni sono di', weatherData['weather'][0]['description'])
