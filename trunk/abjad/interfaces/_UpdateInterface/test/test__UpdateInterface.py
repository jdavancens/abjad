from abjad import *


def test__UpdateInterface_01( ):
   '''For newly instantiated notes:
   neither prolated offset values nor observer interfaces are current.
   '''

   t = Note(0, (1, 4))
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current
   
   t.offset.start
   assert t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current

   t.meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current
   

def test__UpdateInterface_02( ):
   '''Newly instantiated containers are not current.'''

   t = Voice(macros.scale(4))
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current

   t[-1].offset.start
   assert t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current

   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current


def test__UpdateInterface_03( ):
   '''Copied notes are not current.'''

   t = Note(0, (1, 4))
   t.offset.start
   new = componenttools.clone_components_and_remove_all_spanners([t])[0]
   assert not new._update._prolated_offset_values_of_component_are_current
   assert not new._update._current


def test__UpdateInterface_04( ):
   '''Copied containers are not current.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   new = componenttools.clone_components_and_remove_all_spanners([t])[0]
   assert not new._update._prolated_offset_values_of_component_are_current
   assert not new._update._current


def test__UpdateInterface_05( ):
   '''Container deletion marks all components in parentage for update.'''

   t = Voice(macros.scale(4))

   t[-1].offset.start
   assert t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current

   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current

   del(t[1])
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current


def test__UpdateInterface_06( ):
   '''Container insert marks all components in parentage for update.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current
   
   t.insert(1, Note(1, (1, 16)))
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current


def test__UpdateInterface_07( ):
   '''Container append marks components in parentage for update.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current

   t.append(Note(7, (1, 8)))
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current


def test__UpdateInterface_08( ):
   '''Container extend marks components in parentage for update.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current

   t.extend([Note(7, (1, 8)), Note(9, (1, 8))])
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current


def test__UpdateInterface_09( ):
   '''Container pop marks components in parentage for update.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current

   t.pop( )
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current


def test__UpdateInterface_10( ):
   '''Container remove marks components in parentage for update.'''

   t = Voice(macros.scale(4))
   t[-1].offset.start
   t[-1].meter.effective
   assert t._update._prolated_offset_values_of_component_are_current
   #assert t._update._current

   t.remove(t[1])
   assert not t._update._prolated_offset_values_of_component_are_current
   assert not t._update._current
