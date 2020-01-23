from board import Board
import input
from makeCharacterForm import makeMando
from characters import Character, Mandalorian
from zappers import Zapper, VerticalZapper, HorizontalZapper, LeftZapper, RightZapper
from coins import Coins

board = Board()
form = makeMando()
mandalorian = Mandalorian(4, 3, form, board)
zapper = Zapper(0, 0, 0, board)
coins = Coins(board)

def startGame():

    mandalorian.addToBoard()
    zapper.generateRandomZappers()
    coins.generateRandomCoins()
    board.displayBoard()


    while(1):
        inputKey = input.get()
        checkMovement(mandalorian, board, "")
        board.timeTrack += 1

        if inputKey == "w":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveUp()
            if checkMovement(mandalorian, board, inputKey) == 0:
                mandalorian.lives -= 1
                mandalorian.moveUp()
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveUp()

        elif inputKey == "d":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 0:
                mandalorian.lives -= 1
                mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveRight()

        elif inputKey == "a":
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveLeft()
            if checkMovement(mandalorian, board, inputKey) == 0:
                mandalorian.lives -= 1
                mandalorian.moveLeft()
            if checkMovement(mandalorian, board, inputKey) == 3:
                mandalorian.score += 5
                mandalorian.moveLeft()

        elif inputKey == "q":
            print("Game Over!\n")
            break

        elif mandalorian.lives <= 0:
            print("You Died!\n")
            break

        elif inputKey == "":
            # mandalorian.moveRight()
            if checkMovement(mandalorian, board, inputKey) == 1:
                mandalorian.moveDown()
            if checkMovement(mandalorian, board, inputKey) == 0:
                mandalorian.lives -= 1
                mandalorian.moveDown()
        
        moveBoard(board, mandalorian)
        board.displayBoard()

def moveBoard(board, mandalorian):
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
    '''

    if inputKey == "d":
        if (mandalorian.xPos + mandalorian.width + board.boardSection) >= (board.boardSection + board.frameWidth):
            return 4
        for i in range(mandalorian.yPos, mandalorian.yPos + mandalorian.height):
            if board.boardDesign[mandalorian.xPos + mandalorian.width + board.boardSection][-i -1 -board.groundHeight ] == "X":
                return 0
            elif board.boardDesign[mandalorian.xPos + mandalorian.width + board.boardSection][-i -1 -board.groundHeight ] == "$":
                return 3
    
    elif inputKey == "a":
        if (mandalorian.xPos - 1 + board.boardSection) <= board.boardSection :
            return 4
        for i in range(-mandalorian.yPos, mandalorian.yPos + mandalorian.height):
            if board.boardDesign[mandalorian.xPos - 1 + board.boardSection][-i -1 -board.groundHeight ] == "X":
                return 0
            elif board.boardDesign[mandalorian.xPos - 1 + board.boardSection][-i -1 -board.groundHeight ] == "$":
                return 3

    elif inputKey == "w":
        for i in range(mandalorian.xPos, mandalorian.xPos + mandalorian.width):
            if board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "X":
                return 0
            elif board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "C":
                return 2
            elif board.boardDesign[i][-mandalorian.yPos - mandalorian.height - board.groundHeight - 1] == "$":
                return 3

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
    return 1
        