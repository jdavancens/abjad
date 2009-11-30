import cPickle


def dump(data, file_name):
   '''Easy interface to Python cPickle persistence module.

   ::

      abjad> t = Note(0, (1, 4))
      abjad> f(t)
      c'4
      abjad> pickle.dump(t, 'temp.pkl')

   ::

      abjad> new = pickle.load('temp.pkl') 
      abjad> new
      Note(c', 4)
   '''

   f = open(file_name, 'w')
   cPickle.dump(data, f)
   f.close( )
