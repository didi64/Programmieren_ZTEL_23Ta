import time


moves = [(0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1),
         (0, 2), (1, 2), (1, 0), (2, 0), (1, 2), (0, 1), (0, 2), (1, 2)]


game.new_game()
for move in moves:
    game.move_disk(*move)
    time.sleep(0.5)