def get_options(heaps):
    options = ()
    i = 1
    for n in heaps:
        if n > 0:
            options = options + (i,)
        i = i + 1
    return options


def ask_for_option(prompt, options):
    while True:
        opt = int(input(prompt)) 
        if opt in options:
            return opt


def ask_for_move(player, heaps):
    print(player)
    options = get_options(heaps)
    prompt = 'Haufen ' + str(options) + '?'
    heap = ask_for_option(prompt, options) - 1
    options = range(1, heaps[heap] +1)
    prompt = 'Wieviele ' + str(options) + '?'
    n = ask_for_option(prompt, options)
    return (heap, n)


def update_state(move, heaps):
    heap, n = move
    heaps[heap] = max(0, heaps[heap] - n)
    print(heaps)
