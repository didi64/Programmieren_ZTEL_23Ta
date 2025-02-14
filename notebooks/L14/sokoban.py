class Sokoban:
    board = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', ' ', ' ', ' ', 'X', 'X'],
             ['X', '.', ' ', 'b', ' ', ' ', 'X', 'X'],
             ['X', 'X', 'X', ' ', 'b', '.', 'X', 'X'],
             ['X', '.', 'X', 'X', 'b', ' ', 'X', 'X'],
             ['X', ' ', 'X', ' ', '.', ' ', 'X', 'X'],
             ['X', 'b', ' ', 'B', 'b', 'b', '.', 'X'],
             ['X', ' ', ' ', ' ', '.', ' ', ' ', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ]
    start_pos = (2, 2)

    directions = {'up': (0, -1),
                  'down': (0, 1),
                  'right': (1, 0),
                  'left': (-1, 0),
                  }

    BOX = 'b'
    PLAYER = 'p'
    MARK = '.'
    EMPTY = ' '
    FREE = (EMPTY, MARK)

    def __init__(self):
        self.event_handler = print
        self.new_game()

    def new_game(self):
        self.board = [row.copy() for row in Sokoban.board]
        self.pos = Sokoban.start_pos
        self.set_field(self.pos, Sokoban.PLAYER)
        self.event_handler('new game', None)

    def new_pos(self, pos, direction):
        dx, dy = self.directions[direction]
        return pos[0]+dx, pos[1]+dy

    def get_field(self, pos):
        col, row = pos
        return self.board[row][col]

    def set_field(self, pos, char):
        col, row = pos
        current = self.board[row][col]
        self.board[row][col] = char.upper() if current == Sokoban.MARK else char.lower()

    def move_piece(self, old_pos, new_pos):
        char = self.get_field(old_pos)
        self.set_field(new_pos, char)
        self.set_field(old_pos, Sokoban.MARK if char.isupper() else Sokoban.EMPTY)

    def move_player_to(self, pos):
        self.move_piece(self.pos, pos)
        self.pos = pos

    def push_box(self, old_pos, move):
        new_pos = self.new_pos(old_pos, move)
        if self.get_field(new_pos) in Sokoban.FREE:
            self.move_piece(old_pos, new_pos)
            return True

    def move(self, move):
        new_pos = self.new_pos(self.pos, move)
        char = self.get_field(new_pos).lower()
        if char in Sokoban.FREE or (char == Sokoban.BOX and self.push_box(new_pos, move)):
            self.move_player_to(new_pos)
        self.event_handler('move', move)

    def __repr__(self):
        return '\n'.join(str(row) for row in self.board)
