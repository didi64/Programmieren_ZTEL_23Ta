import widgets_helpers
from IPython.display import display
from canvas_helpers import remove_all_callbacks


class KeyController:
    err_out = widgets_helpers.new_output()

    def __init__(self, game, canvas, remove_callbacks=True):
        self.game = game
        self.canvas = canvas
        self.src = None

        if remove_all_callbacks:
            remove_all_callbacks(self.canvas)

        self.canvas.on_key_down(self.on_key_down)

    @err_out.capture()
    def on_key_down(self, key, *flags):
        if key in '123' and self.src is None:
            self.src = int(key) - 1
            return
        elif key in '123':
            dst = int(key) - 1
            self.game.move_disk(self.src, dst)
        if key == 'n':
            self.game.new_game()
        self.src = None

    def _ipython_display_(self):
        display(self.canvas, self.err_out)


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


class TextController:
    err_out = widgets_helpers.new_output()

    def __init__(self, game, prompt='', width=None):
        self.game = game
        self.prompt = prompt
        layout = None if width is None else {'width': f'{width}px'}
        self.text = widgets_helpers.new_text(value=prompt, layout=layout)
        self.text.on_submit(self.on_press_enter)

    @err_out.capture()
    def on_press_enter(self, text):
        value = self.text.value.removeprefix(self.prompt)
        if value == 'c':
            self.err_out.clear_output()
        if value == 'p':
            print('stacks:', self.game.stacks)
        if value == 'n':
            self.game.new_game()
        if len(value) == 2 and value.isdigit():
            src, dst = (int(s)-1 for s in value)
            self.game.move_disk(src, dst)
        self.text.value = self.prompt

    def _ipython_display_(self):
        display(self.text, self.err_out)