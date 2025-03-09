import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from ipywidgets import  HBox, VBox, IntSlider, Text
from widgets_helpers import new_button, new_output
from IPython.display import display


class Controller:
    err_out = new_output()

    def __init__(self, game):
        self.game = game
        self.betsize = 10
        self.name = None

        self.text = Text(description='register:', placeholder='Name, bankroll')
        self.text.on_submit(self.register)
        
        self.intslider = IntSlider(10, min=10, max=50, step=10)
        self.intslider.observe(self.update_betsize, names='value')
        self.err_out.clear_output()
        
        #self.button_register = new_button(description='register')
        self.button_play = new_button(description=f'play ({self.name}, {self.betsize})')
        self.button_play.layout.width = 'auto'
        self.button_hit = new_button(description='hit')
        self.button_stay = new_button(description='stay')
        
        self.intslider = IntSlider(10, min=10, max=50, step=10)
        self.intslider.observe(self.update_betsize, names='value')


        # Buttons und Slider nebeneinander legen
        self.hbox = HBox(children=[self.button_play,
                                   self.intslider,
                                   self.button_hit,
                                   self.button_stay]
                         )

        self.app = VBox([self.text, self.hbox])
                                   
        #self.button_register.on_click(self.register)
        self.button_play.on_click(self.play)
        self.button_hit.on_click(self.hit)
        self.button_stay.on_click(self.stay)

    @err_out.capture()
    def update_betsize(self, change):
        self.betsize = change.new
        self.button_play.description = f'play ({self.name}, {self.betsize})'
    
    @err_out.capture()
    def register(self, text):
        self.name, bankroll = text.value.split(',')
        self.bankroll = int(bankroll) if bankroll.strip().isdigit() else None
        self.button_play.description=f'play ({self.name}, {self.betsize})'
        self.game.register(self.name, self.bankroll)
    
    @err_out.capture()
    def play(self, bt):
        self.game.play(self.betsize)
    
    
    @err_out.capture()
    def hit(self, bt):
        self.game.hit()
    
    
    @err_out.capture()
    def stay(self, bt):
        self.game.stay()

    def _ipython_display_(self):
        display(self.app, self.err_out)
