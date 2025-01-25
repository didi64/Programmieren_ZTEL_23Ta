import widgets_helpers
from IPython.display import display
from canvas_callbacks import remove_all_callbacks


class KeyController:

    def __init__(self, game, canvas, remove_callbacks=True, debug=True):
        self.game = game
        self.canvas = canvas
        if debug:
            self.err_out = widgets_helpers.new_output()

        self.src = None
        self.dst = None

        if remove_all_callbacks:
            remove_all_callbacks(self.canvas)
        if debug:
            self.on_key_down = self.err_out.capture()(self.on_key_down)

        self.canvas.on_key_down(self.on_key_down)

    def on_key_down(self, key, *flags):
        if key in '123' and self.src is None:
            self.src = int(key) - 1
            return
        elif key in '123':
            self.dst = int(key) - 1
            self.game.move_disk(self.src, self.dst)
        if key == 'n':
            self.game.new_game()
        self.src = None

    def _ipython_display_(self):
        display(self.canvas, self.err_out)


class KeyMouseController:

    callbacks = ['on_key_down', 'on_mouse_down', 'on_mouse_up']

    def __init__(self, game, canvas, remove_callbacks=True, debug=True):
        self.game = game
        self.canvas = canvas
        if debug:
            self.out = widgets_helpers.new_output()

        self.src = None
        self.dst = None

        if remove_all_callbacks:
            remove_all_callbacks(self.canvas)

        if debug:
            for callback in []:
                f = getattr(self, callback)
                decorated_f = self.out.capture()(f)
                setattr(self, callback, decorated_f)

        for callback in self.callbacks:
            f = getattr(self, callback)
            setter = getattr(self.canvas, callback)
            setter(f)

    def on_key_down(self, key, *flags):
        if key in '123' and self.src is None:
            self.src = int(key) - 1
            return
        elif key in '123':
            self.dst = int(key) - 1
            self.game.move_disk(self.src, self.dst)
        if key == 'n':
            self.game.new_game()
        self.src = None

    def on_mouse_down(self, x, y):
        stack_width = self.canvas.width / 3
        self.src = int(x // stack_width)

    def on_mouse_up(self, x, y):
        if self.src is None:
            return

        stack_width = self.canvas.width / 3
        dst = int(x // stack_width)
        self.game.move_disk(self.src, dst)
        self.src = None

    def _ipython_display_(self):
        display(self.canvas, self.out)


class TextController:
    err_out = widgets_helpers.new_output()

    def __init__(self, game, prompt='Your move: '):
        self.game = game
        self.prompt = prompt
        self.text = widgets_helpers.new_text(value=prompt)
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