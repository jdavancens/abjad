# -*- encoding: utf-8 -*-
from abjad import *


def test_Parentage__get_governor_01( ):
    r'''Return the last sequential container in the parentage of client
    such that the next element in the parentage of client is
    either a parallel container or None.
    '''

    voice = Voice([Container(Voice(notetools.make_repeated_notes(2)) * 2)])
    voice[0].is_parallel = True
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    voice[0][0].name = 'voice 1'
    voice[0][1].name = 'voice 2'

    r'''
    \new Voice {
        <<
            \context Voice = "voice 1" {
                c'8
                d'8
            }
            \context Voice = "voice 2" {
                e'8
                f'8
            }
        >>
    }
    '''

    assert voice.select_leaves()[0].select_parentage()._get_governor() is voice[0][0]
    assert voice.select_leaves()[1].select_parentage()._get_governor() is voice[0][0]
    assert voice.select_leaves()[2].select_parentage()._get_governor() is voice[0][1]
    assert voice.select_leaves()[3].select_parentage()._get_governor() is voice[0][1]


def test_Parentage__get_governor_02( ):
    r'''Unicorporated leaves have no governor.
    '''

    note = Note(0, (1, 8))
    assert note.select_parentage()._get_governor() is None


def test_Parentage__get_governor_03( ):
    r'''Return the last sequential container in the parentage of client
        such that the next element in the parentage of client is
        either a parallel container or None.'''

    staff = Staff([Voice([Container("c'8 d'8 e'8 f'8")])])

    r'''
    \new Staff {
        \new Voice {
            {
                c'8
                d'8
                e'8
                f'8
            }
        }
    }
    '''

    assert staff.select_leaves()[0].select_parentage()._get_governor() is staff
    assert staff.select_leaves()[1].select_parentage()._get_governor() is staff
    assert staff.select_leaves()[2].select_parentage()._get_governor() is staff
    assert staff.select_leaves()[3].select_parentage()._get_governor() is staff


def test_Parentage__get_governor_04( ):
    r'''Return the last sequential container in the parentage of client
    such that the next element in the parentage of client is
    either a parallel container or None.
    '''

    t = Staff([Voice([Container("c'8 d'8 e'8 f'8")])])

    r'''
    \new Staff {
        \new Voice {
            {
                c'8
                d'8
                e'8
                f'8
            }
        }
    }
    '''

    assert t[0][0].select_parentage()._get_governor() is t
    assert t[0].select_parentage()._get_governor() is t
    assert t.select_parentage()._get_governor() is t
