_ESC = chr(27)
_fmt = '[22;{}m'
_colors = ['black', 'red', 'green', 'yellow', 
          'blue', 'magenta', 'cyan', 'silver',
          ]
_variants = [(30, ''), (90, '_bright')]
reset = _ESC + '[0m'


def _make_colordicts():
    fg = {}
    bg = {}
    for i, color in enumerate(_colors):
        for code, suffix in _variants:
            fg[color+suffix] = _ESC + _fmt.format(code+i)
            bg[color+suffix] = _ESC + _fmt.format(code+10+i)
    return fg, bg


fgcolor_ANSIesc, bgcolor_ANSIesc = _make_colordicts()
