# -*- encoding: utf-8 -*-
from abjad import *


def test_GlissandoSpanner_01():
    staff = Staff([Note(n, (1, 8)) for n in range(8)])
    gliss = spannertools.GlissandoSpanner(staff.select_leaves()[:4])
    assert isinstance(gliss, spannertools.GlissandoSpanner)
    assert staff.lilypond_format =="\\new Staff {\n\tc'8 \\glissando\n\tcs'8 \\glissando\n\td'8 \\glissando\n\tef'8\n\te'8\n\tf'8\n\tfs'8\n\tg'8\n}"
    '''
    \new Staff {
        c'8 \glissando
        cs'8 \glissando
        d'8 \glissando
        ef'8
        e'8
        f'8
        fs'8
        g'8
    }
    '''
