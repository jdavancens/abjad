from abjad.tools.datastructuretools.ObjectInventory import ObjectInventory
from experimental import helpertools
from experimental.settingtools.MultipleContextSetting import MultipleContextSetting


class MultipleContextSettingInventory(ObjectInventory):
    r'''.. versionadded:: 1.0

    MultipleContextSetting inventory.
    '''

    ### CLASS ATTRIBUTES ###

    attributes = helpertools.AttributeNameEnumeration()

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _item_callable(self):
        return MultipleContextSetting
