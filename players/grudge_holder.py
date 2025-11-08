# Grrudge_holder will default to corporation but if the opponent defects once, he will defect twice

class Grudge_holder:
    
    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        if not opponent_previous_moves:
            return "corporate"
        elif len(opponent_previous_moves) == 1:
            return opponent_previous_moves[0]
        elif "defect" in opponent_previous_moves[0:2]:
            return "defect"
        return "corporate"
    
    @property
    def name(self):
        return "grudge holder"