from Actor import Actor

# Aggressive Actor Class
class Aggressive(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Aggressive"

    def choose_target(self, targets):
        filteredTargets = [t for t in targets if t.type == "Aggressive" and t.occupied is False and t.downedBy is not None]
        if len(filteredTargets != 0):
            self.target = filteredTargets[0]