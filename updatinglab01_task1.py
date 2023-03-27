import streamlit as st
import json, requests

APIkey = 'b0dc5ff479faf43dff849169f51ad2b0'
location = st.text_input('Gimme a city')

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'

response = requests.get(url)
weatherData = json.loads(response.text)
st.write(weatherData['main']['temp_max'], weatherData['main']['temp_min'],'\n', weatherData['weather'][0]['description'])
