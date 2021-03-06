from board import Board
import time
import input
from makeCharacterForm import makeMando, makeBoss
from characters import Character, Mandalorian, Boss, moveBoss
from zappers import Zapper, VerticalZapper, HorizontalZapper, LeftZapper, RightZapper
from coins import Coins
# from powerUps import activateShield, speedUp, shieldTimer, SpeedPowerUp, speedTimer

board = Board()

mandoForm = makeMando()
mandalorian = Mandalorian(4, 3, mandoForm, board)

bossForm = makeBoss()
boss = Boss(bossForm, board)

zapper = Zapper(0, 0, 0, board)
coins = Coins(board)
# speedPowerUps = SpeedPowerUp(board)

# timeTrack = 1
# mandoLives = 5
# mandoScore = 0

def startGame():

    mandalorian.addToBoard()
    zapper.generateRandomZappers()
    coins.generateRandomCoins()
    # speedPowerUps.generateRandomPowerUp()

    board.displayBoard()

    while(1):
        inputKey = input.get()
        checkMovement(mandalorian, board, "")
        board.timeTrack += 1

        # shieldTimer(board, mandalorian)
        # speedTimer(board, mandalorian)

        if inputKey == "w":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveUp()
                moveBoss(boss, mandalorian, board)
            if checkMovement(mandalorian, board, inputKey) == 0:
                # if mandalorian.shield == 0:
                board.mandoLives -= 1
                    # mandalorian.shield = 0
                mandalorian.moveUp()
                moveBoss(boss, mandalorian, board)
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveUp()
                moveBoss(boss, mandalorian, board)
            # if checkMovement(mandalorian, board, inputKey) == 5:
            #     mandalorian.speed = 2
            #     board.speedTime = 30
            #     mandalorian.moveUp()

        elif inputKey == "d":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 0:
                # if mandalorian.shield == 0:
                board.mandoLives -= 1
                    # mandalorian.shield = 0
                mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveRight()
            # if checkMovement(mandalorian, board, inputKey) == 5:
            #     mandalorian.speed = 2
            #     mandalorian.moveRight()

        elif inputKey == "a":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveLeft()
            if checkMovement(mandalorian, board, inputKey) == 0:
                # if mandalorian.shield == 0:
                board.mandoLives -= 1
                    # mandalorian.shield = 0
                mandalorian.moveLeft()
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveLeft()
            # if checkMovement(mandalorian, board, inputKey) == 5:
            #     mandalorian.speed = 2
            #     mandalorian.moveLeft()

        elif inputKey == "q":
            print("Game Over!\n")
            break

        # elif board.mandoLives <= 0:
        #     print("You Died!\n")
        #     break

        elif inputKey == "" or "s":
            # mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveDown()
                moveBoss(boss, mandalorian, board)
            if checkMovement(mandalorian, board, inputKey) == 0:
                # if mandalorian.shield == 0:
                board.mandoLives -= 1
                    # mandalorian.shield = 0
                mandalorian.moveDown()
                moveBoss(boss, mandalorian, board)
            # if checkMovement(mandalorian, board, inputKey) == 5:
            #     mandalorian.speed = 2
            #     mandalorian.moveDown()

        # elif inputKey == " " and board.shieldPermission == 1:
        #     activateShield(mandalorian)
        #     board.shieldOn -= 1
        
        moveBoard(board, mandalorian)
        board.displayBoard()
        
        time.sleep(0.01)

# def displayStats(timeTrack, mandoLives, mandoScore, board):
    
#     print("\033[0;0H]")


def moveBoard(board, mandalorian):

    if(board.boardSection < board.totalWidth - 190):
        for i in range(mandalorian.height):
                for j in range(mandalorian.width):
                    board.boardDesign[board.boardSection + j + mandalorian.xPos][-board.groundHeight - i -1 - mandalorian.yPos] = " "

        board.boardSection += 1

        mandalorian.addToBoard()

def checkMovement(mandalorian, board, inputKey):

    '''
    return 0 -> Barrier (.)
    return 1 -> Clear
    return 2 -> Ground/Ceiling
    return 3 -> Coins
    return 4 -> Out_Of_Frame
    return 5 -> Speed Power Up
    '''

    if inputKey == "d":
        if (mandalorian.xPos + mandalorian.width + board.boardSection) >= (board.boardSection + board.frameWidth):
            return 4
        for i in range(mandalorian.yPos, mandalorian.yPos + mandalorian.height):
            if board.boardDesign[mandalorian.xPos + mandalorian.width + board.boardSection][-i -1 -board.groundHeight ] == "X":
                return 0
            elif board.boardDesign[mandalorian.xPos + mandalorian.width + board.boardSection][-i -1 -board.groundHeight ] == "$":
                return 3
            # elif board.boardDesign[mandalorian.xPos + mandalorian.width + board.boardSection][-i -1 -board.groundHeight ] == ">>":
            #     return 5
    
    elif inputKey == "a":
        if (mandalorian.xPos - 1 + board.boardSection) <= board.boardSection :
            return 4
        for i in range(-mandalorian.yPos, mandalorian.yPos + mandalorian.height):
            if board.boardDesign[mandalorian.xPos - 1 + board.boardSection][-i -1 -board.groundHeight ] == "X":
                return 0
            elif board.boardDesign[mandalorian.xPos - 1 + board.boardSection][-i -1 -board.groundHeight ] == "$":
                return 3
            # elif board.boardDesign[mandalorian.xPos - 1 + board.boardSection][-i -1 -board.groundHeight ] == ">>":
            #     return 5

    elif inputKey == "w":
        for i in range(mandalorian.xPos, mandalorian.xPos + mandalorian.width):
            if board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "X":
                return 0
            elif board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "C":
                return 2
            elif board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "$":
                return 3
            # elif board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == ">>":
            #     return 5

    elif inputKey == "":
        if (mandalorian.xPos - 2 + board.boardSection) <= board.boardSection :
            return 4
        for i in range(mandalorian.xPos, mandalorian.xPos + mandalorian.width):
            if board.boardDesign[i][mandalorian.yPos - 1] == "X":
                return 0
            elif board.boardDesign[i][mandalorian.yPos - 1] == "G":
                return 2
            elif board.boardDesign[i][mandalorian.yPos - 1] == "$":
                return 3
            # elif board.boardDesign[i][mandalorian.yPos - 1] == ">>":
            #     return 5
    return 1
        