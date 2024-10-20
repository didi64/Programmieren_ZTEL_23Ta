from observable import Observable
from .maze_delta import delta


class Maze(Observable):
    def __init__(self):
        self.initial_state = 0
        self.accepting_states = {57, 58, 59}
        self.delta = delta

        self.state = None
        self.idx = None
        self.game_over = None
        self.history = None

    def new_game(self):
        self.state = self.initial_state
        self.history = [self.initial_state]
        self.idx = 0
        self._notify('new_game')

    def is_game_over(self):
        return self.state in self.accepting_states

    def get_opts(self):
        return self.delta.get(self.state, set())

    def is_legal(self, opt):
        if self.is_game_over() or self.state is None:
            return False
        return opt in self.get_opts()

    def move(self, opt):
        if not self.is_legal(opt):
            return
        self.state = opt
        self.game_over = self.state in self.accepting_states

        if len(self.history) >= self.idx+1:
            self.history = self.history[:self.idx+1]
        self.history.append(self.state)
        self.idx += 1
        self._notify('state_change')

    def undo(self):
        if not self.idx:
            return
        self.idx -= 1
        self.state = self.history[self.idx]
        self._notify('state_change')

    def redo(self):
        if not self.history or self.idx+1 >= len(self.history):
            return
        self.idx += 1
        self.state = self.history[self.idx]
        self._notify('state_change')

    def __repr__(self):
        opts = self.get_opts()
        return f'state: {self.state}, moves: {opts}, target reached: {self.is_game_over()}'