# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_01():
    r'''Move parentage, children and spanners from multiple containers 
    to empty tuplet.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    spannertools.BeamSpanner(voice.select_leaves())

    r'''
    \new Voice {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8
        }
        {
            g'8
            a'8 ]
        }
    }
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(3, 8), [])
    containertools.move_parentage_children_and_spanners_from_components_to_empty_container(voice[:2], tuplet)

    r'''
    \new Voice {
        \tweak #'text #tuplet-number::calc-fraction-text
        \times 3/4 {
            c'8 [
            d'8
            e'8
            f'8
        }
        {
            g'8
            a'8 ]
        }
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            \tweak #'text #tuplet-number::calc-fraction-text
            \times 3/4 {
                c'8 [
                d'8
                e'8
                f'8
            }
            {
                g'8
                a'8 ]
            }
        }
        '''
        )


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_02():
    r'''Move parentage, children and spanners from container to empty voice.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 3)
    voice.name = 'foo'
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    spannertools.GlissandoSpanner(voice[:])
    spannertools.BeamSpanner(voice.select_leaves())

    r'''
    \context Voice = "foo" {
        {
            c'8 [ \glissando
            d'8 \glissando
        }
        {
            e'8 \glissando
            f'8 \glissando
        }
        {
            g'8 \glissando
            a'8 ]
        }
    }
    '''

    new = Voice()
    new.name = 'foo'
    containertools.move_parentage_children_and_spanners_from_components_to_empty_container(voice[1:2], new)

    r'''
    \context Voice = "foo" {
        {
            c'8 [ \glissando
            d'8 \glissando
        }
        \context Voice = "foo" {
            e'8 \glissando
            f'8 \glissando
        }
        {
            g'8 \glissando
            a'8 ]
        }
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \context Voice = "foo" {
            {
                c'8 [ \glissando
                d'8 \glissando
            }
            \context Voice = "foo" {
                e'8 \glissando
                f'8 \glissando
            }
            {
                g'8 \glissando
                a'8 ]
            }
        }
        '''
        )


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_03():
    r'''Move parentage, children and spanners from container to empty tuplet.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    spannertools.GlissandoSpanner(voice[:])
    spannertools.BeamSpanner(voice.select_leaves())

    r'''
    \new Voice {
        {
            c'8 [ \glissando
            d'8 \glissando
        }
        {
            e'8 \glissando
            f'8 \glissando
        }
        {
            g'8 \glissando
            a'8 ]
        }
    }
    '''

    containertools.move_parentage_children_and_spanners_from_components_to_empty_container(
        voice[1:2], tuplettools.FixedDurationTuplet(Duration(3, 16), []))

    r'''
    \new Voice {
        {
            c'8 [ \glissando
            d'8 \glissando
        }
        \tweak #'text #tuplet-number::calc-fraction-text
        \times 3/4 {
            e'8 \glissando
            f'8 \glissando
        }
        {
            g'8 \glissando
            a'8 ]
        }
    }
    '''

    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            {
                c'8 [ \glissando
                d'8 \glissando
            }
            \tweak #'text #tuplet-number::calc-fraction-text
            \times 3/4 {
                e'8 \glissando
                f'8 \glissando
            }
            {
                g'8 \glissando
                a'8 ]
            }
        }
        '''
        )

    assert select(voice).is_well_formed()


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_04():
    r'''Trying to move parentage, children and spanners to noncontainer 
    raises exception.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 2)
    spannertools.BeamSpanner(voice[:])
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)

    assert py.test.raises(
        Exception,
        'containertools.move_parentage_children_and_spanners_from_components_to_empty_container(voice[1:2], Note(4, (1, 4)))')


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_05():
    r'''Trying to move parentage, children and spanners from nonempty container
    to nonempty container raises exception.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 2)
    spannertools.BeamSpanner(voice[:])
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)

    tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")
    assert py.test.raises(
        Exception,
        'containertools.move_parentage_children_and_spanners_from_components_to_empty_container(voice[1:2], tuplet)')


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_06():
    r'''Trying to move parentage, children and spanners from components 
    that are not parent-contiguous raises exception.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    spannertools.BeamSpanner(voice.select_leaves())

    r'''
    \new Voice {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8
        }
        {
            g'8
            a'8 ]
        }
    }
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(3, 8), [])
    assert py.test.raises(
        Exception,
        'containertools.move_parentage_children_and_spanners_from_components_to_empty_container([voice[0], voice[2]], tuplet)')


def test_containertools_move_parentage_children_and_spanners_from_components_to_empty_container_07():
    r'''Move parentage, children and spanners from multiple dynamic measure 
    to empty measure.
    '''

    t = Measure((4, 8), "c'8 d'8 e'8 f'8")

    r'''
    {
        \time 4/8
        c'8
        d'8
        e'8
        f'8
    }
    '''

    u = Measure((4, 8), [])
    containertools.move_parentage_children_and_spanners_from_components_to_empty_container([t], u)

    r'''
    {
        \time 4/8
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert testtools.compare(
        u.lilypond_format,
        r'''
        {
            \time 4/8
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )
