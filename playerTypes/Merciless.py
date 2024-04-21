from playerTypes.Actor import Actor
import random

# Merciless Actor Class
# Ryan Bertola | April 20th 2024
# Will only target those who have less than 2 downs if possible. Otherwise, randomly targets.
# Originally referred to as "Tryhard" but sounded too biased [regardless of us having no bias when making these strategies]
class Merciless(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Merciless"
    
    def __str__(self):
        return "Merciless"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None and len(t.downs) <= 2] # Removes downed / occupied players and players with more than 2 downs
        if len(filteredTargets) != 0: # Player with less than two downs found
            self.target = random.choice(filteredTargets) # Selects random target
        else: # Random time
            filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None] # Remove occupied and downed players.
            random.shuffle(filteredTargets)
            if len(filteredTargets) != 0:
                self.target = filteredTargets[0] # Set target to the first of the randomly shuffled group
            else:
                self.target = None # If nobody is available we don't want them to target.
        if self.target is not None:
            self.target.occupied = True