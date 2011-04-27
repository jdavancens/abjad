from abjad.components import Tuplet
from abjad.tools.componenttools.iterate_components_forward_in_expr import iterate_components_forward_in_expr


def iterate_tuplets_forward_in_expr(expr, start = 0, stop = None):
   r'''.. versionadded:: 1.1.2

   Iterate tuplets forward in `expr`::

      abjad> staff = Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
      abjad> Tuplet((2, 3), staff[:3])
      abjad> Tuplet((2, 3), staff[-3:])

      abjad> f(staff)
      \new Staff {
         \times 2/3 {
            c'8
            d'8
            e'8
         }
         f'8
         g'8
         \times 2/3 {
            a'8
            b'8
            c''8
         }
      }

      abjad> for tuplet in tuplettools.iterate_tuplets_forward_in_expr(staff):
      ...     tuplet
      ... 
      Tuplet(2/3, [c'8, d'8, e'8])
      Tuplet(2/3, [a'8, b'8, c''8])

   Return generator.
   '''

   return iterate_components_forward_in_expr(expr, Tuplet, start = start, stop = stop)
