# -*- coding: utf-8 -*-
from abjad.tools import scoretools


def make_basic_lilypond_file(
    music=None,
    date_time_token=None,
    default_paper_size=None,
    comments=None,
    includes=None,
    global_staff_size=None,
    lilypond_language_token=None,
    lilypond_version_token=None,
    use_relative_includes=None,
    ):
    r'''Makes basic LilyPond file.

    ..  container:: example


        ::

            >>> score = Score([Staff("c'8 d'8 e'8 f'8")])
            >>> lilypond_file = lilypondfiletools.make_basic_lilypond_file(score)
            >>> lilypond_file.header_block.title = Markup('Missa sexti tonus')
            >>> lilypond_file.header_block.composer = Markup('Josquin')
            >>> lilypond_file.layout_block.indent = 0
            >>> lilypond_file.paper_block.top_margin = 15
            >>> lilypond_file.paper_block.left_margin = 15

        ::

            >>> print(format(lilypond_file)) # doctest: +SKIP
            \header {
                composer = \markup { Josquin }
                title = \markup { Missa sexti tonus }
            }

            \layout {
                indent = #0
            }

            \paper {
                left-margin = #15
                top-margin = #15
            }

            \score {
                \new Score <<
                    \new Staff {
                        c'8
                        d'8
                        e'8
                        f'8
                    }
                >>
            }

        ::

            >>> show(lilypond_file) # doctest: +SKIP

    Wraps `music` in LilyPond ``\score`` block.

    Adds LilyPond ``\header``, ``\layout``, ``\paper`` and ``\score`` blocks to
    LilyPond file.

    Returns LilyPond file.
    '''
    from abjad.tools import lilypondfiletools
    if isinstance(music, lilypondfiletools.LilyPondFile):
        return music
    lilypond_file = lilypondfiletools.LilyPondFile(
        date_time_token=date_time_token,
        default_paper_size=default_paper_size,
        comments=comments,
        includes=includes,
        global_staff_size=global_staff_size,
        lilypond_language_token=lilypond_language_token,
        lilypond_version_token=lilypond_version_token,
        use_relative_includes=use_relative_includes,
        )
    header_block = lilypondfiletools.Block(name='header')
    layout_block = lilypondfiletools.Block(name='layout')
    paper_block = lilypondfiletools.Block(name='paper')
    score_block = lilypondfiletools.Block(name='score')
    lilypond_file.items.extend([
        header_block,
        layout_block,
        paper_block,
        score_block,
        ])
    if music is not None:
        score_block.items.append(music)
    return lilypond_file