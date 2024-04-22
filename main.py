from playerTypes.Aggressive import Aggressive
from playerTypes.Passive import Passive
from playerTypes.RandStrat import RandomStrat
from playerTypes.WinnerTargetting import WinTarg
from playerTypes.Besties import createBesties # Only import the function so as to not overcomplicate things.
from playerTypes.Snake import createSnake # Only import the function so as to not overcomplicate things.
from playerTypes.Knight import Knight
from playerTypes.Revenge import Revenge
from playerTypes.Fuse import Fuse
from playerTypes.Merciless import Merciless
from game import Game

Durants = []
for x in range(10):
  Durants += createSnake()

bestiesList = []
for y in range(10):
  bestiesList += createBesties()

GList = ([Aggressive() for i in range(10)] + [Revenge() for j in range(10)]
            + [RandomStrat() for k in range(10)] + bestiesList 
            + Durants + [Knight() for i in range(10)] 
            + [Fuse() for j in range(10)] + [Merciless() for k in range(10)]  
            + [Passive() for k in range(10)] + [WinTarg() for k in range(10)]
            )
firstGame = Game(GList)
firstGame.iterate()
roundscore, scoreboard = firstGame.getscore()
Leaderboard = scoreboard

for i, t in enumerate(roundscore):
    Leaderboard[t] += i + 1
print(roundscore, Leaderboard)

SecondGame = Game(GList)
SecondGame.iterate()
roundscore, scoreboard = SecondGame.getscore()
for i, t in enumerate(roundscore):
    Leaderboard[t] += i + 1
print(roundscore)
print("ROUND TWO OVER")
print(Leaderboard)

ThirdGame = Game(GList)
ThirdGame.iterate()
roundscore, scoreboard = ThirdGame.getscore()
for i, t in enumerate(roundscore):
    Leaderboard[t] += i + 1
print(roundscore)
print("ROUND Three OVER")
print(Leaderboard)
