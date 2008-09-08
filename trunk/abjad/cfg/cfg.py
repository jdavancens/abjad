from os import environ

ABJADPATH = environ.get('ABJADPATH', '/home/abjad/')
ABJADPERSISTENCE = environ.get('ABJADPERSISTENCE', '/home/abjab/persistence/')
ABJADOUTPUT = environ.get('ABJADOUTPUT', '/home/abjad/output/')
VERSIONFILE = ABJADOUTPUT + '.version'
PDFVIEWER = environ.get('PDFVIEWER', 'open')
LILYPONDINCLUDES = environ.get('LILYPONDINCLUDES', None)
