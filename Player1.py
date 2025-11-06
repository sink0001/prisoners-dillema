

class Player1:
    # maybe make class property of own previous move
    
    def __init__(self, opponent_previous_moves: list, own_moves: list):
        self.opponent_previous_moves = opponent_previous_moves
        self.own_moves = own_moves

    def default_first_move():
        return "corporate"
    
    def move():
        pass