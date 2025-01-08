ndisks = 4
stacks = []
event_handler = lambda event, data: print(event, data)


def new_game():
    stacks[:] = [list(range(ndisks))[::-1], [], []]
    event_handler('new game', stacks)


def move_disk(src, dst):
    if not stacks[src] or (stacks[dst] and stacks[dst][-1] < stacks[src][-1]):
        return
    disk = stacks[src].pop()
    stacks[dst].append(disk)
    event_handler('update stacks', stacks)