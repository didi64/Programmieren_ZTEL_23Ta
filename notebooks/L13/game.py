class Game:
    def __init__(self, ndisks=4):
        self.ndisks = ndisks
        self.stacks = None
        self.callback = lambda *args: print(*args)

    def notify(self, event, data):
        self.callback(event, data)

    def new_game(self):
        self.stacks = [list(range(self.ndisks))[::-1], [], []]
        self.notify('new_game', self.stacks)

    def move_disk(self, i, j):
        x = self.stacks[i].pop()
        self.stacks[j].append(x)
        self.notify('update_stacks', self.stacks)

    def __repr__(self):
        return self.stacks.__repr__()
