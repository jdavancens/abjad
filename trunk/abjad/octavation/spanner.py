from .. core.spanner import _Spanner

class Octavation(_Spanner):

   def __init__(self, music, start, stop = 0):
      _Spanner.__init__(self, music)
      self.start = start
      self.stop = stop

   ### TODO - test the shit out of the middleCPosition stuff, esp
   ###        clef changes in the middle of an octavation spanner

   def _before(self, leaf):
      result = [ ]
      position = leaf.clef.middleCPosition - 7 * self.start
      if self._isMyFirstLeaf(leaf):
         result.append(r'#(set-octavation %s)' % self.start)
      ### TODO - this is a ghetto way of checking for a clef change
      ###        maybe better to create a clef interface to hold info?
      if self._isMyFirstLeaf(leaf) or hasattr(leaf, '_clef'):
         position = leaf.clef.middleCPosition - 7 * self.start
         result.append(r'\set Staff.middleCPosition = #%s' % position)
      return result

   def _after(self, leaf):
      result = [ ]
      if self._isMyLastLeaf(leaf):
         result.append(r'#(set-octavation %s)' % self.stop)
         position = leaf.clef.middleCPosition - 7 * self.stop
         result.append(r'\set Staff.middleCPosition = #%s' % position)
      return result
