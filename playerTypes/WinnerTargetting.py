from playerTypes.Actor import Actor
import random


# WinTarg Actor Class
# Ryan Bertola | April 20th 2024
# Will target exclusively those they deem the winner. Only activates when somebody has >4 downs.
class WinTarg(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Winner Targetting"
        self.priority = 2  # Higher priority means the winner doesn't get a chance to target somebody else.

    def __str__(self):
        return "Winner Targetting"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        filteredTargets = [t for t in targets if
                           t.occupied is False and t.downedBy is None]  # Removes downed / occupied players.
        filteredTargets.sort(key=lambda x: len(x.downs), reverse=True)  # Sorts by downs in descending order
        if len(filteredTargets) != 0 and len(filteredTargets[0].downs) >= 5:  # Ensures 5 downs.
            self.target = filteredTargets[0]  # Set target to the leader
        else:
            self.target = None  # Does not target anyone otherwise.
        if self.target is not None:
            self.target.occupied = True
