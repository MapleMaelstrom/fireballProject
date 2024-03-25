import random

# Main Actor Class
# Created by Ryan Bertola | March 24th 2024
class Actor():
    # initialization of class
    def __init__(self) -> None:
        self.downedBy = None # The player who eliminated this player. If None, player still in play
        self.downs = [] # The players this player has eliminated. If this player is downed,
        self.priority = 1 # Higher priority = targets first. 
        self.type = "" # Defined by a class if their type is actually relevant [aggressive has it defined bc aggressive targets aggressive]
        self.occupied = False # Mark as true if the player has been targetted. This is reset to false after the fight.
        self.target = None # The player this player is targetting [if they are targetting anybody]
        self.win_weight = 50 # The relative chance of winning against another player. DOES NOT NEED TO ADD TO 100.

    # Defines what gets printed when the actor has won. Must be defined for each strategy.
    def __str__(self):
        return "ERROR!!!!\nERROR!!!!\nERROR!!!!\nUnderdefined Actor [define a __str__ function for this class]"

    # target choosing, individually defined by each class
    def choose_target(self, targets):
        pass

    # what to do when the user is downed. Universally defined. 
    # Only edit this on a given class if they do something when downed [such as either cheating, holding a grudge, etc]
    # typically, try to super this rather than fully re-implementing.
    def downed(self, winner):
        self.downedBy = winner
        winner.downs.append(self)
        for d in self.downs:
            d.downedBy = None
        self.downs = []

    # what to do when battling. Universally defined. Do not edit on a per-class basis; this is meant to be global.
    def battle_target(self):
        self.on_battle()
        weights = [self.win_weight, self.target.win_weight]
        players = [self, self.target]
        winner = random.choices(players, weights)[0] # Determine winner base on weights. Higher weight = better odds
        if players[0] != winner:
            players[0].downed(winner)
        else:
            players[1].downed(winner)
        # Reset data
        self.occupied = False
        self.target.occupied = False
        self.target = None

    # if you wish for something to occur when the strategy battles, PLEASE make an altered verion of this instead. 
    # For example, if you want win rate to decrement with each fight.
    def on_battle(self):
        pass

