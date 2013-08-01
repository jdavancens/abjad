# -*- encoding: utf-8 -*-
def remove_component_subtree_from_score_and_spanners(components):
    r'''Example 1. Remove one leaf from score:

    ::

        >>> voice = Voice("c'8 [ { d'8 e'8 } f'8 ]")
        >>> spannertools.GlissandoSpanner(voice.select_leaves())
        GlissandoSpanner(c'8, d'8, e'8, f'8)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            {
                d'8 \glissando
                e'8 \glissando
            }
            f'8 ]
        }

    ::

        >>> componenttools.remove_component_subtree_from_score_and_spanners(
        ...     voice.select_leaves()[1:2])
        SequentialLeafSelection(Note("d'8"),)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            {
                e'8 \glissando
            }
            f'8 ]
        }

    Example 2. Remove contiguous leaves from score:

    ::

        >>> voice = Voice("c'8 [ { d'8 e'8 } f'8 ]")
        >>> spannertools.GlissandoSpanner(voice.select_leaves())
        GlissandoSpanner(c'8, d'8, e'8, f'8)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            {
                d'8 \glissando
                e'8 \glissando
            }
            f'8 ]
        }

    ::

        >>> componenttools.remove_component_subtree_from_score_and_spanners(
        ...     voice.select_leaves()[:2])
        SequentialLeafSelection(Note("c'8"), Note("d'8"))

    ::

        >>> f(voice)
        \new Voice {
            {
                e'8 [ \glissando
            }
            f'8 ]
        }

    Example 3. Remove noncontiguous leaves from score:

    ::

        >>> voice = Voice("c'8 [ { d'8 e'8 } f'8 ]")
        >>> spannertools.GlissandoSpanner(voice.select_leaves())
        GlissandoSpanner(c'8, d'8, e'8, f'8)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            {
                d'8 \glissando
                e'8 \glissando
            }
            f'8 ]
        }

    ::

        >>> componenttools.remove_component_subtree_from_score_and_spanners(
        ... [voice.select_leaves()[0], voice.select_leaves()[2]])
        [Note("c'8"), Note("e'8")]

    ::

        >>> f(voice)
        \new Voice {
            { d'8 [ \glissando
            }
            f'8 ]
        }

    Example 4. Remove container from score:

    ::

        >>> voice = Voice("c'8 [ { d'8 e'8 } f'8 ]")
        >>> spannertools.GlissandoSpanner(voice.select_leaves())
        GlissandoSpanner(c'8, d'8, e'8, f'8)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            {
                d'8 \glissando
                e'8 \glissando
            }
            f'8 ]
        }

    ::

        >>> componenttools.remove_component_subtree_from_score_and_spanners(
        ...     voice[1:2])
        SequentialSelection({d'8, e'8},)

    ::

        >>> f(voice)
        \new Voice {
            c'8 [ \glissando
            f'8 ]
        }

    Withdraw `components` and children of `components` from spanners.

    Return either tuple or list of `components` and children of `components`.

    .. todo:: regularize return value of function.
    '''
    from abjad.tools import componenttools
    from abjad.tools import iterationtools

    # check input
    assert componenttools.all_are_components(components)

    # remove from score and spanners
    for component in components:
        component._remove_from_parent()
        for child in iterationtools.iterate_components_in_expr([component]):
            for spanner in child.spanners:
                spanner._remove(child)

    # return components
    return components
