import random

class Player1:

    def move(self) -> str:
        decision = random.randint(0, 1)
        if decision == 1:
            return "defect"
        else:
            return "corporate"