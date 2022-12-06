import streamlit as st
import requests
import numpy as np

'''
# Chord Progression Prediction
'''

a = st.text_input("Input 1-12 chords", 'C,D,Em')
b = a.replace(' ', '')

song = f'{b}'

n_chords = st.selectbox('Select a number of predicted chords.', np.arange(1, 13, 1, 'int'))

randomness = st.slider('How common of a chord progression would you like?', 1, 10, 3)


'''
---
'''
@st.cache(suppress_st_warning=True)
def call_api(song, n_chords, randomness):
    url = 'https://chords-progression-prediction-1-zkfrzn26zq-ew.a.run.app/predict'
    parameters = {'song': song, 'n_chords': n_chords, 'randomness': randomness}

    try:
        response = requests.get(url, params=parameters).json()
    except:
        response = 'Input Error, try again'

    return response

if st.button('Get your prediction'):
    st.text(call_api(song, n_chords, randomness))


