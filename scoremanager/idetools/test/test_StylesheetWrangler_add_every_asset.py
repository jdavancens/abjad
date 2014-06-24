# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_StylesheetWrangler_add_every_asset_01():
    r'''Flow control reaches method in score.
    '''

    score_manager._session._is_repository_test = True
    input_ = 'red~example~score y rad* q'
    score_manager._run(input_=input_)
    assert score_manager._session._attempted_to_add


def test_StylesheetWrangler_add_every_asset_02():
    r'''Flow control reaches method in library.
    '''

    score_manager._session._is_repository_test = True
    input_ = 'Y rad* q'
    score_manager._run(input_=input_)
    assert score_manager._session._attempted_to_add