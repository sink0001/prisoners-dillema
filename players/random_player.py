from random import randint

class Random:

    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        decision = randint(0, 1)
        if decision == 1:
            return "defect"
        else:
            return "corporate"
        
    @property
    def name(self):
        return "Random"