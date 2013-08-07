# -*- encoding: utf-8 -*-
from abjad import *


def test_componenttools_partition_components_by_durations_exactly_01():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    contexttools.TempoMark(Duration(1, 4), 60, target_context=Staff)(staff)

    r'''
    \new Staff {
            \time 2/8
            \tempo 4=60
            c'8
            d'8
            \time 2/8
            e'8
            f'8
            \time 2/8
            g'8
            a'8
            \time 2/8
            b'8
            c''8
            %% tempo 4=60 ends here
    }
    '''

    parts = componenttools.partition_components_by_durations_exactly(
        staff.select_leaves(), [1.5], cyclic=True, in_seconds=True, overhang=False)

    "[[Note(c'', 8), Note(b', 8), Note(a', 8)], [Note(g', 8), Note(f', 8), Note(e', 8)]]"

    assert len(parts) == 2
    assert parts[0] == list(staff.select_leaves()[:3])
    assert parts[1] == list(staff.select_leaves()[3:6])


def test_componenttools_partition_components_by_durations_exactly_02():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    contexttools.TempoMark(Duration(1, 4), 60, target_context = Staff)(staff)

    r'''
    \new Staff {
            \time 2/8
            \tempo 4=60
            c'8
            d'8
            \time 2/8
            e'8
            f'8
            \time 2/8
            g'8
            a'8
            \time 2/8
            b'8
            c''8
            %% tempo 4=60 ends here
    }
    '''

    parts = componenttools.partition_components_by_durations_exactly(
        staff.select_leaves(), [1.5], cyclic=True, in_seconds=True, overhang=True)

    "[[Note(c'', 8), Note(b', 8), Note(a', 8)], "
    "[Note(g', 8), Note(f', 8), Note(e', 8)], "
    "[Note(d', 8), Note(c', 8)]]"

    assert len(parts) == 3
    assert parts[0] == list(staff.select_leaves()[:3])
    assert parts[1] == list(staff.select_leaves()[3:6])
    assert parts[2] == list(staff.select_leaves()[6:8])


def test_componenttools_partition_components_by_durations_exactly_03():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)

    r'''
    \new Staff {
            \time 2/8
            c'8
            d'8
            \time 2/8
            e'8
            f'8
            \time 2/8
            g'8
            a'8
            \time 2/8
            b'8
            c''8
    }
    '''

    parts = componenttools.partition_components_by_durations_exactly(
        staff.select_leaves(), [Duration(3, 8)], cyclic=True, in_seconds=False, overhang=True)

    "[[Note(c'', 8), Note(b', 8), Note(a', 8)], "
    "[Note(g', 8), Note(f', 8), Note(e', 8)], "
    "[Note(d', 8), Note(c', 8)]]"

    assert len(parts) == 3
    assert parts[0] == list(staff.select_leaves()[:3])
    assert parts[1] == list(staff.select_leaves()[3:6])
    assert parts[2] == list(staff.select_leaves()[6:8])


def test_componenttools_partition_components_by_durations_exactly_04():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    contexttools.TempoMark(Duration(1, 4), 60, target_context = Staff)(staff)

    r'''
    \new Staff {
            \time 2/8
            \tempo 4=60
            c'8
            d'8
            \time 2/8
            e'8
            f'8
            \time 2/8
            g'8
            a'8
            \time 2/8
            b'8
            c''8
            %% tempo 4=60 ends here
    }
    '''

    parts = componenttools.partition_components_by_durations_exactly(
        staff.select_leaves(), [1.5], cyclic=False, in_seconds=True, overhang=False)

    "[[Note(c'', 8), Note(b', 8), Note(a', 8)]]"

    assert len(parts) == 1
    assert parts[0] == list(staff.select_leaves()[:3])


def test_componenttools_partition_components_by_durations_exactly_05():

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 4)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)

    r'''
    \new Staff {
            \time 2/8
            c'8
            d'8
            \time 2/8
            e'8
            f'8
            \time 2/8
            g'8
            a'8
            \time 2/8
            b'8
            c''8
    }
    '''

    groups = \
        componenttools.partition_components_by_durations_exactly(
        t.select_leaves(), [Duration(3, 8)], cyclic=False, in_seconds=False, overhang=False)

    "[[Note(c'', 8), Note(b', 8), Note(a', 8)]]"

    assert len(groups) == 1
    assert groups[0] == list(t.select_leaves()[:3])
