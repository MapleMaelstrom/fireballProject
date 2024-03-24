# Main Actor Class
# Created by Ryan Bertola | March 24th 2024
class Actor():
    # initialization of class
    def __init__(self) -> None:
        self.downedBy = None
        self.downs = []
        self.priority = 1 # Higher priority = targets first. 
        self.type = ""
        self.occupied = False
        self.target = None

    # target choosing
    def choose_target(self, targets):
        pass