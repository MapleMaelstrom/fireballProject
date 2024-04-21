from playerTypes.Actor import Actor
from playerTypes.Besties import Bestie
import random

# Snake Actor Class
# Ryan Bertola | April 20th 2024
# Strategy by Doyin. Snake will act like a bestie until a random moment.
# Random moment is a 1/100 to occur on a given time they choose target.
class Snake(Actor):
    def __init__(self, friend) -> None:
        super().__init__()
        self.type = "Snake"
        self.friend = friend
        self.broken = False
    
    def __str__(self):
        return "Snake"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        if self.friend.downedBy is not None and not self.friend.downedBy.occupied and not self.broken: # If friend downed and downer is not occupied, target downer
            self.target = self.friend.downedBy
        if random.randrange(100) == 42: # 1/100 chance to break the bond at any moment. Friend does not realize, and will think it's a mistake.
            self.broken = True
        if not self.broken:
            filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None and t != self.friend] # Removing friend and invalid targets
        else:
            filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None] # Removing only invalid targets instead
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


# Function to create snake and bestie due to the complexities of such.
# Should be used in any situation where a snake is made.
# Returns a list of a snake and a bestie who have eachother as their friend.
def createSnake():
    f1 = Snake(None)
    f2 = Bestie(f1)
    f1.friend = f2
    return [f1, f2]