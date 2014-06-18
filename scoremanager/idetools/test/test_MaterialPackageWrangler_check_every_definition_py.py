# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_check_every_definition_py_01():

    input_ = 'red~example~score m dc* y q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    package_names = [
        'instrumentation',
        'magic_numbers',
        'pitch_range_inventory',
        'tempo_inventory',
        'time_signatures',
        ]
    paths = []
    for package_name in package_names:
        path = os.path.join(
            score_manager._configuration.example_score_packages_directory,
            'red_example_score',
            'materials',
            package_name,
            'definition.py',
            )
        paths.append(path)

    confirmation_messages = [_ + ' OK.' for _ in paths]

    assert 'Will check ...' in contents
    for path in paths:
        assert path in contents
    for confirmation_message in confirmation_messages:
        assert confirmation_message in contents