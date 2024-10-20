'''
all functions that draw on the canvas take kwargs
keywords are the canvas attributes such as 'line_width', 'fill_style', 'stroke_style', ...
'''


from ipycanvas import hold_canvas
from functools import wraps
from vec2d import Vec2d as Vec


def keep_ATTRS(attrs=None):
    '''attrs: Iterable
       decorator for functions f(canvas, ...) that draw on a canvas object
       saves and restores all drawing attributs, or the
       the attributes provided by the iterable attrs
    '''
    def decorator(f):
        @wraps(f)
        def wrapper(canvas, *args, **kwargs):
            nonlocal attrs
            if attrs is None:
                attrs = canvas.ATTRS
            cfg = {attr: getattr(canvas, attr) for attr in attrs}
            res = f(canvas, *args, **kwargs)
            for attr, val in cfg.items():
                setattr(canvas, attr, val)
            return res
        return wrapper
    return decorator


@keep_ATTRS()
def draw_arrowtip(canvas, pos, width=None, height=None, alpha=0, fill=True, **kwargs):
    '''draws an arrowtip
       returns a bounding box (x, y, width, height)
    '''
    if width is None and height is None:
        width, height = canvas.width / 50, canvas.height / 50 * 1.5
    elif width is None and height is not None:
        width = height / 1.5
    elif height is None and width is not None:
        height = width * 1.5

    for k, v in kwargs.items():
        setattr(canvas, k, v)
    drawers = {True: canvas.fill_polygon, False: canvas.stroke_polygon}
    drawer = drawers[fill]
    pos = Vec(*pos)
    arrow = [Vec(0, width/2), Vec(height, 0), Vec(0, -width/2)]
    arrow_transformed = [pt.rotate(-alpha) + pos for pt in arrow]
    drawer(arrow_transformed)
    pos, w, h = Vec.bbox(arrow_transformed)
    rect = *pos, w, h
    return rect


def get_transforminfo(pos, width, height, nrows, ncols):
    '''returns a dict with transformation infos, see source'''
    dx = width / ncols
    dy = height / nrows

    def colrow2xy(col, row):
        return (pos[0] + col*dx, pos[1] + row*dy)

    def xy2colrow(x, y):
        return int((x - pos[0]) // dx), int((y - pos[1]) // dy)

    transform_info = {'pos': pos,
                      'width': width,
                      'height': height,
                      'nrows': nrows,
                      'ncols': ncols,
                      'dx': dx,
                      'dy': dy,
                      'colrow2xy': colrow2xy,
                      'xy2colrow': xy2colrow,
                      }
    return transform_info


@keep_ATTRS()
def draw_chessboard(canvas, pos, width, height=None,
                    ncols=8, nrows=None, colors=None, **kwargs):
    '''draws a chessbord:
       colors: function f(col, row) -> color
    '''
    if colors is None or type(colors) is tuple:
        opts = colors or ('#F0D9B5', '#B48762')

        def colors(col, row):
            color = opts[(col+row) % 2]
            return color

    if height is None:
        height = width

    if nrows is None:
        nrows = ncols

    for k, v in kwargs.items():
        setattr(canvas, k, v)

    trans_info = get_transforminfo(pos, width, height, nrows, ncols)
    dx, dy, colrow2xy = trans_info['dx'], trans_info['dy'], trans_info['colrow2xy']
    with hold_canvas():
        for i in range(ncols):
            for j in range(nrows):
                color = colors(i, j)
                canvas.fill_style = color
                canvas.fill_rect(*colrow2xy(i, j), dx, dy)

    return trans_info


@keep_ATTRS()
def draw_grid(canvas, pos, width, height=None, ncols=8, nrows=None, **kwargs):
    '''draw grid lines'''
    if height is None:
        height = width
    if nrows is None:
        nrows = ncols
    for k, v in kwargs.items():
        setattr(canvas, k, v)

    trans_info = get_transforminfo(pos, width, height, nrows, ncols)
    colrow2xy = trans_info['colrow2xy']
    with hold_canvas():
        # vertical lines
        for i in range(ncols + 1):
            canvas.stroke_lines([colrow2xy(i, 0), colrow2xy(i, nrows)])
        # horizontal lines
        for j in range(nrows + 1):
            canvas.stroke_lines([colrow2xy(0, j), colrow2xy(ncols, j)])

    trans_info = get_transforminfo(pos, width, height, nrows, ncols) 
    return trans_info


@keep_ATTRS()
def draw_pts(canvas, pos, width, height=None, radius=2,
             nrows=8, ncols=8, **kwargs):
    '''draws grid points'''
    if height is None:
        height = width

    for k, v in kwargs.items():
        setattr(canvas, k, v)

    trans_info = get_transforminfo(pos, width, height, nrows, ncols)
    colrow2xy = trans_info['colrow2xy']

    with hold_canvas():
        for i in range(ncols+1):
            for j in range(nrows+1):
                canvas.fill_circle(*colrow2xy(i, j), radius)