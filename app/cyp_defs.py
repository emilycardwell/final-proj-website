from music21 import stream
from music21 import chord
from mingus.core import chords
import os


def get_notes(chords_input):
    array_of_chord = []
    for chord in chords_input:
        array_of_chord.append(chords.from_shorthand(chord))
    return array_of_chord


def convert_chord_into_staff_and_midi_file(chords):
    array_of_chord = get_notes(chords)
    s = stream.Stream()

    for b in array_of_chord:
        c = chord.Chord(b)
        c.duration.quarterLength = 2.0
        s.append(c)

    local_path = os.getcwd()
    filename = "input_chords"
    my_image_file = f'{local_path}/{filename}'
    my_image_file_path = f'{local_path}/{filename}-1.png'
    my_midi_path_file = f'{my_image_file}.midi'
    s.write('midi',fp=my_midi_path_file)
    s.show('musicxml.png',fp=my_image_file,app=False)
    return my_image_file_path,my_midi_path_file



# @st.cache(suppress_st_warning=True)
# def call_api(input_chords):
#     url = 'https://chords-prog-proj-1-zkfrzn26zq-ew.a.run.app/predict'
#     parameters = {'input_chords': input_chords}

#     try:
#         response = requests.get(url, params=parameters).json()
#     except:
#         response = 'Input Error, try again'

#     return response

# if st.button('Get your prediction'):
#     st.text(f'Your chord progression: {input_chords}')
#     st.text(call_api(input_chords))
#     st.text(f'Your chords: {[input_chords]}')
#     image_path_return , midi_path_return = convert_chord_into_staff_and_midi_file(input_chords)
#     st.image(image_path_return)
#     mixer.init()
#     #music = st.file_uploader("Choose a song")
#     wav_file = midi_to_wav(midi_path_return)
#     music2 = open(wav_file,'wav')
#     #audio_bytes = audiofile.read(midi_path_return) #reading the fileaudio_bytes = audio_file.read() #reading the file
# try:
#     mixer.music.load(music2)
# except Exception:
#     st.write("Please choose a song")

#     if st.button("Play"):
#         mixer.music.play()

#     if st.button("Stop"):
#         mixer.music.stop()

#     if st.button("Resume"):
#         mixer.music.unpause()

#     if st.button("Pause"):
#         mixer.music.pause()
