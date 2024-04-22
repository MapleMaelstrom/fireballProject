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
            rawDownData = self.get_downed_each()
            print(rawDownData)
        print(f"Round {self.iteration} has commenced!")

    def game_logic(self):  # Run the game logic
        random.shuffle(self.playerlist)  # Shuffle player list
        self.playerlist.sort(key=lambda x: x.priority, reverse=True)  # Sort by priority
        for p in self.playerlist:
            p.choose_target(self.playerlist)  # Targetting logic
        for p in [n for n in self.playerlist if n.target is not None]:
            p.battle_target()  # Battling logic

    def get_downed_each(self):  # Get stats on how much of each class is downed
        playerTypes = list(set([i.type for i in self.playerlist]))  # Get each type of player in game
        downedPlayers = [p.type for p in self.playerlist if p.downedBy is not None]  # Get downed player types
        eachDowned = {}
        for t in playerTypes:
            eachDowned[t] = downedPlayers.count(t)  # With the set-up made above, counting is simple :D
        return eachDowned  # A dictionary of each class and how much is downed
