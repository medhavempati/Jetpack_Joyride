import sys
import time
from gameView import GameView
from characters import Character

board = GameView(40, 190)
mandalorian = Character()

def startGame():
    print("Start Game")

    board.displayGameView()
    gameLoop(board, mandalorian)

def endGame():
    sys.exit("Game Over")

def gameLoop(GameView, Character):
    while(1):
      return  
