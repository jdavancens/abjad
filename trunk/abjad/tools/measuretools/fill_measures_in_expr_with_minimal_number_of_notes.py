from abjad.tools import contexttools


def fill_measures_in_expr_with_minimal_number_of_notes(expr, big_endian=True, iterctrl=None):
    '''.. versionadded:: 1.1

    Fill measures in `expr` with minimal number of big-endian notes.

        >>> measure = Measure((5, 18), [])

    ::

        >>> measuretools.fill_measures_in_expr_with_minimal_number_of_notes(measure, big_endian=True)

    ::

        >>> f(measure)
        {
            \time 5/18
            \scaleDurations #'(8 . 9) {
                c'4 ~
                c'16
            }
        }

    Fill measures in `expr` with minimal number of little-endian notes.

        >>> measure = Measure((5, 18), [])

    ::

        >>> measuretools.fill_measures_in_expr_with_minimal_number_of_notes(measure, big_endian=False)

    ::

        >>> f(measure)
        {
            \time 5/18
            \scaleDurations #'(8 . 9) {
                c'16 ~
                c'4
            }
        }

    '''
    from abjad.tools import measuretools
    from abjad.tools import notetools

    if iterctrl is None:
        iterctrl = lambda measure, i: True
    for i, measure in enumerate(measuretools.iterate_measures_forward_in_expr(expr)):
        if iterctrl(measure, i):
            meter = contexttools.get_effective_time_signature(measure)
            written_duration = meter.duration / meter.multiplier
            notes = notetools.make_notes(0, written_duration, big_endian=big_endian)
            measure[:] = notes
