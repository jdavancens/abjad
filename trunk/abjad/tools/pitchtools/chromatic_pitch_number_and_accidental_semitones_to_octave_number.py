# -*- encoding: utf-8 -*-
import math


def chromatic_pitch_number_and_accidental_semitones_to_octave_number(
    chromatic_pitch_number, accidental_semitones):
    '''Change `chromatic_pitch_number` and `accidental_semitones` to octave number:

    ::

        >>> pitchtools.chromatic_pitch_number_and_accidental_semitones_to_octave_number(12, -2)
        5

    Return integer.
    '''

    return int(math.floor((chromatic_pitch_number - accidental_semitones) / 12)) + 4
