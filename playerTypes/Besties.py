from playerTypes.Actor import Actor
import random

# Besties Actor Class
# Ryan Bertola | April 20th 2024
# Strategy by Doyin. Two are created at a time. 
# They refuse to target eachother unless they are the only option.
# If bestie is downed, will target the player who downed bestie.
class Bestie(Actor):
    def __init__(self, friend) -> None:
        super().__init__()
        self.type = "Bestie"
        self.friend = friend
    
    def __str__(self):
        return "Bestie"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        if self.friend.downedBy is not None and not self.friend.downedBy.occupied: # If friend downed and downer is not occupied, target downer
            self.target = self.friend.downedBy
        filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None and t != self.friend] # Removing friend and invalid targets
        random.shuffle(filteredTargets)
        if len(filteredTargets) != 0:
            self.target = filteredTargets[0] # Set target to the first of the randomly shuffled group
        else:
            # Settle for any target if not desired group, typically meaning friend, but not exclusively to account for unseen edgecases. Can never be too safe.
            refiltered = [t for t in targets if t.occupied is False and t.downedBy is None]
            random.shuffle(refiltered)
            if len(refiltered) != 0:
                self.target = refiltered[0]
            else: # If no unoccupied players or non-downed players are found, default to no target.
                self.target = None
        if self.target is not None:
            self.target.occupied = True


# Function to create besties due to the complexities of such.
# Should be used in any situation where besties are made.
# Returns a list of two besties who have eachother as their friend.
def createBesties():
    f1 = Bestie(None)
    f2 = Bestie(f1)
    f1.friend = f2
    return [f1, f2]