from gameplay import startGame, endGame

def displayOptions():
    option = input("Press S to start playing\nPress Q to quit\n")

    if option == "s":
        startGame()
    elif option == "q":
       endGame()
    else:
      print("Invalid option\nPlease choose from among the displayed options\n")
      displayOptions()
