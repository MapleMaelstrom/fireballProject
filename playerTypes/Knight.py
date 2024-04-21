from playerTypes.Actor import Actor
import random

# Knight Actor Class
# Ryan Bertola | April 20th 2024
# Will target anyone except those they deem the winner. Only activates when somebody has >2 downs.
class Knight(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Knight"
    
    def __str__(self):
        return "Knight"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        filteredTargets = [t for t in targets if t.occupied is False and t.downedBy is None] # Removes downed / occupied players.
        filteredTargets.sort(key=lambda x: len(x.downs), reverse=True) # Sorts by downs in descending order
        if len(filteredTargets) != 0 and len(filteredTargets[0].downs) >= 2: # Ensures 2 downs.
            leaderDowns = len(filteredTargets[0].downs)
            filteredTargets = [t for t in filteredTargets if len(t.downs) == leaderDowns] # Removes any user who is in the lead [to prevent complications if there is a current tie].
            self.target = random.choice(filteredTargets) # Selects random target
        else:
            self.target = None # Does not target anyone otherwise.
        if self.target is not None:
            self.target.occupied = True