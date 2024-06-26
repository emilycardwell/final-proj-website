import streamlit as st
import requests
import base64
import numpy as np
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px



# Background Image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('pics/vintage-2721099_1280_2.jpeg')

# website title
new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">Chord Progression Prediction</p>'
st.markdown(new_title, unsafe_allow_html=True)

# Input chords
new_text = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">Input 1 - 12 chords (4 or more for best results)</p>'
st.markdown(new_text, unsafe_allow_html=True)
chords_input = st.text_input("Input 1-12 chords (4 or more for best results)", 'C, Dm, G7, C', label_visibility="collapsed")
b = chords_input.replace(' ', '')
song = f'{b}'

# select number of chords to predict
new_text1 = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">Select a number of predicted chords.</p>'
st.markdown(new_text1, unsafe_allow_html=True)
n_chords = st.selectbox('Select a number of predicted chords.', np.arange(1, 5, 1, 'int'), index=0, label_visibility="collapsed")

# randomness slider
new_text2 = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">Choose a random factor:</p>'
st.markdown(new_text2, unsafe_allow_html=True)
new_text2_1 = '<p style="font-family:sans-serif; color:Black; font-size: 12px;">Changes hyperparameters for new result</p>'
st.markdown(new_text2_1, unsafe_allow_html=True)
randomness = st.slider('Pick the level of randomness:', 1, 10, 2, label_visibility="collapsed")
'''
---
'''
# call API
@st.cache_data
def call_api(song, n_chords, randomness):
    url = 'https://chords-progression-prediction-1-zkfrzn26zq-ew.a.run.app/predict'
    parameters = {'song': song, 'n_chords': n_chords, 'randomness': randomness}

    try:
        response = requests.get(url, params=parameters).json()
    except:
        response = 'Input Error, try again'

    return response

if st.button('Get your prediction'):
    new_text3 = '<p style="font-family:sans-serif; color:Red; font-size: 24px;">New chord(s):</p>'
    st.markdown(new_text3, unsafe_allow_html=True)
    try:
        chord_string = ', '.join(list(call_api(song, n_chords, randomness)["predicted_chord"])[-n_chords:])
        new_text4 = f'<p style="font-family:sans-serif; color:Black; font-size: 20px;">{chord_string}</p>'
        st.markdown(new_text4, unsafe_allow_html=True)
    except TypeError:
        st.markdown('Chord Input Error, try again (maybe you missed a comma?)')

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Created by Emily Cardwell  |  ",
        link("https://emilycardwell.com", "emilycardwell.com"),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
