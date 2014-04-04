# -*- encoding: utf-8 -*-
from abjad import *
from scoremanager.managers.MaterialPackageManager import MaterialPackageManager


class OctaveTranspositionMappingInventoryMaterialManager(MaterialPackageManager):
    r'''Octave transposition mapping inventory material manager.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(self, path=None, session=None):
        superclass = super(
            OctaveTranspositionMappingInventoryMaterialManager,
            self,
            )
        superclass.__init__(path=path, session=session)
        self._output_module_import_statements = [
            self._abjad_import_statement,
            ]

    ### PUBLIC METHODS ###

    @staticmethod
    def _check_output_material(material):
        return isinstance(
            material,
            pitchtools.OctaveTranspositionMappingInventory,
            )

    def _get_output_material_editor(self, target=None):
        from scoremanager import iotools
        target = target or pitchtools.OctaveTranspositionMappingInventory()
        editor = iotools.ListEditor(
            session=self._session,
            target=target,
            )
        return editor

    def _make_output_material(self):
        return pitchtools.OctaveTranspositionMappingInventory