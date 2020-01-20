import sys
import time
import input
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
    i=0
    for i in range(10):
        inputKey = input.get()

        if inputKey == 'q':
            endGame()

        elif mandalorian.lives == 0:
            endGame()
        
        else:
            print("i = "+str(i))
            board.displayGameView()

        

