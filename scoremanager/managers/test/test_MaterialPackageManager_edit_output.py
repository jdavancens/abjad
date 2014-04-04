# -*- encoding: utf-8 -*-
import os
import pytest
import shutil
from abjad import *
from experimental import *
import scoremanager


def test_MaterialPackageManager_edit_output_01():
    '''Edit menu has correct header.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    input_ = 'm example~markup~inventory me q'
    score_manager._run(pending_user_input=input_)
    transcript = score_manager._transcript

    string = 'Score manager - material library -'
    string += ' example markup inventory (Abjad) - markup inventory'
    assert transcript.last_title == string


def test_MaterialPackageManager_edit_output_02():
    r'''Edits tempo inventory.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testtempoinventory',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    inventory = indicatortools.TempoInventory([
        ((1, 4), 60),
        ((1, 4), 90),
        ])

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc TempoInventory testtempoinventory'
        input_ += ' add d (1, 4) units 60 done add d (1, 4) units 90 done'
        input_ += ' done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testtempoinventory rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_03():
    r'''Edits empty pitch range inventory.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testpri',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    inventory = pitchtools.PitchRangeInventory()

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc PitchRangeInventory testpri done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testpri rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_04():
    r'''Edits populated pitch range inventory.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testpri',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    inventory = pitchtools.PitchRangeInventory([
        pitchtools.PitchRange('[C2, G5]'),
        pitchtools.PitchRange('[C2, F#5]'),
        ])
    input_ = 'm nmc PitchRangeInventory testpri default'
    input_ += ' testpri me add range [A0, C8] done'
    input_ += ' add range [C2, F#5] done'
    input_ += ' add range [C2, G5] done'
    input_ += ' rm 1 mv 1 2 b default q'

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testpri rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_05():

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testmarkupinventory',
        )
    inventory = markuptools.MarkupInventory(
        [
            markuptools.Markup(
                '\\italic { serenamente }',
                ),
            markuptools.Markup(
                '\\italic { presto }',
                )
            ],
        )
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'output.py',
        ]

    assert not os.path.exists(path)
    try:
        input_ = "m nmc markup testmarkupinventory"
        input_ += " add arg r'\\italic~{~serenamente~}' done"
        input_ += " add arg r'\\italic~{~presto~}' done done default q"
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testmarkupinventory rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_06():
    r'''Edits empty octave transposition mapping inventory.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testoctavetrans',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    inventory = pitchtools.OctaveTranspositionMappingInventory()

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc OctaveTranspositionMappingInventory'
        input_ += ' testoctavetrans done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testoctavetrans rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_07():
    r'''Edits populated octave transposition mapping inventory.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testoctavetrans',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    mapping_1 = pitchtools.OctaveTranspositionMapping([
        ('[A0, C4)', 15),
        ('[C4, C8)', 27),
        ])
    mapping_2 = pitchtools.OctaveTranspositionMapping([
        ('[A0, C8]', -18),
        ])
    inventory = pitchtools.OctaveTranspositionMappingInventory([
        mapping_1,
        mapping_2
        ])

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc OctaveTranspositionMappingInventory testoctavetrans'
        input_ += ' add add source [A0, C4) target 15 done'
        input_ += ' add source [C4, C8) target 27 done done'
        input_ += ' add add source [A0, C8] target -18 done'
        input_ += ' done done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == inventory
        input_ = 'm testoctavetrans rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_08():
    pytest.skip('make autoadding work again.')

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testlist',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]

    assert not os.path.exists(path)
    try:
        input_ = 'm nmm list testlist 17 foo done b default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == [17, 'foo']
        input_ = 'm testlist rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_09():

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testlist',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc list testlist add 17 add foo done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == [17, 'foo']
        input_ = 'm testlist rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_10():
    r'''Edits talea rhythm-maker.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testrhythmmaker',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    talea = rhythmmakertools.Talea(
        counts=(-1, 2, -3, 4),
        denominator=16,
        )
    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        split_divisions_by_counts=(6,),
        extra_counts_per_division=(2, 3),
        )

    assert not os.path.exists(path)
    try:
        input_ = 'm nmc TaleaRhythmMaker testrhythmmaker'
        input_ += ' talea counts (-1, 2, -3, 4) denominator 16 done'
        input_ += ' split (6,)'
        input_ += ' extra (2, 3)'
        input_ += ' done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == maker
        input_ = 'm testrhythmmaker rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_11():
    r'''Edits retierated articulation handler.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testarticulationhandler',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    handler = handlertools.ReiteratedArticulationHandler(
        articulation_list=['^', '.'],
        minimum_duration=Duration(1, 64),
        maximum_duration=Duration(1, 4),
        minimum_written_pitch=NamedPitch('c'),
        maximum_written_pitch=NamedPitch("c''''"),
        )

    assert not os.path.exists(path)
    try:
        input_ = "m nmc ReiteratedArticulationHandler testarticulationhandler"
        input_ += " al ['^', '.'] nd (1, 64) xd (1, 4) np c xp c''''"
        input_ += " done default q"
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == handler
        input_ = 'm testarticulationhandler rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageManager_edit_output_12():
    r'''Edits dynamic handler.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    configuration = score_manager._configuration
    path = os.path.join(
        configuration.user_library_material_packages_directory_path,
        'testdynamichandler',
        )
    assert not os.path.exists(path)
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'output.py',
        ]
    handler = handlertools.ReiteratedDynamicHandler(
        dynamic_name='f',
        minimum_duration=Duration(1, 16),
        )

    try:
        input_ = 'm nmc ReiteratedDynamicHandler testdynamichandler'
        input_ += ' dy f md (1, 16) done default q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.MaterialPackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        output_material = manager._execute_output_module()
        assert output_material == handler
        input_ = 'm testdynamichandler rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)

    assert not os.path.exists(path)