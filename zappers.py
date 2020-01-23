import random

class Zapper:
    def __init__(self, startX, startY, length, board):
        self.image = "."
        self.length = length
        self.startX = startX
        self.startY = startY
        # self.type = "v"
        self.board = board
        self.randomZapper = 1

    def generateRandomZappers(self):
        zapperNumber = random.randint(10, 15)
            
        for i in range(zapperNumber):
            zapperType = random.randint(1, 4)
            zapperLength = random.randint(4, 12)
            zapperX = random.randint(self.board.boardSection, self.board.boardSection + self.board.frameWidth)
            zapperY = random.randint(self.board.ceilingHeight, self.board.height - self.board.groundHeight)
            i+=1

            if(zapperType == 1):
                tempZapper = VerticalZapper(zapperX, zapperY, zapperLength, self.board)
                tempZapper.display()

            elif(zapperType == 2):
                tempZapper = HorizontalZapper(zapperX, zapperY, zapperLength, self.board)
                tempZapper.display()
                
            elif(zapperType == 3):
                tempZapper = LeftZapper(zapperX, zapperY, zapperLength, self.board)
                tempZapper.display()
                
            elif(zapperType == 4):
                tempZapper = RightZapper(zapperX, zapperY, zapperLength, self.board)
                tempZapper.display()


class VerticalZapper(Zapper):

    # self.type = "v"
    def display(self):
        for i in range(self.length):
            if(self.board.boardDesign[self.startX + self.board.boardSection][self.startY + i] != " "):
                self.board.displayBoard()
                return
            else:
                self.board.boardDesign[self.startX + self.board.boardSection][self.startY + i] = "X"
        self.board.displayBoard()

class HorizontalZapper(Zapper):

    # self.type = "h"
    def display(self):
        for i in range(self.length):
            if(self.board.boardDesign[self.board.boardSection + self.startX + i][self.startY] != " "):
                self.board.displayBoard()
                return
            else:
                self.board.boardDesign[self.board.boardSection + self.startX + i][self.startY] = "X"
        self.board.displayBoard()

class LeftZapper(Zapper):

    # self.type = "l"
    def display(self):
        for i in range(self.length):
            if (self.board.boardDesign[self.board.boardSection + self.startX - i][self.startY + i] != " "):
                self.board.displayBoard()
                return
            else:
                self.board.boardDesign[self.board.boardSection + self.startX - i][self.startY + i] = "X"
        self.board.displayBoard()

class RightZapper(Zapper):

    # self.type = "r"
    def display(self):
        for i in range(self.length):
            if(self.board.boardDesign[self.board.boardSection + self.startX + i][self.startY + i] != 0):
                self.board.displayBoard()
                return
            else:
                self.board.boardDesign[self.board.boardSection + self.startX + i][self.startY + i] = "X"
        self.board.displayBoard()
