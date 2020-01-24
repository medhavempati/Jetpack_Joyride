import random
from characters import Character, Mandalorian

def activateShield(mandalorian):
    mandalorian.shield = 1
    return

def speedUp(mandalorian):
    mandalorian.speed = 2
    return

def shieldTimer(board, mandalorian):
    if board.shieldOn <= 10 and board.shieldOn >0:
        board.shieldOn -= 1
        return

    elif board.shieldOn <= 0:
        mandalorian.shield = 0
        board.shieldOn = 11
        board.shieldWait = 60
        board.shieldPermission = 0
        return

    else:
        return

def shieldRegenerate(board, mandalorian):
    if board.shieldWait <= 60:
        board.shieldWait -= 1
        return
    
    elif board.shieldWait <= 0:
        board.shieldWait = 61
        board.shieldPermission = 1
        return
    
    else:
        return

class SpeedPowerUp:
    def __init__(self, board):
        self.xPos = 0
        self.yPos = 0
        self.board = board

    def generateRandomPowerUp(self):

        speedNumber = random.randint(3, 6)

        for i in range(speedNumber):
            speedX = random.randint(0, self.board.totalWidth - 200)
            speedY = random.randint(self.board.ceilingHeight, self.board.height - self.board.groundHeight)

            if((self.board.boardDesign[speedX + i][speedY] != " ") or (speedX + i >= self.board.totalWidth)):
                continue
            else:
                self.board.boardDesign[speedX + self.board.boardSection + i][speedY] = ">>"

        return

def speedTimer(board, mandalorian):
    print("time left: " + str(board.speedTime), end="")
    print("speed: " + str(mandalorian.speed), end="")
    if board.speedTime <= 30 and board.speedTime > 0:
        board.speedTime -= 1
    
    elif board.speedTime <= 0:
        mandalorian.speed = 1
        board.speedTime = 31
