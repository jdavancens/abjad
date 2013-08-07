# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_Container_append_01():
    r'''Append sequential to voice.
    '''

    voice = Voice(notetools.make_repeated_notes(2))
    spannertools.BeamSpanner(voice[:])
    voice.append(Container(notetools.make_repeated_notes(2)))
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)

    r'''
    \new Voice {
        c'8 [
        d'8 ]
        {
            e'8
            f'8
        }
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            c'8 [
            d'8 ]
            {
                e'8
                f'8
            }
        }
        '''
        )


def test_Container_append_02():
    r'''Append leaf to tuplet.
    '''

    t = tuplettools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")
    spannertools.BeamSpanner(t[:])
    t.append(Note(5, (1, 16)))

    r'''
    \times 4/7 {
        c'8 [
        d'8
        e'8 ]
        f'16
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \times 4/7 {
            c'8 [
            d'8
            e'8 ]
            f'16
        }
        '''
        )


def test_Container_append_03():
    r'''Trying to append noncomponent to container
        raises TypeError.'''

    voice = Voice("c'8 d'8 e'8")
    spannertools.BeamSpanner(voice[:])

    assert py.test.raises(Exception, "voice.append('foo')")
    assert py.test.raises(Exception, "voice.append(99)")
    assert py.test.raises(Exception, "voice.append([])")
    assert py.test.raises(Exception, "voice.append([Note(0, (1, 8))])")


def test_Container_append_04():
    r'''Append spanned leaf from donor container to recipient container.
    '''

    voice = Voice("c'8 d'8 e'8")
    spannertools.BeamSpanner(voice[:])

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8 ]
    }
    '''

    u = Voice("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(u[:])

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8
        f'8 ]
    }
    '''

    voice.append(u[-1])

    "Container voice is now ..."

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8 ]
        f'8
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            c'8 [
            d'8
            e'8 ]
            f'8
        }
        '''
        )

    "Container u is now ..."

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8 ]
    }
    '''

    assert select(u).is_well_formed()
    assert testtools.compare(
        u.lilypond_format,
        r'''
        \new Voice {
            c'8 [
            d'8
            e'8 ]
        }
        '''
        )


def test_Container_append_05():
    r'''Append spanned leaf from donor container to recipient container.
        Donor and recipient containers are the same.'''

    voice = Voice("c'8 d'8 e'8 f'8")
    spannertools.BeamSpanner(voice[:])

    r'''
    \new Voice {
        c'8 [
        d'8
        e'8
        f'8 ]
    }
    '''

    voice.append(voice[1])

    r'''
    \new Voice {
        c'8 [
        e'8
        f'8 ]
        d'8
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice.lilypond_format,
        r'''
        \new Voice {
            c'8 [
            e'8
            f'8 ]
            d'8
        }
        '''
        )


def test_Container_append_06():
    r'''Can not insert grace container into container.
    '''

    staff = Staff("c' d' e'")
    grace_container = leaftools.GraceContainer("f'16 g'")

    assert py.test.raises(GraceContainerError, 'staff.append(grace_container)')
