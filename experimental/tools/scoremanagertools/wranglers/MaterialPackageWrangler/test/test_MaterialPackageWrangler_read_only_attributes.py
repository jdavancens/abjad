import os
from experimental import *

score_manager = scoremanagertools.scoremanager.ScoreManager()
wrangler = score_manager.material_package_wrangler
assert not wrangler.session.is_in_score


def test_MaterialPackageWrangler_read_only_attributes_01():
    '''Breadcrumb.
    '''

    assert wrangler.breadcrumb == 'materials'


def test_MaterialPackageWrangler_read_only_attributes_02():
    '''Asset containers (all).
    '''

    assert 'materials' in wrangler.list_asset_container_package_paths()
    assert 'example_score_1.mus.materials' in wrangler.list_asset_container_package_paths()
    assert wrangler.configuration.score_manager_materials_directory_path in wrangler.list_asset_container_paths()
    directory_path = os.path.join(
        wrangler.configuration.scores_directory_path, 'example_score_1', 'mus', 'materials')
    assert directory_path in wrangler.list_asset_container_paths()


def test_MaterialPackageWrangler_read_only_attributes_03():
    '''Current asset container.
    '''

    assert wrangler.current_asset_container_package_path == 'materials'
    assert wrangler.current_asset_container_path == wrangler.configuration.score_manager_materials_directory_path


def test_MaterialPackageWrangler_read_only_attributes_04():
    '''Score-external asset container
    '''

    assert wrangler.list_score_external_asset_container_package_paths() == ['materials']
    assert wrangler.list_score_external_asset_container_paths() == \
        [wrangler.configuration.score_manager_materials_directory_path]


def test_MaterialPackageWrangler_read_only_attributes_05():
    '''Score-external assets.
    '''

    assert 'red notes' in wrangler.list_score_external_asset_space_delimited_lowercase_names()
    assert 'materials.red_notes' in wrangler.list_score_external_asset_package_paths()
    assert os.path.join(wrangler.configuration.score_manager_materials_directory_path, 'red_notes') in \
        wrangler.list_score_external_asset_paths()


def test_MaterialPackageWrangler_read_only_attributes_06():
    '''Infix.
    '''

    assert wrangler.score_internal_asset_container_package_path_infix == 'mus.materials'


def test_MaterialPackageWrangler_read_only_attributes_07():
    '''Temporary asset.
    '''

    assert wrangler.temporary_asset_package_path == 'materials.__temporary_package'
    assert wrangler.temporary_asset_path == \
        os.path.join(wrangler.configuration.score_manager_materials_directory_path, '__temporary_package')
    assert wrangler.temporary_asset_name == '__temporary_package'


def test_MaterialPackageWrangler_read_only_attributes_08():
    '''In-score wrangler.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    wrangler = score_manager.material_package_wrangler
    wrangler.session.current_score_package_name = 'example_score_1'
    assert wrangler.session.is_in_score

    assert 'example_score_1.mus.materials' in wrangler.list_asset_container_package_paths()
    assert wrangler.current_asset_container_package_path == 'example_score_1.mus.materials'
    assert wrangler.temporary_asset_package_path == 'example_score_1.mus.materials.__temporary_package'
    directory_path = os.path.join(
         wrangler.configuration.scores_directory_path, 
        'example_score_1', 'mus', 'materials', '__temporary_package')
    assert wrangler.temporary_asset_path == directory_path
