from abjad import *
from abjad.helpers.get_contained_spanners import _get_contained_spanners
import py.test


def test_get_contained_spanners_01( ):
   '''Return unordered set of spanners contained
      within any of the list of thread-contiguous components.'''

   t = Voice(Sequential(run(2)) * 2)
   diatonicize(t)
   beam = Beam(t[0][:])
   slur = Slur(t[1][:])
   trill = Trill(t.leaves)

   r'''\new Voice {
           {
                   c'8 [ \startTrillSpan
                   d'8 ]
           }
           {
                   e'8 (
                   f'8 ) \stopTrillSpan
           }
   }'''

   spanners = _get_contained_spanners([t])
   assert len(spanners) == 3
   assert beam in spanners
   assert slur in spanners
   assert trill in spanners

   spanners = _get_contained_spanners(t.leaves)
   assert len(spanners) == 3
   assert beam in spanners
   assert slur in spanners
   assert trill in spanners

   spanners = _get_contained_spanners(t[0:1])
   assert len(spanners) == 2
   assert beam in spanners
   assert trill in spanners

   spanners = _get_contained_spanners(t.leaves[0:1])
   assert len(spanners) == 2
   assert beam in spanners
   assert trill in spanners


def test_get_contained_spanners_02( ):
   '''Trying to get contained spanners across 
      non-thread-contiguous components raises ContiguityError.'''

   t = Sequential(Voice(run(2)) * 2)
   diatonicize(t)
   Beam(t.leaves[:2])
   Slur(t.leaves[2:])
   
   r'''{
           \new Voice {
                   c'8 [
                   d'8 ]
           }
           \new Voice {
                   e'8 (
                   f'8 )
           }
   }'''
   
   assert py.test.raises(ContiguityError, '_get_contained_spanners(t.leaves)')
