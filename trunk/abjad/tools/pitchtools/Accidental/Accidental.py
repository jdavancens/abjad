from abjad.core import _Abjad


class Accidental(_Abjad):
   '''Abjad model of the accidental:

   ::

      abjad> pitchtools.Accidental('s')
      Accidental(sharp)
   '''

   def __init__(self, arg = ''):
      if arg in self._alphabetic_strings:
         self._alphabetic_string = arg
      elif arg in self._symbolic_strings:
         alphabetic_string = self._symbolic_string_to_alphabetic_string[arg]
         self._alphabetic_string = alphabetic_string
      elif arg in self._names:
         alphabetic_string = self._name_to_alphabetic_string[arg]
         self._alphabetic_string = alphabetic_string
      elif arg in self._semitones:
         alphabetic_string = self._semitones_to_alphabetic_string[arg]
         self._alphabetic_string = alphabetic_string
      elif isinstance(arg, Accidental):
         self._alphabetic_string = arg.alphabetic_string 
      elif isinstance(arg, type(None)):
         self._alphabetic_string = ''
      else:
         raise ValueError('can not initialize accidental from value: %s' % arg)

   ## OVERLOADS ##

   def __add__(self, arg):
      if not isinstance(arg, type(self)):
         raise TypeError('can only add accidental to other accidental.')
      semitones = self.semitones + arg.semitones
      return Accidental(semitones)

   def __eq__(self, arg):
      if isinstance(arg, type(self)):
         if self.alphabetic_string == arg.alphabetic_string:
            return True
      return False

   def __ge__(self, arg):
      return self.semitones >= arg.semitones

   def __gt__(self, arg):
      return self.semitones > arg.semitones
   
   def __le__(self, arg):
      return self.semitones <= arg.semitones

   def __lt__(self, arg):
      return self.semitones < arg.semitones
   
   def __ne__(self, arg):
      return not self == arg

   def __neg__(self):
      return Accidental(-self.semitones)

   def __nonzero__(self):
      return True

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self.name)

   def __str__(self):
      return self.alphabetic_string

   def __sub__(self, arg):
      if not isinstance(arg, type(self)):
         raise TypeError('can only sub accidental from other accidental.')
      semitones = self.semitones - arg.semitones
      return Accidental(semitones)

   ## PRIVATE ATTRIBUTES ##

   @property
   def _alphabetic_strings(self):
      return self._alphabetic_string_to_symbolic_string.keys( )

   _alphabetic_string_to_name = {
      'ss'  : 'double sharp',
      'tqs' : 'three-quarters sharp',
      's'   : 'sharp',
      'qs'  : 'quarter-sharp',
      ''    : 'natural',
      '!'   : 'forced natural',
      'qf'  : 'quarter-flat',
      'f'   : 'flat',
      'tqf' : 'three-quarters flat',
      'ff'  : 'double flat',
   }

   _alphabetic_string_to_semitones = {
        '': 0,      '!': 0,
      'ff': -2,   'tqf': -1.5, 
       'f': -1,    'qf': -0.5,
      'ss': 2,    'tqs': 1.5,
       's': 1,     'qs': 0.5,
   }

   _alphabetic_string_to_symbolic_string = {
        '': '',       '!': '!',
      'ff': 'bb',   'tqf': 'b+', 
       'f': 'b',     'qf': 'b-',
      'ss': '##',   'tqs': '#+',
       's': '#',     'qs': '#-',
   }

   _name_to_alphabetic_string = {
      'double sharp'          : 'ss',
      'three-quarters sharp'  : 'tqs',
      'sharp'                 : 's',
      'quarter sharp'         : 'qs',
      'natural'               : '',
      'forced natural'        : '!',
      'quarter flat'          : 'qf',
      'flat'                  : 'f',
      'three-quarters flat'   : 'tqf',
      'double flat'           :  'ff',
   }

   _semitones_to_alphabetic_string = {
       0: '',
      -2: 'ff',   -1.5: 'tqf',   
      -1: 'f',    -0.5: 'qf',
       2: 'ss',    1.5: 'tqs',    
       1: 's',     0.5: 'qs',
    -2.5: 'ff',
   }

   _symbolic_string_to_alphabetic_string = {
        '': '',       '!': '!',
      'bb': 'ff',   'b+': 'tqf', 
       'b': 'f',     'b-': 'qf',
      '##': 'ss',   '#+': 'tqs',
       '#': 's',     '#-': 'qs',
   }

   @property
   def _names(self):
      return self._name_to_alphabetic_string.keys( )

   @property
   def _semitones(self):
      return self._semitones_to_alphabetic_string.keys( )

   @property
   def _symbolic_strings(self):
      return self._symbolic_string_to_alphabetic_string.keys( )

   ## PUBLIC ATTRIBUTES ##

   @apply
   def alphabetic_string( ):
      def fget(self):
         '''Read / write alphabetic string of accidental:
      
         ::
      
            abjad> accidental = pitchtools.Accidental('s')
            abjad> accidental.alphabetic_string
            's'
         '''
         return self._alphabetic_string
      return property(**locals( ))

   @property
   def format(self):
      '''Read-only LilyPond format of accidental:

      ::
   
         abjad> accidental = pitchtools.Accidental('s')
         abjad> accidental.format
         's' 

      Defined equal to the alphabetic string of accidental.
      '''
      return self.alphabetic_string

   @property
   def is_adjusted(self):
      '''Read-only adjustment indicator of accidental:

      ::

         abjad> accidental = pitchtools.Accidental('s')
         abjad> accidental.is_adjusted
         True

      True for all accidentals equal to a nonzero number of semitones.
      '''
      return not self.semitones == 0

   @property
   def name(self):
      '''Read-only name of accidental:

      ::

         abjad> accidental = pitchtools.Accidental('s')
         abjad> accidental.name
         'sharp'
      '''
      return self._alphabetic_string_to_name[self.alphabetic_string]

   @property
   def semitones(self):
      '''Read-only number of semitones to which accidental is equal:

      ::

         abjad> accidental = pitchtools.Accidental('s')
         abjad> accidental.semitones
         1
      '''
      return self._alphabetic_string_to_semitones[self.alphabetic_string]

   @property
   def symbolic_string(self):
      '''Read-only symbolic string of accidental:

      ::

         abjad> accidental = pitchtools.Accidental('s')
         abjad> accidental.symbolic_string
         '#'
      '''
      symbolic_string = self._alphabetic_string_to_symbolic_string[
         self.alphabetic_string]
      return symbolic_string
