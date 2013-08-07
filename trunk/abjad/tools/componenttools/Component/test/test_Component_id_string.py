# -*- encoding: utf-8 -*-
from abjad import *


def test_Component_id_string_01():
    r'''Return component name if it exists, otherwise Python ID.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    assert staff._id_string.startswith('Staff-')


def test_Component_id_string_02():
    r'''Return component name if it exists, otherwise Python ID.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.name = 'foo'
    assert t._id_string == "Staff-'foo'"
