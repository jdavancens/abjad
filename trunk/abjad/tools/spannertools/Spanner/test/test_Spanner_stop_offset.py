# -*- encoding: utf-8 -*-
from abjad import *


def test_Spanner_stop_offset_01():
    r'''Return stop time of spanner in score.
    '''

    voice = Voice("c'8 d'8 e'8 f'8")
    beam = spannertools.BeamSpanner(voice[1:3])
    glissando = spannertools.GlissandoSpanner([voice])

    r'''
    \new Voice {
        c'8 \glissando
        d'8 [ \glissando
        e'8 ] \glissando
        f'8
    }
    '''

    assert beam.get_timespan().stop_offset == Duration(3, 8)
    assert glissando.get_timespan().stop_offset == Duration(4, 8)
