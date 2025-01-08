import game
import view
from IPython.display import display
from canvas_callbacks import remove_all_callbacks


src = None
running = False


def on_key_down(key, *flags):
    if key == 'n':
        game.new_game()


def on_mouse_down(x, y):
    global src
    stack_width = view.canvas.width / 3
    src = int(x // stack_width)


def on_mouse_up(x, y):
    global src

    if src is None:
        return

    stack_width = view.canvas.width / 3
    dst = int(x // stack_width)
    game.move_disk(src, dst)
    src = None


def start():
    global running

    if not running:
        game.event_handler = lambda event, data: view.draw_stacks(data)
        game.new_game()

        remove_all_callbacks(view.canvas)

        view.canvas.on_key_down(on_key_down)
        view.canvas.on_mouse_down(on_mouse_down)
        view.canvas.on_mouse_up(on_mouse_up)

        display(view.canvas)
        running = True