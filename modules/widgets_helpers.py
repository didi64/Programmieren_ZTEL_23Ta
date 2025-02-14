import warnings
from ipywidgets import Output, Text, Button
from ipycanvas import Canvas, MultiCanvas


# Deprecation Warnings unterdruecken
warnings.filterwarnings('ignore', category=DeprecationWarning)


LAYOUT_DFT = {'border': '1px solid black'}

LAYOUT_BT = {'border': '2px solid blue',
             'width': '80px',
             'height': '30px',
             }

LAYOUT_TEXT = {}


def new_output(layout=None):
    if layout is None:
        layout = LAYOUT_DFT
    out = Output(layout=layout)
    return out


def new_canvas(width=300, height=200, layout=None):
    if layout is None:
        layout = LAYOUT_DFT
    canvas = Canvas(width=width, height=height, layout=layout)
    return canvas


def new_mcanvas(n=2, width=300, height=200, layout=None):
    if layout is None:
        layout = LAYOUT_DFT
    mcanvas = MultiCanvas(n, width=width, height=height, layout=layout)
    return mcanvas


def new_button(description, layout=None):
    if layout is None:
        layout = LAYOUT_BT
    button = Button(description=description, layout=layout)
    return button


def new_text(value='', layout=None):
    if layout is None:
        layout = LAYOUT_TEXT
    text = Text(value=value, layout=layout)
    return text
