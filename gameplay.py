import sys
import time
import input
from gameView import GameView
from characters import Character, Mandalorian

board = GameView(40, 190)
mandalorian = Mandalorian()

def startGame():
    print("Start Game")

    mandalorian.position()
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
            mandalorian.position()
            print("i = "+str(i))
            board.displayGameView()

        

