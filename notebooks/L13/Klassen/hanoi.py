from game import Game
from view import CanvasView
from controller import Controller
from IPython.display import display


game = Game()
view = CanvasView(game)
controller = Controller(game, view.canvas)
display(controller)