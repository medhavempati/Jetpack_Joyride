import numpy as np
import sys
import random
import time

class GameView:

    def __init__(self, height, width):
        
        self.totalHeight = height
        self.totalWidth = 5000
        self.dimensions = (height, width)
        
        self.groundHeight = int(height/8)       #Ground is 1/8th the height of the screen
        self.ceilingHeight = int(height/15)      #Ceiling is 1/10th the height of the screen
        
        self.viewFrameHeight = height
        self.viewFrameWidth = width
        self.viewSection = 0

        # Design empty space
        self.viewDesign = [[" " for y in range(self.viewFrameHeight)] for x in range(self.viewFrameWidth)]
        
        print("val 1: "+ str(self.viewFrameHeight - self.groundHeight))
        print("val2: " + str(self.viewFrameHeight))

        # Design ground boundary
        for x in range(self.viewFrameWidth):
            for y in range(self.viewFrameHeight - self.groundHeight, self.viewFrameHeight):
                #print(str(x) + "," + str(y) + "\n")
                self.viewDesign[x][y] = "_"
        
        # Design ceiling boundary
        for x in range(self.viewFrameWidth):
            for y in range(int(self.ceilingHeight)):
                self.viewDesign[x][y] = "~"

    def displayGameView(self):
        print("\033[0;0H]")

        for y in range(self.viewFrameHeight):
            for x in range(self.viewSection, self.viewSection+self.viewFrameWidth):
                print(self.viewDesign[x][y], end='')
            print()

    