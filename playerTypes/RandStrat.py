from playerTypes.Actor import Actor
import random

# RandomStrat Actor Class
# Ryan Bertola | April 20th 2024
# A strategy with no strategy. Just random.
# This class is not named random so as to not interfere with the existent random library.
class RandomStrat(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Random"
    
    def __str__(self):
        return "Random"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None] # Remove occupied and downed players.
        random.shuffle(filteredTargets)
        if len(filteredTargets) != 0:
            self.target = filteredTargets[0] # Set target to the first of the randomly shuffled group
        else:
            self.target = None # If nobody is available we don't want them to target
        if self.target is not None:
            self.target.occupied = True
        
