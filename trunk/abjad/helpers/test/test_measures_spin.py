from abjad import *


def test_measures_spin_01( ):
   '''Spin one measure out three times.'''

   t = RigidMeasure((3, 8), scale(3))
   measures_spin(t, 3)

   r'''
        \time 9/8
        c'8
        d'8
        e'8
        c'8
        d'8
        e'8
        c'8
        d'8
        e'8
   '''

   assert check(t)
   assert t.format == "\t\\time 9/8\n\tc'8\n\td'8\n\te'8\n\tc'8\n\td'8\n\te'8\n\tc'8\n\td'8\n\te'8"


def test_spin_measures_02( ):
   '''Spin multiples measures out twice each.'''

   t = Staff(RigidMeasure((2, 8), run(2)) * 3)
   diatonicize(t)
   
   r'''
   \new Staff {
                   \time 2/8
                   c'8
                   d'8
                   \time 2/8
                   e'8
                   f'8
                   \time 2/8
                   g'8
                   a'8
   }
   '''

   measures_spin(t, 2)

   r'''
   \new Staff {
                   \time 4/8
                   c'8
                   d'8
                   c'8
                   d'8
                   \time 4/8
                   e'8
                   f'8
                   e'8
                   f'8
                   \time 4/8
                   g'8
                   a'8
                   g'8
                   a'8
   }
   '''

   assert check(t)
   assert t.format == "\\new Staff {\n\t\t\\time 4/8\n\t\tc'8\n\t\td'8\n\t\tc'8\n\t\td'8\n\t\t\\time 4/8\n\t\te'8\n\t\tf'8\n\t\te'8\n\t\tf'8\n\t\t\\time 4/8\n\t\tg'8\n\t\ta'8\n\t\tg'8\n\t\ta'8\n}"
