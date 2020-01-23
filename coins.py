import random

class Coins:

    def __init__(self, board):
        self.xPos = 0
        self.yPos = 0
        self.length = 0
        self.board = board

    def generateRandomCoins(self):
        coinNumber = random.randint(100, 200)

        for i in range(coinNumber):
            coinLength = random.randint(5, 10)
            coinX = random.randint(0, self.board.totalWidth - 200)
            coinY = random.randint(self.board.ceilingHeight, self.board.height - self.board.groundHeight)
            i+=1

            for i in range(coinLength):
                if((self.board.boardDesign[coinX + i][coinY] != " ") or (coinX + i >= self.board.totalWidth)):
                    break
                else:
                    self.board.boardDesign[coinX + self.board.boardSection + i][coinY] = "$"
        return
        
