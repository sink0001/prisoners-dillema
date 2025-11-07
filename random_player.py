import random

class Random:

    def move(self, opponent_previous_moves: list) -> str:
        decision = random.randint(0, 1)
        if decision == 1:
            return "defect"
        else:
            return "corporate"
        
    @property
    def name(self):
        return "Random"