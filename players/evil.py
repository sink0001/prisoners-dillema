# Evil always defects

class Evil:

    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        return "defect"
    
    @property
    def name(self):
        return "Evil"