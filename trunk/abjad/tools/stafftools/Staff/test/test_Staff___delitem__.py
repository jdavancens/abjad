# -*- encoding: utf-8 -*-
from abjad import *
from py.test import raises


def test_Staff___delitem___01():
    staff = Staff([Note("c'4"),
            Rest((1, 4)),
            Chord([2, 3, 4], (1, 4)),
            skiptools.Skip((1, 4)),
            tuplettools.FixedDurationTuplet(Duration(5, 16), Note(0, (1, 16)) * 4)])
    assert len(staff) == 5
    assert isinstance(staff[0], Note)
    assert isinstance(staff[1], Rest)
    assert isinstance(staff[2], Chord)
    assert isinstance(staff[3], skiptools.Skip)
    assert isinstance(staff[4], tuplettools.FixedDurationTuplet)
    del(staff[0])
    assert len(staff) == 4
    assert isinstance(staff[0], Rest)
    assert isinstance(staff[1], Chord)
    assert isinstance(staff[2], skiptools.Skip)
    assert isinstance(staff[3], tuplettools.FixedDurationTuplet)
    del(staff[0])
    assert len(staff) == 3
    assert isinstance(staff[0], Chord)
    assert isinstance(staff[1], skiptools.Skip)
    assert isinstance(staff[2], tuplettools.FixedDurationTuplet)
    del(staff[0])
    assert len(staff) == 2
    assert isinstance(staff[0], skiptools.Skip)
    assert isinstance(staff[1], tuplettools.FixedDurationTuplet)
    del(staff[0])
    assert len(staff) == 1
    assert isinstance(staff[0], tuplettools.FixedDurationTuplet)
    del(staff[0])
    assert len(staff) == 0


def test_Staff___delitem___02():
    staff = Staff([Note("c'4"),
            Rest((1, 4)),
            Chord([2, 3, 4], (1, 4)),
            skiptools.Skip((1, 4)),
            tuplettools.FixedDurationTuplet(Duration(5, 16), Note(0, (1, 16)) * 4)])
    assert len(staff) == 5
    assert isinstance(staff[0], Note)
    assert isinstance(staff[1], Rest)
    assert isinstance(staff[2], Chord)
    assert isinstance(staff[3], skiptools.Skip)
    assert isinstance(staff[4], tuplettools.FixedDurationTuplet)
    del(staff[-1])
    assert len(staff) == 4
    assert isinstance(staff[0], Note)
    assert isinstance(staff[1], Rest)
    assert isinstance(staff[2], Chord)
    assert isinstance(staff[3], skiptools.Skip)
    del(staff[-1])
    assert len(staff) == 3
    assert isinstance(staff[0], Note)
    assert isinstance(staff[1], Rest)
    assert isinstance(staff[2], Chord)
    del(staff[-1])
    assert len(staff) == 2
    assert isinstance(staff[0], Note)
    assert isinstance(staff[1], Rest)
    del(staff[-1])
    assert len(staff) == 1
    assert isinstance(staff[0], Note)
    del(staff[-1])
    assert len(staff) == 0


def test_Staff___delitem___03():
    t = Staff([Note("c'4"),
            Rest((1, 4)),
            Chord([2, 3, 4], (1, 4)),
            skiptools.Skip((1, 4)),
            tuplettools.FixedDurationTuplet(Duration(5, 16), Note(0, (1, 16)) * 4)])
    assert len(t) == 5
    assert isinstance(t[0], Note)
    assert isinstance(t[1], Rest)
    assert isinstance(t[2], Chord)
    assert isinstance(t[3], skiptools.Skip)
    assert isinstance(t[4], tuplettools.FixedDurationTuplet)
    del(t[3])
    assert len(t) == 4
    assert isinstance(t[0], Note)
    assert isinstance(t[1], Rest)
    assert isinstance(t[2], Chord)
    assert isinstance(t[3], tuplettools.FixedDurationTuplet)
    del(t[-2])
    assert len(t) == 3
    assert isinstance(t[0], Note)
    assert isinstance(t[1], Rest)
    assert isinstance(t[2], tuplettools.FixedDurationTuplet)
    del(t[2])
    assert len(t) == 2
    assert isinstance(t[0], Note)
    assert isinstance(t[1], Rest)
    del(t[0])
    assert len(t) == 1
    assert isinstance(t[0], Rest)
    del(t[-1])
    assert len(t) == 0
