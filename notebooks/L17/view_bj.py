class View:
    err_out = new_output()

    
    def __init__(self, game):
        self.err_out.clear_output()
        self.game = game
        layout = {'border': '1px solid black', 'height': '100px'}
        self.out = new_output(layout=layout)

    @err_out.capture()
    def update(self, event, data):
        self.out.clear_output()
        pd = handwert(self.game.hand_player)
        pp = handwert(self.game.hand_dealer)
        with self.out:
            print((f'Name: {self.game.player}, '
                   + f'Bankroll: {self.game.bankroll}, '
                   + f'Betsize: {self.game.betsize}'))
            print(f'Hand Player: {self.game.hand_player} ({'bust!' if pp > 21 else pp})')
            print(f'Hand dealer: {self.game.hand_dealer} ({'bust!' if pd > 21 else pd})')
            print(f'Result: {self.game.result}')

    def _ipython_display_(self):
        display(self.out, err_out)        
