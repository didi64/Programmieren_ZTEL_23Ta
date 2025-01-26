import widgets_helpers
from IPython.display import display
from canvas_callbacks import remove_all_callbacks


class KeyMouseController:
    err_out = widgets_helpers.new_output()

    def __init__(self, game, canvas, remove_callbacks=True):
        self.game = game
        self.canvas = canvas
        self.src = None

        if remove_all_callbacks:
            remove_all_callbacks(self.canvas)

        self.canvas.on_key_down(self.on_key_down)
        self.canvas.on_mouse_down(self.on_mouse_down)
        self.canvas.on_mouse_up(self.on_mouse_up)

    @err_out.capture()
    def on_key_down(self, key, *flags):
        if key in '123' and self.src is None:
            self.src = int(key) - 1
            return
        elif key in '123':
            dst = int(key) - 1
            self.game.move_disk(self.src, dst)
        elif key == 'n':
            self.game.new_game()
        self.src = None

    @err_out.capture()
    def on_mouse_down(self, x, y):
        stack_width = self.canvas.width / 3
        self.src = int(x // stack_width)

    @err_out.capture()
    def on_mouse_up(self, x, y):
        if self.src is None:
            return

        stack_width = self.canvas.width / 3
        dst = int(x // stack_width)
        self.game.move_disk(self.src, dst)
        self.src = None

    def _ipython_display_(self):
        display(self.canvas, self.err_out)