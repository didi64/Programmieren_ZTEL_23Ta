import random


SUITS = '♥♠♦♣'
VALUES = '23456789TJQKA'
rank_points = {k: int(k) if k in '23456789' else (10 if k in 'TJQK' else 11)
               for k in VALUES}


def new_deck(shuffle=True):
    deck = [value+suit for suit in SUITS for value in VALUES]
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
