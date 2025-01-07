class Controller:
    def __init__(self, game, view):
        view.canvas.on_key_down(self.on_key_down)
        self.game = game
        self.src = None

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
