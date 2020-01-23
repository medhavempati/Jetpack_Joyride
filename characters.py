from board import Board

class Character:
    
    def __init__(self, height, width, form, board):

        self.height = height
        self.width = width
        self.form = form

        self.xPos = 0
        self.yPos = 0
        
        self.lives = 5
        self.score = 0

        self.board = board

    def moveUp(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        self.yPos += 1

        self.addToBoard()

    def moveDown(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        self.yPos -= 1

        self.addToBoard()

    def moveLeft(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        self.xPos -= 1

        self.addToBoard()

    def moveRight(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = " "

        self.xPos += 1

        self.addToBoard()
    
    def addToBoard(self):
        self.board.mandoLives = self.lives
        self.board.mandoScore = self.score
        for i in range(self.height):
            for j in range(self.width):
                self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = self.form[j][-i-1]
        # j = self.xPos+self.width
        # for i in range(self.height):
        #         self.board.boardDesign[self.board.boardSection + j + self.xPos][-self.board.groundHeight - i -1 - self.yPos] = "f"


class Mandalorian(Character):
    pass
