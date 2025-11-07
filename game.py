from grudge_holder import Grudge_holder
from random_player import Random
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
            player1_move = self.player1.move(self.player2_previous_moves)
            self.player1_previous_moves = [player1_move] + self.player1_previous_moves
            player2_move = self.player2.move(self.player1_previous_moves)
            self.player2_previous_moves = [player2_move] + self.player2_previous_moves

            match (player1_move, player2_move):
                case ("corporate", "corporate"):
                    print(f"both {self.player1.name} and {self.player2.name} corporated and gained 1 point each")
                    self.player1_score += 1
                    self.player2_score += 1
                case ("defect", "corporate"):
                    print(f"{self.player1.name} defected while {self.player2.name} corporated {self.player1.name} gained 2 points and {self.player2.name} gained 0")
                    self.player1_score += 2
                case ("corporate", "defect"):
                    print(f"{self.player1.name} corporated while {self.player2.name} defected {self.player2.name} gained 2 points and {self.player1.name} gained 0")
                    self.player2_score += 2
                case ("defect", "defect"):
                    print("both players defected neither gain any points")

        return f"\n{self.player1.name} total: {self.player1_score}\n{self.player2.name} total: {self.player2_score}\nWinner: {self.player1.name if self.player1_score > self.player2_score else self.player2.name}"


me = Grudge_holder()
opp = Random()
game1 = Game(me, opp)
print(game1.play(10000))
