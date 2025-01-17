import game
import view
from IPython.display import display
from canvas_callbacks import remove_all_callbacks


src = None
running = False


def on_key_down(key, *flags):
    global src

    if key in '123' and src is None:
        src = int(key) - 1
        return
    elif key in '123':
        dst = int(key) - 1
        game.move_disk(src, dst)
    if key == 'n':
        game.new_game()
    src = None


def start():
    global running

    if not running:
        game.event_handler = lambda event, data: view.draw_stacks(data)
        game.new_game()
        remove_all_callbacks(view.canvas)
        view.canvas.on_key_down(on_key_down)
        display(view.canvas)
        running = True