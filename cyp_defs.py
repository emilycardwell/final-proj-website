from music21 import stream, chord
from mingus.core import chords
import os
from music21 import converter
from music21.musicxml.m21ToXml import ScoreExporter

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

    scex = ScoreExporter(s)
    unused_root = scex.parse()
    xml_string = scex.asBytes().decode('utf-8')
    with open('file.xml', 'w+') as f:
        f.write(xml_string)

    midi_file = s.write('midi', fp=f'{os.getcwd()}/test.midi')
    conv = converter.parse(s.write('midi', fp=f'{os.getcwd()}/test.midi'))
    image_path_return = conv.write('musicxml.png',fp=f'{os.getcwd()}/test')

    return image_path_return
