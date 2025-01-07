def draw_CH_flag(canvas, pos, size):
    '''CH Flagge, quadratisch,
       Langes Kreuz: 2/3 * size, Balkenhoehe 1/5 * size
    '''
    x0, y0 = pos
    # rote Grundierung
    canvas.fill_style = 'red'
    canvas.fill_rect(x0, y0, size)

    # weisses Kreuz
    canvas.fill_style = 'white'

    # verticaler Streifen
    bar_width = size/5
    bar_height = 2/3 * size
    canvas.fill_rect(x0 + 4*size/10,
                     y0 + size/6,
                     width=bar_width,
                     height=bar_height,
                     )
    # horizontaler Streifen
    canvas.fill_rect(x0 + size/6,
                     y0 + 4*size/10,
                     width=bar_height,
                     height=bar_width,
                     )


def draw_BRD_flag(canvas, pos, size):
    '''BRD Flagge: Seitenverhaeltnis Hoehe:Breite = 3:5,
       3 horizontale Streifen: schwarz, gel, rot
    '''
    x0, y0 = pos
    canvas.fill_style = 'gray'
    canvas.fill_rect(x0, y0, size)

    for i, color in [(1, 'black'), (2, 'red'), (3, 'yellow')]:
        canvas.fill_style = color
        canvas.fill_rect(x0, y0 + i/5 * size, width=size, height=size/5)


def draw_BE_flag(canvas, pos, size):
    '''Be Flagge: Seitenverhaeltnis Hoehe:Breite = 13:15,
       3 vertikale Streifen: schwarz, gelb, rot
    '''
    x0, y0 = pos
    canvas.fill_style = 'gray'
    canvas.fill_rect(x0, y0, size)

    for i, color in enumerate(('black', 'yellow', 'red')):
        canvas.fill_style = color
        x = x0 + i/3 * size
        y = y0 + 1/15 * size
        canvas.fill_rect(x, y, width=size/3, height=13/15*size)