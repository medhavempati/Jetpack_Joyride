from gameView import GameView
import gameplay

class Character:

    def __init__(self, height, width, form):
        self.height = height
        self.width = width
        self.form = form

        self.xPos = 0
        self.yPos = gameplay.board.viewFrameHeight - gameplay.board.groundHeight

        self.lives = 3
        self.score = 0

    def moveUp(self):
        self.yPos = self.yPos + 1

    def moveLeft(self):
        self.xPos = self.xPos - 1

    def moveRight(self):
        self.xPos = self.xPos + 1

    def position(self):
        for x in range(self.width):
            for y in range(self.height):
                gameplay.board.viewDesign[gameplay.board.viewSection + self.xPos + x ][self.yPos + y - self.height] = self.form[x][y]

def Mandalorian():

    height = 4
    width = 3
    form = [["M" for x in range(height)] for y in range(width)]
    mandalorian = Character(height, width, form)

    return mandalorian
