from abjad.tools.seqtools._split_sequence_by_weights import _split_sequence_by_weights


def split_sequence_cyclically_by_weights_with_overhang(sequence, weights):
   '''.. versionadded:: 1.1.2

   Split `sequence` cyclically by `weights` with overhang::

      abjad> seqtools.split_sequence_cyclically_by_weights_with_overhang((10, -10, 10, -10), [3, 15, 3])
      [(3,), (7, -8), (-2, 1), (3,), (6, -9), (-1,)]

   Return list of `sequence` types.
   '''

   return _split_sequence_by_weights(sequence, weights, cyclic = True, overhang = True)
