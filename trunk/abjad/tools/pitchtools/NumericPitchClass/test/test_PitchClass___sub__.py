from abjad import *
import py.test


def test_PitchClass___sub___01( ):
   '''Subtracting one pitch class from another.'''

   pc1 = pitchtools.NumericPitchClass(6)
   pc2 = pitchtools.NumericPitchClass(7)

   assert pc1 - pc2 == pitchtools.IntervalClass(1)
   assert pc2 - pc1 == pitchtools.IntervalClass(1)


def test_PitchClass___sub___02( ):
   '''Subtracting an interval class from a pitch class.'''

   pc = pitchtools.NumericPitchClass(0)
   ic = pitchtools.IntervalClass(2)

   assert pc - ic == pitchtools.NumericPitchClass(10)
   assert py.test.raises(TypeError, 'ic - pc')
