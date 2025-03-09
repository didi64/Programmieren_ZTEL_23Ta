import random
import cards


class BlackJack:
    def __init__(self):
        self.player = None
        self.bankroll = 0
        
        self.hand_player = []
        self.hand_dealer = []
        
        self.betsize = 0
        self.result = None
        self.game_on = False
        
        self.deck = cards.new_deck()
        

    def register(self, name, bankroll):
        if self.game_on or type(bankroll) is not int:
            return
        self.player = name
        self.bankroll = bankroll

    
    def play(self, betsize=10):
        if self.game_on or (self.betsize > self.bankroll) or self.bankroll <= 0:
            return
            
        self.game_on = True
        self.betsize = betsize
        self.bankroll -= self.betsize
        
        if len(self.deck) < 20:
            self.deck = cards.new_deck()
            
        self.hand_player[:] = [self.deck.pop() for _ in range(2)]
        self.hand_dealer[:] = [self.deck.pop() for _ in range(2)]


    def hit(self):
        if not self.game_on:
            return
            
        card = self.deck.pop()
        self.hand_player.append(card)
        
        if cards.handwert(self.hand_player) > 21:
           self._end_play()

    def stay(self):
        if not self.game_on:
            return
            
        while cards.handwert(self.hand_dealer) < 17:
            card = self.deck.pop()
            self.hand_dealer.append(card)
            
        self._end_play()

    
    def _end_play(self):
        pd = cards.handwert(self.hand_dealer)
        pp = cards.handwert(self.hand_player)
        if pp > 21:
            self.result = 0
        elif pp == pd:
            self.result = 1
        else:
            self.result = 2
        
        self.bankroll += self.result*self.betsize
        self.game_on = False
        
    
    def __repr__(self):
        s = (f'({self.game_on}, {self.result}, {self.player}, {self.bankroll}, ' +
             f'{self.betsize})\n{self.hand_player} {self.hand_dealer}')
        return s
