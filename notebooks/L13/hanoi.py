from game import Game
from view import View
from controller import Controller
from IPython.display import display


game = Game()
view = View()
game.callback = lambda event, data: view.draw_stacks(data)

Controller(game, view)
game.new_game()
display(view)