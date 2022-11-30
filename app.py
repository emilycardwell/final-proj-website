import streamlit as st
import requests

'''
# Chord Prediction Front
'''
columns = st.columns(3)
a = columns[0].text_input("Input Chord 1", 'C')
b = columns[0].text_input("Input Chord 2", 'A7')
c = columns[0].text_input("Input Chord 3", 'F')

d = a + "-" + b + "-" + c


'''
## Prediction
'''
@st.cache
def call_api(chords):
    url = 'https://final-project-api-zkfrzn26zq-ue.a.run.app/predict'
    parameters = {'chords': chords}

    response = requests.get(url, params=parameters)
    return response.json()

st.text(f'your chord progression: {d}...')
st.text(call_api(d))
