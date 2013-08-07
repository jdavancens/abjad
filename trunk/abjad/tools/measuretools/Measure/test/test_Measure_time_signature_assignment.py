# -*- encoding: utf-8 -*-
from abjad import *


def test_Measure_time_signature_assignment_01():
    r'''Measures allow timesignature reassignment.
    '''

    measure = Measure((4, 8), "c'8 d'8 e'8 f'8")

    r'''
    {
        \time 4/8
        c'8
        d'8
        e'8
        f'8
    }
    '''

    measure.pop()
    measure.select().detach_marks(contexttools.TimeSignatureMark)
    contexttools.TimeSignatureMark((3, 8))(measure)

    r'''
    {
        \time 3/8
        c'8
        d'8
        e'8
    }
    '''

    assert testtools.compare(
        measure.lilypond_format,
        r'''
        {
            \time 3/8
            c'8
            d'8
            e'8
        }
        '''
        )
