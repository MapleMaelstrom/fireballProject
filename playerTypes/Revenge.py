from playerTypes.Actor import Actor
import random

# Revenge Actor Class
# Ryan Bertola | April 20th 2024
# Idea by Doyin
# Targets randomly until downed twice by same person. Then, will target them above all else
class Revenge(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Revenge"
        self.prevDowns = []
    
    def __str__(self):
        return "Revenge"

    def choose_target(self, targets):
        # Filter targets down to the desired group
        if self.occupied:
            self.target = None
            return
        enemy = self.determine_enemy()
        if enemy is not None and enemy.downedBy is None and not enemy.occupied: # Ensures enemy can be selected
            self.target = enemy
        else:
            filteredTargets = random.shuffle([t for t in targets if t.occupied is False and t.downedBy is None]) # Removes downed / occupied players.
            if filteredTargets is not None and len(filteredTargets) != 0:
                self.target = filteredTargets[0]
            else:
                self.target = None # Does not target anyone otherwise.
        if self.target is not None:
            self.target.occupied = True
    
    def downed(self, winner): # Adding to list of prevdowns
        self.prevDowns.append(winner)
        return super().downed(winner) # Reusing existent code to minimize rewritten code
    
    def determine_enemy(self):
        uniquePast = random.shuffle(list(set(self.prevDowns))) # remove dupes and randomly order them
        if uniquePast is None: # If no past
            return None
        downedByEach = [[self.prevDowns.count(i), i] for i in uniquePast] # Count previous downs from each
        downedByEach.sort(key=lambda x: x[0], reverse=True) # Get descending order
        if downedByEach[0][0] >= 2:
            revengePoint = downedByEach[0][0] # Determine how many downs on this user are needed to be considered a possible enemy
            possibleEnemies = random.shuffle([i for i in downedByEach if i[0] >= revengePoint]) # remove all lower than the revenge point and randomly shuffle them
            return possibleEnemies[0][1] # Select the enemy
        return None # If this point is reached, no enemy is selected. Thus, random selection will begin.