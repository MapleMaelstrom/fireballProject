from Actor import Actor

# Passive Actor Class
# Ryan Bertola | March 24th 2024
# Treated as the template for all other actors
class Aggressive(Actor):
    def __init__(self) -> None:
        super().__init__()
        self.win_weight = 40 # Lower win weight to represent more battle experience
    
    def choose_target(self, targets):
        return super().choose_target(targets)