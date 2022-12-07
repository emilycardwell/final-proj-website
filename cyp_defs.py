from music21 import stream, chord
from mingus.core import chords
#import music21 as m21
#from music21 import converter, configure
# from music21.musicxml.m21ToXml import ScoreExporter

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

    return s.show()

