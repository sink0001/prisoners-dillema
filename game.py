from Player1 import Player1
from Player2 import Player2
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
        self.player1_previous_moves = []
        self.player2_previous_moves = []
        self.player1_score = 0
        self.player2_score = 0

    def play(self, number_of_rounds: int) -> str:
        '''
        first play first round special behaviour
        then play normally
        return the number of points each player got
        '''
        for r in range(0, number_of_rounds):
            player1_move = self.player1.move()
            player2_move = self.player2.move(self.player1_previous_moves)
            self.player1_previous_moves.append(player1_move)
            self.player2_previous_moves.append(player2_move)

            match (player1_move, player2_move):
                case ("corporate", "corporate"):
                    print(f"both {self.player1} and {self.player2} corporated and gained 1 point each")
                    self.player1_score += 1
                    self.player2_score += 1
                    print(self.player1_score)
                case ("defect", "corporate"):
                    print(f"{self.player1} defected while {self.player2} corporated {self.player1} gained 2 points and {self.player2} gained 0")
                    self.player1_score += 2
                    print(self.player1_score)
                case ("corporate", "defect"):
                    print(f"{self.player1} corporated while {self.player2} defected {self.player2} gained 2 points and {self.player1} gained 0")
                    self.player2_score += 2
                case ("defect", "defect"):
                    print("both players defected neither gain any points")

        return f"{self.player1} total: {self.player1_score}\n{self.player2} total: {self.player2_score}\nWinner: {self.player1 if self.player1_score > self.player2_score else self.player2}"

me = Player1()
opp = Player2()
game1 = Game(me, opp)
print(game1.play(100000))
