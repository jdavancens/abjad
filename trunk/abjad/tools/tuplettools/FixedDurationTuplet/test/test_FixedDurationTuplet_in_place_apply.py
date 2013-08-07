# -*- encoding: utf-8 -*-
from abjad import *


def test_FixedDurationTuplet_in_place_apply_01():
    container = Container([Note(n, (1, 8)) for n in range(8)])
    leaves_before = container.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), container[0:3])
    leaves_after = container.select_leaves()
    assert leaves_before == leaves_after
    assert len(container) == 6
    for i, x in enumerate(container):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(container).is_well_formed()


def test_FixedDurationTuplet_in_place_apply_02():
    t = tuplettools.FixedDurationTuplet(Duration(7, 8), [Note(n, (1, 8)) for n in range(8)])
    leaves_before = t.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), t[0:3])
    leaves_after = t.select_leaves()
    assert leaves_before == leaves_after
    assert len(t) == 6
    for i, x in enumerate(t):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(t).is_well_formed()


def test_FixedDurationTuplet_in_place_apply_03():
    #tuplet = Tuplet(Fraction(7, 8), [Note(n, (1, 8)) for n in range(8)])
    tuplet = Tuplet(Fraction(7, 8), [Note(n, (1, 8)) for n in range(8)])
    leaves_before = tuplet.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), tuplet[0:3])
    leaves_after = tuplet.select_leaves()
    assert leaves_before == leaves_after
    assert len(tuplet) == 6
    for i, x in enumerate(tuplet):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(tuplet).is_well_formed()


def test_FixedDurationTuplet_in_place_apply_04():
    measure = Measure((8, 8), [Note(n, (1, 8)) for n in range(8)])
    leaves_before = measure.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), measure[0:3])
    measure.select().detach_marks(contexttools.TimeSignatureMark)
    contexttools.TimeSignatureMark((7, 8))(measure)
    leaves_after = measure.select_leaves()
    assert leaves_before == leaves_after
    assert len(measure) == 6
    for i, x in enumerate(measure):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(measure).is_well_formed()


def test_FixedDurationTuplet_in_place_apply_05():
    voice = Voice([Note(n, (1, 8)) for n in range(8)])
    leaves_before = voice.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), voice[0:3])
    leaves_after = voice.select_leaves()
    assert leaves_before == leaves_after
    assert len(voice) == 6
    for i, x in enumerate(voice):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(voice).is_well_formed()


def test_FixedDurationTuplet_in_place_apply_06():
    t = Staff([Note(n, (1, 8)) for n in range(8)])
    leaves_before = t.select_leaves()
    tuplettools.FixedDurationTuplet(Duration(2, 8), t[0:3])
    leaves_after = t.select_leaves()
    assert leaves_before == leaves_after
    assert len(t) == 6
    for i, x in enumerate(t):
        if i == 0:
            assert isinstance(x, tuplettools.FixedDurationTuplet)
        else:
            assert isinstance(x, Note)
    assert select(t).is_well_formed()
