# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_componenttools_all_are_contiguous_components_in_same_thread_01():
    r'''True for strictly contiguous leaves in same staff.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    assert componenttools.all_are_contiguous_components_in_same_thread(staff[:])


def test_componenttools_all_are_contiguous_components_in_same_thread_02():
    r'''True for orphan components when allow_orphans is True.
        False for orphan components when allow_orphans is False.'''

    notes = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]
    assert componenttools.all_are_contiguous_components_in_same_thread(notes)
    assert not componenttools.all_are_contiguous_components_in_same_thread(notes, allow_orphans=False)


def test_componenttools_all_are_contiguous_components_in_same_thread_03():
    r'''False for time reordered leaves in staff.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    assert not componenttools.all_are_contiguous_components_in_same_thread(staff[2:] + staff[:2],
        )


def test_componenttools_all_are_contiguous_components_in_same_thread_04():
    r'''False for unincorporated component.
    '''

    assert componenttools.all_are_contiguous_components_in_same_thread([Staff("c'8 d'8 e'8 f'8")],
        )


def test_componenttools_all_are_contiguous_components_in_same_thread_05():
    r'''True for empty list.
    '''

    assert componenttools.all_are_contiguous_components_in_same_thread([])
