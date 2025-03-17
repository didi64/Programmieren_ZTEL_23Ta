import random

IMG_PATH = '/home/studi/work/.src/notebooks/L17/Blackjack/img_cards'
SUITS = '♥♠♦♣'
RANKS = '23456789TJQKA'
rank_points = {k: int(k) if k in '23456789' else (10 if k in 'TJQK' else 11)
               for k in RANKS}


def new_deck(shuffle=True):
    deck = [value+suit for suit in SUITS for value in RANKS]
    if shuffle:
        random.shuffle(deck)
    return deck


def handwert(hand):
    """Berechnet den Gesamtwert einer Hand."""
    ranks = [card[0] for card in hand]
    wert = sum(rank_points[r] for r in ranks)
    anzahl_asse = ranks.count('A')
    while wert > 21 and anzahl_asse:
        wert -= 10
        anzahl_asse -= 1
    return wert


def card2filename(card):
    tt = {'♥': 'H', '♠': 'S', '♦': 'D', '♣': 'C'}
    return IMG_PATH + '/' + card[0] + tt[card[1]] + '.png'