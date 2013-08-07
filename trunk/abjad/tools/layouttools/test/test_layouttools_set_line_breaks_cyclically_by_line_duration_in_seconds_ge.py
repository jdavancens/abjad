# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import layouttools


def test_layouttools_set_line_breaks_cyclically_by_line_duration_in_seconds_ge_01():
    r'''Iterate line-break class instances in expr and 
    accumulate duration in seconds.
    Add line break after every total less than or equal to line_duration.
    '''

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    contexttools.TempoMark(Duration(1, 8), 44, target_context = Staff)(staff)
    measuretools.set_always_format_time_signature_of_measures_in_expr(staff)

    r'''
    \new Staff {
        \tempo 8=44
        {
            \time 2/8
            c'8
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    layouttools.set_line_breaks_cyclically_by_line_duration_in_seconds_ge(staff, Duration(6))

    r'''
    \new Staff {
        \tempo 8=44
        {
            \time 2/8
            c'8
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
            \break
        }
        {
            \time 2/8
            g'8
            a'8
        }
        {
            \time 2/8
            b'8
            c''8
        }
    }
    '''

    assert select(staff).is_well_formed()
    assert testtools.compare(
        staff.lilypond_format,
        r'''
        \new Staff {
            \tempo 8=44
            {
                \time 2/8
                c'8
                d'8
            }
            {
                \time 2/8
                e'8
                f'8
                \break
            }
            {
                \time 2/8
                g'8
                a'8
            }
            {
                \time 2/8
                b'8
                c''8
            }
        }
        '''
        )
