import random


VALUE = 0
SUIT = 1
SUITS = '♥♠♦♣'
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

VALUE_RANK = {v: i for i, v in enumerate(VALUES)}
RANK_VALUE = {v: k for k, v in VALUE_RANK.items()}

STRAIGHTS = ('2345A',) + tuple(''.join(VALUES[i:i+5]) for i in range(9))
HANDTYPES = ['11111', '2111', '221', '311', 'straight',
             'flush', '32', '41', 'straightflush']
HANDTYPE_RANK = {t: i for i, t in enumerate(HANDTYPES)}

HANDNAMES = ['high card', 'one pair', 'two pairs', 'triple', 'straight',
             'flush', 'fullhouse', 'four of a kind', 'straightflush']
HANDTYPE_NAME = dict(zip(HANDTYPES, HANDNAMES))


def new_deck(shuffle=True):
    deck = [value+suit for suit in SUITS for value in VALUES]
    if shuffle:
        random.shuffle(deck)
    return deck


def draw(deck, n=1):
    n = min(n, len(deck))
    cards = tuple(deck.pop() for _ in range(n))
    return cards


def get_values(hand):
    values = [card[VALUE] for card in hand]
    return values


def get_suits(hand):
    suits = [card[SUIT] for card in hand]
    return suits


def is_flush(hand):
    return len(set(get_suits(hand))) == 1


def is_straight(hand):
    values = get_values(hand)
    values = sorted(values, key=lambda x: VALUES.index(x))
    return ''.join(values) in STRAIGHTS


def vals2ranks(vals):
    return tuple(VALUE_RANK[v] for v in vals)


def count_dict(items):
    d = {}
    for item in items:
        d[item] = d.get(item, 0) + 1
    return d


def sort_ranks(ranks):
    cd = count_dict(ranks)
    return sorted(ranks, key=lambda x: (cd[x], x), reverse=True)


def handtype(hand):
    sf = 'straight' * is_straight(hand) + 'flush' * is_flush(hand)
    if sf:
        return sf

    values = get_values(hand)
    counts = count_dict(values).values()
    counts = sorted(counts, reverse=True)
    return ''.join(str(x) for x in counts)


def handrank(hand):
    t = handtype(hand)
    return HANDTYPE_RANK[t]


def handname(hand):
    t = handtype(hand)
    return HANDTYPE_NAME[t]


def tiebreaker(hand):
    ranks = vals2ranks(get_values(hand))
    return sort_ranks(ranks)


def rank_hands(hand1, hand2):
    v1, v2 = ((handrank(h), tiebreaker(h)) for h in (hand1, hand2))
    if v1 > v2:
        return 1
    elif v1 == v2:
        return 0
    else:
        return -1