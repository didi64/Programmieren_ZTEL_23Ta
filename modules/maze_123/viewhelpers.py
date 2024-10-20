from ipywidgets import HBox, VBox, Button, Output
from ipycanvas import MultiCanvas
from IPython.display import display


class Mob():
    '''MultiCanvas with Output-Widget and Buttons'''
    layout = {'border': '1px solid black'}
    layout_bt = {'border': '1px solid black',
                 'width': '100px',
                 }
    layout_vbox = {'border': '1px solid black',
                   'justify_content': 'space-around',
                   }

    def __init__(self, nlayers=2, width=300, height=200, buttons=()):
        self.buttons = {name: Button(description=name, layout=self.layout_bt)
                        for name in buttons
                        }
        self.mcanvas = MultiCanvas(nlayers, width=width, height=height, layout=self.layout)
        self.out = Output(layout=self.layout)
        vbox = VBox(children=list(self.buttons.values()), layout=self.layout_vbox)
        self.mob = VBox(children=[HBox(children=[self.mcanvas, vbox]), self.out])

    def _ipython_display_(self):
        display(self.mob)