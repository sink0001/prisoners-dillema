# Prisoners Dillema simulation
## This is a simple game simulation for the popular prisoners dillema using python
---
Prisoners dillema here is defined as parties A and B meeting such that they have option defect or corporate.
- all possible outcomes:
- A corporates and B corporates -> A and B both gain 1 point (1, 1)
- A corporates while B defects -> B gains 2 points and A gains 0 (0, 2)
- A defects while B corporates -> A gains 2 points while B gains 0 (2, 0)
- A and B defect -> both get 0 points (0, 0)
---
In the simulation I allow 2 players to play eachother in a game for any number of rounds and I then record the number of points each player gets and decide a winner.
To add a new player strategy head to the players directory and simply add a player in the following format: <br>
```
class Player_name:
    def move(self, opponent_previous_moves: list, own_previous_moves: list) -> str:
        # Note that the move lists have moves in descending order i.e. opponent_previous_moves[0] is the most recent move
    
    @property
    def name(self):
        return "name for this player"
```
