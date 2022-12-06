import streamlit as st
from pygame import mixer
import requests
import numpy as np
from music21 import stream
from music21 import chord
from mingus.core import chords
import os



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def get_notes(chords_input):
    array_of_chord = []
    for chord in chords_input:
        array_of_chord.append(chords.from_shorthand(chord))
    return array_of_chord


def convert_chord_into_staff_and_midi_file(chords):
    array_of_chord = get_notes(chords)
    s = stream.Stream()

    for i, b in enumerate(array_of_chord):
        c = chord.Chord(b)
        c.duration.quarterLength = 2.0
        s.append(c)

    local_path = os.getcwd()
    filename = "input_chords"
    #midi_file = s.write('midi',fp=f'{local_path}/{filename}.midi')
    my_image_file = f'{local_path}/{filename}'
    my_image_file_path = f'{local_path}/{filename}-1.png'
    #s = converter.parse(midi_file)
    my_midi_path_file = f'{my_image_file}.midi'
    my_midi_file = s.write('midi',fp=my_midi_path_file)
    s.show('musicxml.png',fp=my_image_file,app=False)
    return my_image_file_path,my_midi_path_file


def midi_to_wav(midi_file):
    local_path = os.getcwd()
    filename = "input_chords"
    wav_file = midi_file.replace('.midi', '.wav')
    wav_path_dir = f'{local_path}/{filename}'
    wav_path_file = f'{wav_path_dir}.wav'
    return wav_path_file

#image = Image.open('images/wagon.png')
#st.image(image, caption='Le Wagon', use_column_width=False)
'''
# Chord Progression Prediction
'''

a = st.text_input("Input 1-12 chords", 'C,D,Em')
b = a.replace(' ', '')
print(b)
input_chords = f'{b}'
input_chords = [x.strip() for x in b.split(',')]



#if st.button('Get it converted into a stream'):
    #st.text(f'Your chords: {[input_chords]}')
    #image_path_return , midi_path_return = convert_chord_into_staff_and_midi_file(input_chords)
    #st.image(image_path_return)

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
        response = 'Input Error, try again'

    return response

if st.button('Get your prediction'):
    st.text(f'Your chord progression: {input_chords}')
    st.text(call_api(input_chords))
    st.text(f'Your chords: {[input_chords]}')
    image_path_return , midi_path_return = convert_chord_into_staff_and_midi_file(input_chords)
    st.image(image_path_return)
    mixer.init()
    #music = st.file_uploader("Choose a song")
    wav_file = midi_to_wav(midi_path_return)
    music2 = open(wav_file,'wav')
    #audio_bytes = audiofile.read(midi_path_return) #reading the fileaudio_bytes = audio_file.read() #reading the file
try:
    mixer.music.load(music2)
except Exception:
    st.write("Please choose a song")

    if st.button("Play"):
        mixer.music.play()

    if st.button("Stop"):
        mixer.music.stop()

    if st.button("Resume"):
        mixer.music.unpause()

    if st.button("Pause"):
        mixer.music.pause()
