import widgets_helpers
from IPython.display import display


class Controller:
    err_out = widgets_helpers.new_output()

    def __init__(self, game):
        self.game = game
        self.canvas = widgets_helpers.new_canvas(200, 30)
        self.canvas.font = '20px sans-serif'
        self.canvas.fill_text('listening for keys', 10, 20)
        self.canvas.on_key_down(self.on_key_down)

    @err_out.capture(clear_output=True)
    def on_key_down(self, key, *flags):
        if key == 'n':
            self.game.new_game()

        if key.startswith('Arrow'):
            move = key.removeprefix('Arrow').lower()
            self.game.move(move)

    def _ipython_display_(self):
        display(self.canvas, self.err_out)
