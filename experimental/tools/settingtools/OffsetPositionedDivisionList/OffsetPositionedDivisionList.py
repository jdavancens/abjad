import copy
from abjad.tools import durationtools
from abjad.tools import sequencetools
from experimental.tools import divisiontools
from experimental.tools.settingtools.OffsetPositionedExpression import OffsetPositionedExpression


class OffsetPositionedDivisionList(OffsetPositionedExpression):
    r'''

    ::

        >>> from experimental.tools import *

    Offset-positioned division expression.

    Composers do not create offset-positioned division expressions
    because division expression arise as a byproduct of interpretation.
    '''

    ### INITIALIZER ###

    def __init__(self, division_list, voice_name=None, start_offset=None, stop_offset=None):
        OffsetPositionedExpression.__init__(
            self, voice_name, start_offset=start_offset, stop_offset=stop_offset)
        if not isinstance(division_list, divisiontools.DivisionList):
            division_list = divisiontools.DivisionList(division_list)
        self._division_list = division_list

    ### SPECIAL METHODS ###

    def __len__(self):
        return len(self.division_list)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def division_list(self):
        '''Offset-positioned division expression division list.

        Return division list object.
        '''
        return self._division_list

    @property
    def divisions(self):
        '''Offset-positioned division expression division list divisions.

        Delegate to ``self.division_list.divisions``.

        Return list.
        '''
        return self.division_list.divisions

    @property
    def duration(self):
        '''Duration of division expression.
        
        Return duration.
        '''
        return self.division_list.duration

    ### PUBLIC METHODS ###
    
    def fracture(self, slice_index):
        assert isinstance(slice_index, int)
        left_division_list, right_division_list = self.division_list.fracture(slice_index)
        left_result = type(self)(
            left_division_list, voice_name=self.voice_name, start_offset=self.start_offset)
        right_result = type(self)(
            right_division_list, voice_name=self.voice_name, start_offset=left_result.stop_offset)
        return left_result, right_result

    def fuse(self, expr):
        '''Fuse if expression stops when `expr` starts::

            >>> expr_1 = settingtools.OffsetPositionedDivisionList(2 * [(3, 16)], 'Voice 1')
            >>> expr_2 = settingtools.OffsetPositionedDivisionList(
            ...     2 * [(2, 16)], 'Voice 1', start_offset=(6, 16))

        ::

            >>> expr_1.stops_when_expr_starts(expr_2)
            True

        ::

            >>> new_expr = expr_1.fuse(expr_2)

        ::
        
            >>> z(new_expr)
            settingtools.OffsetPositionedDivisionList(
                divisiontools.DivisionList(
                    [Division('[3, 16]'), Division('[3, 16]'), Division('[2, 16]'), Division('[2, 16]')]
                    ),
                voice_name='Voice 1',
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(5, 8)
                )

        Return newly constructed expression.
        '''
        assert isinstance(expr, type(self)), repr(expr)
        assert self.stops_when_expr_starts(expr), repr(expr)
        assert self.voice_name == expr.voice_name, repr(expr)
        division_list = self.division_list + expr.division_list
        result = type(self)(division_list, voice_name=self.voice_name, start_offset=self.start_offset)
        return result

    def reverse(self):
        self.division_list.reverse()

    def _set_start_offset(self, start_offset):
        '''Trim to start offset.

        ::

            >>> expr = settingtools.OffsetPositionedDivisionList(4 * [(3, 16)], 'Voice 1')

        ::

            >>> z(expr)
            settingtools.OffsetPositionedDivisionList(
                divisiontools.DivisionList(
                    [Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]')]
                    ),
                voice_name='Voice 1',
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(3, 4)
                )

        ::

            >>> expr.set_offsets(start_offset=(1, 16))

        ::

            >>> z(expr)
            settingtools.OffsetPositionedDivisionList(
                divisiontools.DivisionList(
                    [Division('[2, 16]'), Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]')]
                    ),
                voice_name='Voice 1',
                start_offset=durationtools.Offset(1, 16),
                stop_offset=durationtools.Offset(3, 4)
                )

        ::

            >>> expr.duration
            Duration(11, 16)

        Set start offset.
        
        Operate in place and return none.
        '''
        start_offset = durationtools.Offset(start_offset)
        assert self.start_offset <= start_offset
        duration_to_trim = start_offset - self.start_offset
        divisions = copy.deepcopy(self.divisions)
        shards = sequencetools.split_sequence_by_weights(
            divisions, [duration_to_trim], cyclic=False, overhang=True)
        trimmed_divisions = shards[-1]
        division_list = divisiontools.DivisionList(trimmed_divisions)
        self._division_list = division_list
        self._start_offset = start_offset

    def _set_stop_offset(self, stop_offset):
        '''Trim to stop offset.

        ::

            >>> expr = settingtools.OffsetPositionedDivisionList(4 * [(3, 16)], 'Voice 1')

        ::

            >>> z(expr)
            settingtools.OffsetPositionedDivisionList(
                divisiontools.DivisionList(
                    [Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]')]
                    ),
                voice_name='Voice 1',
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(3, 4)
                )

        ::

            >>> expr.set_offsets(stop_offset=(11, 16))

        ::

            >>> z(expr)
            settingtools.OffsetPositionedDivisionList(
                divisiontools.DivisionList(
                    [Division('[3, 16]'), Division('[3, 16]'), Division('[3, 16]'), Division('[2, 16]')]
                    ),
                voice_name='Voice 1',
                start_offset=durationtools.Offset(0, 1),
                stop_offset=durationtools.Offset(11, 16)
                )

        ::

            >>> expr.duration
            Duration(11, 16)

        Set stop offset.
        
        Operate in place and return none.
        '''
        stop_offset = durationtools.Offset(stop_offset)
        assert stop_offset <= self.stop_offset
        duration_to_trim = self.stop_offset - stop_offset
        duration_to_keep = self.division_list.duration - duration_to_trim
        divisions = copy.deepcopy(self.divisions)
        shards = sequencetools.split_sequence_by_weights(
            divisions, [duration_to_keep], cyclic=False, overhang=True)
        trimmed_divisions = shards[0]
        division_list = divisiontools.DivisionList(trimmed_divisions)
        self._division_list = division_list
