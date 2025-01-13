import game
import view
import warnings
from IPython.display import display
from ipywidgets import Text


def on_press_enter(text):
    value = text.value.removeprefix(prompt)
    if value == 'n':
        game.new_game()
    if len(value) == 2 and value.isdigit():
        src, dst = (int(s)-1 for s in value)
        game.move_disk(src, dst)
    text.value = prompt


def start():
    global running

    if not running:
        game.event_handler = lambda event, data: view.draw_stacks(data)
        game.new_game()

        text = Text(value=prompt)
        text.on_submit(on_press_enter)
        running = True
        display(view.canvas, text)


warnings.filterwarnings('ignore', category=DeprecationWarning)

running = False
prompt = 'Move ? '