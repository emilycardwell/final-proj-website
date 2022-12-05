import streamlit as st
import requests

'''
# Chord Prediction Front
'''
columns = st.columns(4)
a = columns[0].text_input("Input Chord 1", 'C')
b = columns[1].text_input("Input Chord 2", 'G')
c = columns[2].text_input("Input Chord 3", 'C')
d = columns[3].text_input("Input Chord 4", 'G')
st.text('Optional:')
e = columns[0].text_input("Input Chord 5", '')
f = columns[1].text_input("Input Chord 6", '')
g = columns[2].text_input("Input Chord 7", '')
h = columns[3].text_input("Input Chord 8", '')


input_chords = f'{a},{b},{c},{d}'
if e != '':
    input_chords = input_chords + f',{e},{f},{g},{h}'


'''
## Prediction
'''
@st.cache
def call_api(input_chords):
    url = 'https://chords-prog-proj-1-zkfrzn26zq-ew.a.run.app/predict'
    parameters = {'input_chords': input_chords}

    response = requests.get(url, params=parameters)
    return response.json()

st.text(f'Your chord progression: {input_chords}')
st.text(call_api(input_chords))
