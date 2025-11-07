

class Player2:
    
    def move(self, opponent_previous_moves: list):
        '''
        start with corporation
        the grudge holder, if you defected once in the previous 2 moves he defects
        if it has only been 1 move and the opponent defected he defects
        otherwise if the opponent is nice he is nice
        '''
        if not opponent_previous_moves:
            return "corporate"
        try:
            if "defect" in opponent_previous_moves[0:1]:
                return "defect"
        except IndexError:
            return opponent_previous_moves[0]
        return "corporate"