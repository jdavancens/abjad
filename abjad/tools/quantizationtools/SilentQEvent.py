# -*- encoding: utf-8 -*-
from abjad.tools.quantizationtools.QEvent import QEvent


class SilentQEvent(QEvent):
    r'''A ``QEvent`` which indicates the onset of a period of silence
    in a ``QEventSequence``.

        >>> q_event = quantizationtools.SilentQEvent(1000)
        >>> q_event
        SilentQEvent(offset=Offset(1000, 1))

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_attachments',
        )

    ### INITIALIZER ###

    def __init__(self, offset=0, attachments=None, index=None):
        QEvent.__init__(self, offset=offset, index=index)
        if attachments is None:
            attachments = ()
        else:
            attachments = tuple(attachments)
        self._attachments = attachments

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if type(self) == type(expr) and \
            self._offset == expr._offset and \
            self._attachments == expr._attachments and \
            self._index == expr._index:
            return True
        return False

    ### PUBLIC PROPERTIES ###

    @property
    def attachments(self):
        return self._attachments
