from abjad.tools.abctools.AbjadObject import AbjadObject


class LiteralTimespan(AbjadObject):
    r'''.. versionadded:: 2.11

    Literal timespan.

    Literal timespan ``[1/2, 3/2)``::

        >>> timespan_constant = timerelationtools.LiteralTimespan((1, 2), (3, 2)) 

    ::

        >>> timespan_constant
        LiteralTimespan(start_offset=Offset(1, 2), stop_offset=Offset(3, 2))

    ::
    
        >>> z(timespan_constant)
        timerelationtools.LiteralTimespan(
            start_offset=durationtools.Offset(1, 2),
            stop_offset=durationtools.Offset(3, 2)
            )

    Literal timespans are object-modeled offset pairs.

    Literal timespans are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, start_offset=None, stop_offset=None):
        start_offset = self._initialize_offset(start_offset)
        stop_offset = self._initialize_offset(stop_offset)
        self._start_offset = start_offset
        self._stop_offset = stop_offset

    ### PRIVATE METHODS ###

    def _initialize_offset(self, offset):
        from abjad.tools import durationtools
        if offset is not None:
            return durationtools.Offset(offset)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def duration(self):
        '''Duration of timespan constant.
        '''
        return self.stop_offset - self.start_offset

    @property
    def start_offset(self):
        '''Start offset of timespan constant specified by user.

        Return offset.
        '''
        return self._start_offset

    @property
    def stop_offset(self):
        '''Stop offset of timespan constant specified by user.

        Return stop offset.
        '''
        return self._stop_offset
