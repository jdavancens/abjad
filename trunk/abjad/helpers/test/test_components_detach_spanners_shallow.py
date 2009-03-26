from abjad import *
from abjad.helpers.components_detach_spanners_shallow import \
   _components_detach_spanners_shallow


def test_components_detach_spanners_shallow_01( ):
   t = Staff(scale(4))
   Beam(t[:])
   _components_detach_spanners_shallow(t[:])

   r'''
   \new Staff {
      c'8
      d'8
      e'8
      f'8
   }
   '''

   assert check(t)
   assert t.format == "\\new Staff {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"


def test_components_detach_spanners_shallow_02( ):
   t = Staff(scale(4))
   Beam(t[:])
   _components_detach_spanners_shallow(t[0:2])

   r'''
   \new Staff {
      c'8
      d'8 
      e'8 [
      f'8 ]
   }
   '''

   assert check(t)
   assert t.format == "\\new Staff {\n\tc'8\n\td'8\n\te'8 [\n\tf'8 ]\n}"


def test_components_detach_spanners_shallow_03( ):
   t = _components_detach_spanners_shallow([ ])
   assert t == [ ]
