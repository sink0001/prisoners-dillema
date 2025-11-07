

class Grudge_holder:
    
    def move(self, opponent_previous_moves: list):
        '''
        start with corporation
        the grudge holder, if you defected once in the previous 2 moves he defects
        if it has only been 1 move and the opponent defected he defects
        otherwise if the opponent is nice he is nice
        '''
        if len(opponent_previous_moves) == 0:
            return "corporate"
        elif len(opponent_previous_moves) == 1:
            return opponent_previous_moves[0]
        elif "defect" in opponent_previous_moves[0:2]:
            return "defect"
        else:
            return "corporate"
    
    @property
    def name(self):
        return "2 eyes for one"