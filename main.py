from playerTypes.Aggressive import Aggressive
from playerTypes.Passive import Passive
from game import Game

firstList = [Aggressive() for i in range(50)] + [Passive() for j in range(50)]
firstGame = Game(firstList)
firstGame.iterate()
