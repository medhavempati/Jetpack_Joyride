import random

class Coins:

    def __init__(self, board):
        self.xPos = 0
        self.yPos = 0
        self.length = 0
        self.board = board

    def display(self, xPos, yPos, length, board):
        for i in range(self.length):
            if(self.board.boardDesign[self.xPos + self.board.boardSection + i][self.yPos] != " "):
                self.board.displayBoard()
                return
            else:
                self.board.boardDesign[self.xPos + self.board.boardSection + i][self.yPos] = "$"
        self.board.displayBoard()
        return

    def generateRandomCoins(self):
        coinNumber = random.randint(5, 10)

        for i in range(coinNumber):
            coinLength = random.randint(5, 10)
            coinX = random.randint(self.board.boardSection, self.board.boardSection + self.board.frameWidth)
            coinY = random.randint(self.board.ceilingHeight, self.board.height - self.board.groundHeight)
            i+=1

            for i in range(coinLength):
                if(self.board.boardDesign[coinX + self.board.boardSection + i][coinY] != " "):
                    self.board.displayBoard()
                    break
                else:
                    self.board.boardDesign[coinX + self.board.boardSection + i][coinY] = "$"
            self.board.displayBoard()
        
