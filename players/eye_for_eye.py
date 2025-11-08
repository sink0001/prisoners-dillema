# Eye_for_eye defaults to corporation but mirrors defection of opponent

class Eye_for_eye:

    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        if not opponent_previous_moves:
            return "corporate"
        elif opponent_previous_moves[0] == "defect":
            return "defect"
        return "corporate"
    
    @property
    def name(self):
        return "Eye for eye"