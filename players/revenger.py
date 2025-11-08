# Revenger defaults to corporation but if the opponent defects twice in a row, then Revenger defects thrice in a row

class Revenger:
    
    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        if len(opponent_previous_moves) == 0:
            return "corporate"
        elif "corporate" not in opponent_previous_moves[0:2]:
            if "corporate" in own_previous_moves[0:3]:
                return "defect"
        return "corporate"
    
    @property
    def name(self):
        return "Revenger"