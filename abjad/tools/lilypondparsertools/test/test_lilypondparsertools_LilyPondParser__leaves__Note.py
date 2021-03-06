# -*- coding: utf-8 -*-
from abjad import *
from abjad.tools.lilypondparsertools import LilyPondParser


def test_lilypondparsertools_LilyPondParser__leaves__Note_01():

    target = Note(0, 1)
    parser = LilyPondParser()
    result = parser('{ %s }' % format(target))
    assert format(target) == format(result[0]) and target is not result[0]