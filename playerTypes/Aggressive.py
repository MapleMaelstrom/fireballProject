from Actor import Actor
import random

# Aggressive Actor Class
# Ryan Bertola | March 24th 2024
# Treated as the template for all other actors
class Aggressive(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Aggressive"
        self.win_weight = 60 # Higher win weight to represent more battle experience

    def choose_target(self, targets):
        # Filter targets down to the desired group
        filteredTargets = random.shuffle([t for t in targets if t.type == "Aggressive" and t.occupied is False and t.downedBy is None])
        if len(filteredTargets) != 0:
            self.target = filteredTargets[0] # Set target to the first of the randomly shuffled group
        else:
            # Settle for any target if not desired group
            refiltered = random.shuffle([t for t in targets if t.occupied is False and t.downedBy is None])
            if len(refiltered) != 0:
                self.target = refiltered[0]
            else: # If no unoccupied players or non-downed players are found, default to no target.
                self.target = None
        
# The battle will be started in the main.py so everybody attacks simultaneously [thus nobody gets attacked twice same iteration]