# -*- encoding: utf-8 -*-
from abjad import *


def test_componenttools_all_are_contiguous_components_in_same_parent_01():
    r'''True for strictly contiguous leaves in voice.
        False for other time orderings of leaves in voice.'''

    voice = Voice("c'8 d'8 e'8 f'8")

    assert componenttools.all_are_contiguous_components_in_same_parent(voice.select_leaves())

    assert not componenttools.all_are_contiguous_components_in_same_parent(list(reversed(voice.select_leaves())))

    components = []
    components.extend(voice.select_leaves()[2:])
    components.extend(voice.select_leaves()[:2])
    assert not componenttools.all_are_contiguous_components_in_same_parent(components)

    components = []
    components.extend(voice.select_leaves()[3:4])
    components.extend(voice.select_leaves()[0:1])
    assert not componenttools.all_are_contiguous_components_in_same_parent(components)
    components = [voice]
    components.extend(voice.select_leaves())
    assert not componenttools.all_are_contiguous_components_in_same_parent(components)


def test_componenttools_all_are_contiguous_components_in_same_parent_02():
    r'''True for unincorporated components when orphans allowed.
        False to unincorporated components when orphans not allowed.'''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)

    r'''
    \new Voice {
        {
            c'8
            d'8
        }
        {
            e'8
            f'8
        }
    }
    '''

    assert componenttools.all_are_contiguous_components_in_same_parent([voice])
    assert not componenttools.all_are_contiguous_components_in_same_parent([voice],
        allow_orphans = False)

    assert componenttools.all_are_contiguous_components_in_same_parent(voice[:])

    assert componenttools.all_are_contiguous_components_in_same_parent(voice[0][:])
    assert componenttools.all_are_contiguous_components_in_same_parent(voice[1][:])

    assert not componenttools.all_are_contiguous_components_in_same_parent(voice.select_leaves())


def test_componenttools_all_are_contiguous_components_in_same_parent_03():
    r'''True for orphan leaves when allow_orphans is True.
        False for orphan leaves when allow_orphans is False.'''

    notes = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]

    assert componenttools.all_are_contiguous_components_in_same_parent(notes)
    assert not componenttools.all_are_contiguous_components_in_same_parent(notes, allow_orphans=False)


def test_componenttools_all_are_contiguous_components_in_same_parent_04():
    r'''Empty list returns True.
    '''

    t = []

    assert componenttools.all_are_contiguous_components_in_same_parent(t)
