from playerTypes.Actor import Actor
import random
import time
from matplotlib import pyplot as plt


# The game class, to store all game data.
# This is used to enable multiple games can be run and so no games have data leaks into eachother
class Game:
    # define any variables you wish to track here
    def __init__(self, players: list[Actor], end: int = 500) -> None:
        self.playerlist = players  # player list
        self.end = end  # the round in which the end occurs [default 500]
        self.iteration = 0  # which round we are at [if iteration > end, end round]
        self.down_count = []
        pass

    # iterates the game a given amount of count [default 500]
    def iterate(self, count=500):
        for i in range(count):
            self.iteration += 1
            self.data_collection()
            self.game_logic()
            downedPlayers = [i for i in self.playerlist if i.downedBy is not None]
            self.down_count.append(len(downedPlayers))
            # check if game ended.
            if self.iteration >= self.end:
                self.end_game()
                break

    # Ends the game. Any data that needs to be outputted should be put here.
    def end_game(self):
        plt.plot(self.down_count)
        plt.show()
        finalLeaderboard = sorted(self.playerlist, key=lambda x: len(x.downs), reverse=True)
        winner = finalLeaderboard[0]
        print(f"An {winner} strategy has won with {len(winner.downs)} downs!")

    # Outputs data at the given moment
    def get_game_data(self):
        leaderboard = sorted(self.playerlist, key=lambda x: len(x.downs), reverse=True)
        current_winner = leaderboard[0]
        print(f"A(n) {current_winner} strategy is winning with {len(current_winner.downs)} downs!")
        downedPlayers = [i for i in self.playerlist if i.downedBy is not None]
        print(f"There are {len(downedPlayers)} downed players.")
        # time.sleep(10) # 10-second delay to give time to read. Can be edited.

    def data_collection(self):
        if self.iteration >= self.end:  # Announce final round
            print("Final round!")
        if not self.iteration % 100 and self.iteration < self.end:
            self.get_game_data()
        print(f"Round {self.iteration} has commenced!")

    def game_logic(self):
        random.shuffle(self.playerlist)
        self.playerlist.sort(key=lambda x: x.priority, reverse=True)
        playerlist = [i for i in playerlist if i.downedBy is None]
        for p in self.playerlist:
            p.choose_target(self.playerlist)
        for p in [n for n in self.playerlist if n.target is not None]:
            p.battle_target()
