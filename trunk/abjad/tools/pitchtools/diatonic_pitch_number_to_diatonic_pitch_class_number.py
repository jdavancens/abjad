# -*- encoding: utf-8 -*-
def diatonic_pitch_number_to_diatonic_pitch_class_number(diatonic_pitch_number):
    '''Change `diatonic_pitch_number` to diatonic pitch-class number:

    ::

        >>> pitchtools.diatonic_pitch_number_to_diatonic_pitch_class_number(7)
        0

    Return nonnegative integer.
    '''
    from abjad.tools import pitchtools

    if not pitchtools.is_diatonic_pitch_number(diatonic_pitch_number):
        raise TypeError

    return diatonic_pitch_number % 7
