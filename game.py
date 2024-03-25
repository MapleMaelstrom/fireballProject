from playerTypes.Actor import Actor
import random
# The game class, to store all game data. 
# This is used to enable multiple games can be run and so no games have data leaks into eachother
class Game():
    # define any variables you wish to track here
    def __init__(self, players: list[Actor], end: int = 500) -> None: 
        self.playerlist = players # player list
        self.end = end # the round in which the end occurs [default 500]
        self.iteration = 0 # which round we are at [if iteration > end, end round]
        pass

    # iterates the game a given amount of count [default 500]
    def iterate(self, count = 500):
        for i in range(count):
            if self.iteration >= self.end:
                print("Final round!")
            self.iteration += 1
            print(f"Round {self.iteration} has commenced!")
            random.shuffle(self.playerlist)
            self.playerlist.sort(key=lambda x: x.priority, reverse=True)
            for p in self.playerlist:
                p.choose_target(self.playerlist)
            for p in [n for n in self.playerlist if n.target is not None]:
                p.battle_target()
            # check if game ended.
            if self.iteration >= self.end:
                self.end_game()
                break
            

    # Ends the game. Any data that needs to be outputted should be put here.
    def end_game(self):
        finalLeaderboard = sorted(self.playerlist, key=lambda x: len(x.downs), reverse=True)
        winner = finalLeaderboard[0]
        print(f"An {winner} strategy has won with {len(winner.downs)} downs!")
