def timespan_2_overlaps_only_start_of_timespan_1(timespan_1=None, timespan_2=None, hold=False):
    r'''.. versionadded:: 2.11

    Make timespan inequality template indicating that expression happens during timespan::

        >>> timerelationtools.timespan_2_overlaps_only_start_of_timespan_1()
        TimespanTimespanTimeRelation('timespan_2.start < timespan_1.start < timespan_2.start <= timespan_1.stop')

    Return boolean or timespan inequality.
    '''
    from abjad.tools import timerelationtools

    timespan_inequality = timerelationtools.TimespanTimespanTimeRelation(
        'timespan_2.start < timespan_1.start < timespan_2.start <= timespan_1.stop',
        timespan_1=timespan_1, 
        timespan_2=timespan_2)
    
    if timespan_inequality.is_fully_loaded and not hold: 
        return timespan_inequality()
    else:
        return timespan_inequality
