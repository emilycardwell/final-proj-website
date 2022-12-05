import streamlit as st
import requests
import numpy as np

'''
# Chord Progression Prediction
'''

a = st.text_input("Input 1-12 chords", 'C,D,Em')
b = a.replace(' ', '')

input_chords = f'{b}'

variation = st.slider('How common of a chord progression would you like?', 1, 10, 3)

n_chords = st.selectbox('Select a number of predicted chords.', np.arange(1, 13, 1, 'int'))

'''
---
'''
@st.cache(suppress_st_warning=True)
def call_api(input_chords):
    url = 'https://chords-prog-proj-1-zkfrzn26zq-ew.a.run.app/predict'
    parameters = {'input_chords': input_chords}

    try:
        response = requests.get(url, params=parameters).json()
    except:
        response = st.markdown('**Input Error, _try again_.**')

    return response

if st.button('Get your prediction'):
    st.text(f'Your chord progression: {input_chords}')
    st.text(call_api(input_chords))
    st.balloons()
