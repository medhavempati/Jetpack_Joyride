from gameplay import startGame, endGame
from gameView import GameView

def displayOptions():
    option = input("Press S to start playing\nPress Q to quit\n")

    if option == "s":
        startGame()
        board = GameView(20, 200)
        board.displayGameView()
    elif option == "q":
       endGame()
    else:
      print("Invalid option\nPlease choose from among the displayed options\n")
      displayOptions()
