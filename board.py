import numpy
import random
import colorama
from zappers import Zapper, VerticalZapper, HorizontalZapper, LeftZapper, RightZapper

class Board:
    def __init__(self):
        
        self.height = 40
        self.frameWidth = 190
        self.totalWidth = 1500

        self.boardSection = 0 
        self.boardDesign = [[" " for x in range(self.height)] for y in range(self.totalWidth)]

        self.ceilingHeight = 2
        self.groundHeight = 4

        self.mandoLives = 5
        self.mandoScore = 0

        self.timeTrack = 0

        self.shieldOn = 11
        self.shieldWait = 61
        self.shieldPermission = 1

        self.speedTime = 31

        for i in range(self.totalWidth):
            for j in range(self.ceilingHeight):
                self.boardDesign[i][j] = "C"

            for j in range(self.height - self.groundHeight, self.height):
                self.boardDesign[i][j] = "G"
        x = 20
        y = 15
        for i in range(10):
            self.boardDesign[x][y+i] = "."

    def originalDisplayBoard(self):
        print("\033[0;0H]")

        # self.boardSection += 1

        print('Lives: ' + str(self.mandoLives))
        print('Score: ' + str(self.mandoScore))

        for i in range(self.height):
            for j in range(self.boardSection, self.boardSection + self.frameWidth):
                print(self.boardDesign[j][i], end = "")
            print()

        return

    def displayBoard(self):
        print("\033[0;0H")

        print(colorama.Back.BLACK + colorama.Fore.WHITE + 'Lives: ' + str(self.mandoLives))
        print(colorama.Back.BLACK + colorama.Fore.WHITE + 'Score: ' + str(self.mandoScore))
        print(colorama.Back.BLACK + colorama.Fore.WHITE + "Time: " + str(self.timeTrack))

        for i in range(self.height):
            for j in range(self.boardSection, self.boardSection + self.frameWidth):
                if self.boardDesign[j][i] == " ":
                    print(colorama.Back.BLACK + " ", end="")
                elif self.boardDesign[j][i] == "C":
                    print(colorama.Back.CYAN + "*", end="")
                elif self.boardDesign[j][i] == "G":
                    print(colorama.Back.CYAN + " ", end="")
                elif self.boardDesign[j][i] == "X":
                    print(colorama.Back.BLACK + colorama.Fore.WHITE + "X", end="")
                elif self.boardDesign[j][i] == "M":
                    print(colorama.Back.MAGENTA + " ", end="")
                elif self.boardDesign[j][i] == "$":
                    print(colorama.Back.BLACK + colorama.Fore.YELLOW + "$", end="")
                elif self.boardDesign[j][i] == ">>":
                    print(colorama.Back.RED + colorama.Fore.YELLOW + ">>", end="")
                
            print()

        return

