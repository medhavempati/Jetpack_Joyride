import sys
from gameplay import startGame

def displayOptions():

    option = input('Press Enter to start playing\nPress Q to quit\n')

    if option == "":
        startGame()
    
    elif option == 'q':
        print('Game Over')

displayOptions()