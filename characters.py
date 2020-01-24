from board import Board

class Character:
    
    def __init__(self, height, width, form, board):

        self.height = height
        self.width = width
        self.form = form

        self.xPos = 0
        self.yPos = 0
        
        # self.lives = 5
        self.score = 0

        self.board = board

        self.shield = 0
        self.speed = 1

    def moveUp(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "
        if self.speed == 1:
            self.yPos += 1
        elif self.speed == 2:
            self.yPos += 2

        self.addToBoard()

    def moveDown(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "
        if self.speed == 1:
            self.yPos -= 1
        elif self.speed == 2:
            self.yPos -= 2

        self.addToBoard()

    def moveLeft(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        if self.speed == 1:
            self.xPos -= 2
        elif self.speed == 2:
            self.xPos -= 3

        self.addToBoard()

    def moveRight(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        if self.speed == 1:
            self.xPos += 1
        elif self.speed == 2:
            self.xPos += 2

        self.addToBoard()
    
    def addToBoard(self):
        # self.board.mandoLives = self.lives
        # self.board.mandoScore = self.score
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = self.form[j][-i-1]
        # j = self.xPos+self.width
        # for i in range(self.height):
        #         self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = "f"


class Mandalorian(Character):
    pass

class Boss:
    def __init__(self, form, board):

        self.height = 6
        self.width = 5
        self.form = form

        self.yPos = 0

        self.board = board

        self.lives = 15

    def addBossToBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.totalWidth - 10 + j][-self.board.groundHeight -i -1 - self.yPos] = self.form[j][-i-1]

def moveBoss(boss, mandalorian, board):
    for i in range(boss.height):
            for j in range(boss.width):
                board.boardDesign[board.totalWidth - 10 + j][-board.groundHeight - i -1 - boss.yPos] = " "
    
    boss.yPos = mandalorian.yPos

    boss.addBossToBoard()

