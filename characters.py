from gameView import GameView
from gameplay import board

class Character:

    def __init__(self):
        self.form = [["B"]]

        self.xPos = 0
        self.yPos = board.viewFrameHeight - board.groundHeight

        self.lives = 3
        self.score = 0

    def moveUp(self):
        self.yPos = self.yPos + 1

    def moveLeft(self):
        self.xPos = self.xPos - 1

    def moveRight(self):
        self.xPos = self.xPos + 1
