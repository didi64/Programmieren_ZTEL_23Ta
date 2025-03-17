from cards import handwert
from widgets_helpers import new_mcanvas
from ipywidgets import Image


def card2filename(card, img_path='img_cards'):
    tt = {'♥': 'H', '♠': 'S', '♦': 'D', '♣': 'C'}
    if len(card) == 2 and card[1] in tt:
        fn = card[0] + tt[card[1]] + '.png'
    else:
        fn = 'backside' + '.png'
    return img_path + '/' + fn


class View:

    def __init__(self, game):
        self.game = game
        self.game.event_handler = self.update
        self.mcanvas = new_mcanvas(2, 340, 200)
        self.bg, self.fg = self.mcanvas

        self.name = None
        self.bankroll = 0


    def draw_card(self, card, n=0, dealer=False):
        x = n*15 +150*dealer
        fn = card2filename(card)
        img = Image.from_file(fn)
        self.bg.draw_image(img, 20+dealer*150+n*15, 60)
    
    def draw_hands(self, hands, masked=True):
        for i, hand in enumerate(hands):
            for j, card in enumerate(hand):
                if masked and i == 1 and j > 0:
                    card = '*'
                self.draw_card(card, j, i)
    
    def register(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
        self.fg.clear()
        self.fg.fill_text(f'Welcome {name} [{bankroll}]', 20, 20)

    def play(self, betsize, hand_player, hand_dealer):
        self.mcanvas.clear()
        self.fg.fill_text(f'{self.name} [{self.bankroll}]', 20, 20)
        self.fg.fill_text(f'betsize: {betsize}', 20, 40)
        self.draw_hands([hand_player, hand_dealer], masked=True)

    def hit(self, hand_player):
        self.draw_card(hand_player[-1], len(hand_player)-1)

    def stay(self):
        pass
    
    def end_play(self, hand_dealer, result, score, bankroll):
        msg = {0: 'You lost', 1: 'It was a tie', 2: 'You won'}[result]
        self.bankroll = bankroll
        for i, card in enumerate(hand_dealer[1:]):
            self.draw_card(card, i+1, dealer=True)
        self.fg.clear()
        self.fg.fill_text(f'{self.name} [{self.bankroll}]', 20, 20)
        self.fg.fill_text(f'{msg}, {score}', 20, 180)

    def update(self, event, data):
        getattr(self, event)(*data)
        
    def _ipython_display_(self):
        display(self.mcanvas)
