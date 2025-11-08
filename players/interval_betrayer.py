# Interval_betrayer will default to corporation but defect every 4th move

class Interval_betrayer:

    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        if len(own_previous_moves) < 3:
            return "corporate"
        elif "defect" not in own_previous_moves[0:3]:
            return "defect"
        return "corporate"
    
    @property
    def name(self):
        return "Interval betrayer"