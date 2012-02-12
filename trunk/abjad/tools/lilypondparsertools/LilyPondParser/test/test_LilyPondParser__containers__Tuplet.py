from abjad import *
from abjad.tools.lilypondparsertools import LilyPondParser


def test_LilyPondParser__containers__Tuplet_01():
    notes = notetools.make_notes([0, 2, 4, 5, 7], (1, 8))
    target = tuplettools.Tuplet(Fraction(2, 3), notes)

    r'''\times 2/3 {
        c'8
        d'8
        e'8
        f'8
        g'8
    }
    '''

    parser = LilyPondParser()
    result = parser(target.format)
    assert target.format == result.format and target is not result

