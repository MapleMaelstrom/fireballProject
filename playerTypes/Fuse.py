from playerTypes.Actor import Actor
import random

# Revenge Actor Class
# Ryan Bertola | April 20th 2024
# Idea by Doyin
# Passive first 10 downs
# Aggressive next 20
# Random forever after
class Fuse(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Fuse"
        self.prevDowns = []
    
    def __str__(self):
        return "Fuse"

    def choose_target(self, targets):
        if len(self.prevDowns < 10): # Passive
            return super().choose_target(targets)
        elif len(self.prevDowns < 30): # Aggressive
            # Filter targets down to the desired group
            if self.occupied:
                self.target = None
                return
            filteredTargets = [t for t in targets if t.type == "Aggressive" and t.occupied is False and t.downedBy is None]
            random.shuffle(filteredTargets)
            if len(filteredTargets) != 0:
                self.target = filteredTargets[0] # Set target to the first of the randomly shuffled group
            else:
                # Settle for any target if not desired group
                refiltered = [t for t in targets if t.occupied is False and t.downedBy is None]
                random.shuffle(refiltered)
                if len(refiltered) != 0:
                    self.target = refiltered[0]
                else: # If no unoccupied players or non-downed players are found, default to no target.
                    self.target = None
        else: # Random
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
    
    def downed(self, winner): # Adding to list of prevdowns
        self.prevDowns.append(winner)
        return super().downed(winner) # Reusing existent code to minimize rewritten code