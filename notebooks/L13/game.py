class Game:
    def __init__(self):
        self.ndisks = 4
        self.stacks = None
        self.event_handler = lambda *args: print(*args)

    def new_game(self):
        self.stacks = [list(range(self.ndisks))[::-1], [], []]
        self.event_handler('new_game', self.stacks)

    def move_disk(self, src, dst):
        if (not self.stacks[src] or
           (self.stacks[dst] and self.stacks[dst][-1] < self.stacks[src][-1])):
            return
        disk = self.stacks[src].pop()
        self.stacks[dst].append(disk)
        self.event_handler('update_stacks', self.stacks)

    def __repr__(self):
        return self.stacks.__repr__()
