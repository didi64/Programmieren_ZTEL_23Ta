from IPython.display import display
from .maze import Maze
from .view import View


def run():
    maze = Maze()
    view = View(maze)
    display(view)