class Game:
    def __init__(self):
        self.board = None
        self.event_handler = print

    def new_game(self):
        self.board = [False] * 6
        self.event_handler('new game', None)

    def place(self, src):
        if self.board is None:
            return
        self.board[src] = True
        self.event_handler('place_stone', (src,))

    def move(self, src, target):
        if self.board is None:
            return
        self.board[src] = False
        self.board[target] = True
        self.event_handler('move_stone', (src, target))

    def __repr__(self):
        return 'Position: {}'.format(self.board)
