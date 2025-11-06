from Player1 import Player1
'''
outcomes
1. A and B defect (both get 0 points)
2. A defects while B corporates (A gets 2 points) (2, 0)
3. A corporates while B defects (B gets 2 points) (0, 2)
4. A and B corporate (each gets 1 point) (1, 1)
'''

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(number_of_rounds):
        '''
        first play first round special behaviour
        then play normally
        '''