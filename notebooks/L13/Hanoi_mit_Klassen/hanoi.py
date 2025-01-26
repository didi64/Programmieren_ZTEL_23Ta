from game import Game
from views import CanvasView
from controllers import KeyMouseController as Controller
from IPython.display import display


game = Game()
view = CanvasView(game)
controller = Controller(game, view.canvas)
game.new_game()
display(controller)