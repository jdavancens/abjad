lilypond_version = "2.17.9"

markup_functions = {
    'abs-fontsize': ('number?', 'cheap-markup?',),
    'arrow-head': ('integer?', 'ly:dir?', 'boolean?',),
    'auto-footnote': ('cheap-markup?', 'cheap-markup?',),
    'backslashed-digit': ('integer?',),
    'beam': ('number?', 'number?', 'number?',),
    'bold': ('cheap-markup?',),
    'box': ('cheap-markup?',),
    'bracket': ('cheap-markup?',),
    'caps': ('cheap-markup?',),
    'center-align': ('cheap-markup?',),
    'center-column': ('markup-list?',),
    'char': ('integer?',),
    'circle': ('cheap-markup?',),
    'column': ('markup-list?',),
    'combine': ('cheap-markup?', 'cheap-markup?',),
    'concat': ('markup-list?',),
    'customTabClef': ('integer?', 'number?',),
    'dir-column': ('markup-list?',),
    'doubleflat': (),
    'doublesharp': (),
    'draw-circle': ('number?', 'number?', 'boolean?',),
    'draw-hline': (),
    'draw-line': ('number-pair?',),
    'dynamic': ('cheap-markup?',),
    'epsfile': ('number?', 'number?', 'string?',),
    'eyeglasses': (),
    'fill-line': ('markup-list?',),
    'fill-with-pattern': ('number?', 'ly:dir?', 'cheap-markup?', 'cheap-markup?', 'cheap-markup?',),
    'filled-box': ('number-pair?', 'number-pair?', 'number?',),
    'finger': ('cheap-markup?',),
    'flat': (),
    'fontCaps': ('cheap-markup?',),
    'fontsize': ('number?', 'cheap-markup?',),
    'footnote': ('cheap-markup?', 'cheap-markup?',),
    'fraction': ('cheap-markup?', 'cheap-markup?',),
    'fret-diagram': ('string?',),
    'fret-diagram-terse': ('string?',),
    'fret-diagram-verbose': ('pair?',),
    'fromproperty': ('symbol?',),
    'general-align': ('integer?', 'number?', 'cheap-markup?',),
    'halign': ('number?', 'cheap-markup?',),
    'harp-pedal': ('string?',),
    'hbracket': ('cheap-markup?',),
    'hcenter-in': ('number?', 'cheap-markup?',),
    'hspace': ('number?',),
    'huge': ('cheap-markup?',),
    'italic': ('cheap-markup?',),
    'justify-field': ('symbol?',),
    'justify': ('markup-list?',),
    'justify-string': ('string?',),
    'large': ('cheap-markup?',),
    'larger': ('cheap-markup?',),
    'left-align': ('cheap-markup?',),
    'left-brace': ('number?',),
    'left-column': ('markup-list?',),
    'line': ('markup-list?',),
    'lookup': ('string?',),
    'lower': ('number?', 'cheap-markup?',),
    'magnify': ('number?', 'cheap-markup?',),
    'markalphabet': ('integer?',),
    'markletter': ('integer?',),
    'medium': ('cheap-markup?',),
    'musicglyph': ('string?',),
    'natural': (),
    'normal-size-sub': ('cheap-markup?',),
    'normal-size-super': ('cheap-markup?',),
    'normal-text': ('cheap-markup?',),
    'normalsize': ('cheap-markup?',),
    'note-by-number': ('number?', 'number?', 'number?',),
    'note': ('string?', 'number?',),
    'null': (),
    'number': ('cheap-markup?',),
    'on-the-fly': ('procedure?', 'cheap-markup?',),
    'override': ('pair?', 'cheap-markup?',),
    'pad-around': ('number?', 'cheap-markup?',),
    'pad': ('number?', 'cheap-markup?',),
    'pad-to-box': ('number-pair?', 'number-pair?', 'cheap-markup?',),
    'pad-x': ('number?', 'cheap-markup?',),
    'page-link': ('number?', 'cheap-markup?',),
    'page-ref': ('symbol?', 'cheap-markup?', 'cheap-markup?',),
    'parenthesize': ('cheap-markup?',),
    'path': ('number?', 'list?',),
    'pattern': ('integer?', 'integer?', 'number?', 'cheap-markup?',),
    'postscript': ('string?',),
    'property-recursive': ('symbol?',),
    'put-adjacent': ('integer?', 'ly:dir?', 'cheap-markup?', 'cheap-markup?',),
    'raise': ('number?', 'cheap-markup?',),
    'replace': ('list?', 'cheap-markup?',),
    'rest-by-number': ('number?', 'number?',),
    'rest': ('string?',),
    'right-align': ('cheap-markup?',),
    'right-brace': ('number?',),
    'right-column': ('markup-list?',),
    'roman': ('cheap-markup?',),
    'rotate': ('number?', 'cheap-markup?',),
    'rounded-box': ('cheap-markup?',),
    'sans': ('cheap-markup?',),
    'scale': ('number-pair?', 'cheap-markup?',),
    'score': ('ly:score?',),
    'semiflat': (),
    'semisharp': (),
    'sesquiflat': (),
    'sesquisharp': (),
    'sharp': (),
    'simple': ('string?',),
    'slashed-digit': ('integer?',),
    'small': ('cheap-markup?',),
    'smallCaps': ('cheap-markup?',),
    'smaller': ('cheap-markup?',),
    'stencil': ('ly:stencil?',),
    'strut': (),
    'sub': ('cheap-markup?',),
    'super': ('cheap-markup?',),
    'teeny': ('cheap-markup?',),
    'text': ('cheap-markup?',),
    'tied-lyric': ('string?',),
    'tiny': ('cheap-markup?',),
    'translate': ('number-pair?', 'cheap-markup?',),
    'translate-scaled': ('number-pair?', 'cheap-markup?',),
    'transparent': ('cheap-markup?',),
    'triangle': ('boolean?',),
    'typewriter': ('cheap-markup?',),
    'underline': ('cheap-markup?',),
    'upright': ('cheap-markup?',),
    'vcenter': ('cheap-markup?',),
    'verbatim-file': ('string?',),
    'vspace': ('number?',),
    'whiteout': ('cheap-markup?',),
    'with-color': ('color?', 'cheap-markup?',),
    'with-dimensions': ('number-pair?', 'number-pair?', 'cheap-markup?',),
    'with-link': ('symbol?', 'cheap-markup?',),
    'with-url': ('string?', 'cheap-markup?',),
    'woodwind-diagram': ('symbol?', 'list?',),
    'wordwrap-field': ('symbol?',),
    'wordwrap': ('markup-list?',),
    'wordwrap-string': ('string?',),
}

markup_list_functions = {
    'column-lines': ('markup-list?',),
    'justified-lines': ('markup-list?',),
    'override-lines': ('pair?', 'markup-list?',),
    'table-of-contents': (),
    'wordwrap-internal': ('boolean?', 'markup-list?',),
    'wordwrap-lines': ('markup-list?',),
    'wordwrap-string-internal': ('boolean?', 'string?',),
}
