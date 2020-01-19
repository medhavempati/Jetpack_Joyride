import numpy as np
import sys
import random

class GameView:

    def __init__(self, height, width):
        
        self.height = height
        self.width = width
        self.groundHeight = height/8        #Ground is 1/8th the height of the screen
        self.ceilingHeight = height/10      #Ceiling is 1/10th the height of the screen
        self.dimensions = (height, width)

        # Design empty space
        self.viewDesign = [[" " for x in range(width)] for y in range(height)]
        
        print("val 1: "+ str(self.height - int(self.groundHeight)))
        print("val2: " + str(self.height))

        # Design ground boundary
        for x in range(width):
            for y in range(self.height - int(self.groundHeight), self.height):
                #print(str(x) + "," + str(y) + "\n")
                self.viewDesign[x][y] = "_"
        
        # Design ceiling boundary
        for x in range(width):
            for y in range(int(self.ceilingHeight)):
                self.viewDesign[x][y] = "~"

    def displayGameView(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.viewDesign[x][y], end='')
            print()