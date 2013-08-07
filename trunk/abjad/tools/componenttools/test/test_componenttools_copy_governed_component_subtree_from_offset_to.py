# -*- encoding: utf-8 -*-
from abjad import *


def test_componenttools_copy_governed_component_subtree_from_offset_to_01():
    r'''Container.
    '''

    container = Container("c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(container, 0, (3, 16))

    r'''
    {
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        {
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_02():
    r'''Container with rest.
    '''

    container = Container("c'8 d'8 e'8")
    rest = Rest(container[1])
    componenttools.move_parentage_and_spanners_from_components_to_components(container[1:2], [rest])
    new = componenttools.copy_governed_component_subtree_from_offset_to(container, 0, (3, 16))

    r'''
    {
    c'8
    r16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        {
            c'8
            r16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_03():
    r'''Copy measure.
    '''

    measure = Measure((3, 8), "c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(measure, 0, (3, 16))

    r'''
    {
    \time 3/16
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        {
            \time 3/16
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_04():
    r'''Fixed duration tuplet.
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(1, 4), "c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(tuplet, 0, (1, 8))

    r'''
    \times 2/3 {
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        \times 2/3 {
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_05():
    r'''Fixed multiplier tuplet.
    '''

    tuplet = Tuplet(Fraction(2, 3), "c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(tuplet, 0, (1, 8))

    r'''
    \times 2/3 {
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        \times 2/3 {
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_06():
    r'''Voice.
    '''

    voice = Voice("c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(voice, 0, (3, 16))

    r'''
    \new Voice {
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Voice {
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_07():
    r'''Staff.
    '''

    staff = Staff("c'8 d'8 e'8")
    new = componenttools.copy_governed_component_subtree_from_offset_to(staff, 0, (3, 16))

    r'''
    \new Staff {
    c'8
    d'16
    }
    '''

    assert testtools.compare(
        new.lilypond_format,
        r'''
        \new Staff {
            c'8
            d'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_08():
    r'''Start-to-mid clean cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, 0, (1, 8))
    assert new.lilypond_format == "c'8"


def test_componenttools_copy_governed_component_subtree_from_offset_to_09():
    r'''Start-to-mid jagged cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, 0, (1, 12))
    parent = new._parent

    r'''
    \times 2/3 {
        c'8
    }
    '''

    assert testtools.compare(
        parent.lilypond_format,
        r'''
        \times 2/3 {
            c'8
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_10():
    r'''Mid-mid jagged cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, (1, 12), (2, 12))
    parent = new._parent

    r'''
    \times 2/3 {
        c'8
    }
    '''

    assert testtools.compare(
        parent.lilypond_format,
        r'''
        \times 2/3 {
            c'8
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_11():
    r'''Mid-to-stop jagged cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, (1, 6), (1, 4))
    parent = new._parent

    r'''
    \times 2/3 {
        c'8
    }
    '''

    assert testtools.compare(
        parent.lilypond_format,
        r'''
        \times 2/3 {
            c'8
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_12():
    r'''Start-to-after clean cut.
    '''
    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, 0, (1, 2))
    assert new.lilypond_format == "c'4"


def test_componenttools_copy_governed_component_subtree_from_offset_to_13():
    r'''Mid-to-after clean cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, (1, 8), (1, 2))
    assert new.lilypond_format == "c'8"


def test_componenttools_copy_governed_component_subtree_from_offset_to_14():
    r'''Mid-to-after jagged cut.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, (2, 12), (1, 2))
    parent = new._parent

    r'''
    \times 2/3 {
        c'8
    }
    '''

    assert testtools.compare(
        parent.lilypond_format,
        r'''
        \times 2/3 {
            c'8
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_15():
    r'''Before-to-after.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, (-1, 4), (1, 2))
    assert new.lilypond_format == "c'4"


def test_componenttools_copy_governed_component_subtree_from_offset_to_16():
    r'''Start-to-mid jagged.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, 0, (5, 24))
    parent = new._parent

    r'''
    \times 2/3 {
        c'4 ~
        c'16
    }
    '''

    assert testtools.compare(
        parent.lilypond_format,
        r'''
        \times 2/3 {
            c'4 ~
            c'16
        }
        '''
        )


def test_componenttools_copy_governed_component_subtree_from_offset_to_17():
    r'''Start-to-mid jagged.
    '''

    note = Note("c'4")
    new = componenttools.copy_governed_component_subtree_from_offset_to(note, 0, (1, 5))
    parent = new._parent

    r'''
    \times 4/5 {
        c'4
    }
    '''
