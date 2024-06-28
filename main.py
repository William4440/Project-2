def gameStart():
    #             0,0 0,1 0,2   1,0 1,1 1,2   2,0 2,1 2,2
    #              TL  T   TR    L   M   R     BL  B   BR
    #              |   |   |     |   |   |     |   |   |
    #              |   |   |     |   |   |     |   |   |
    #             \|/ \|/ \|/   \|/ \|/ \|/   \|/ \|/ \|/ 
    gameArray = [[" "," "," "],[" "," "," "],[" "," "," "]]

    inputVar = ''

    def player_X_wins():
        global gameOver
        print("Player X wins!")

    def player_O_wins():
        global gameOver
        print("Player O wins!")

    def catsGame():
        global gameOver
        print("Cats game!")

    def checkForWinners(gameArray):
        if gameArray[0] == ["X","X","X"]:
            player_X_wins()
            return 1
        elif gameArray[1] == ["X","X","X"]:
            player_X_wins()
            return 1
        elif gameArray[2] == ["X","X","X"]:
            player_X_wins()
            return 1
        elif gameArray[0][0] == "X" and gameArray[1][0] == "X" and gameArray[2][0] == "X":
            player_X_wins()
            return 1
        elif gameArray[0][1] == "X" and gameArray[1][1] == "X" and gameArray[2][1] == "X":
            player_X_wins()
            return 1
        elif gameArray[0][2] == "X" and gameArray[1][2] == "X" and gameArray[2][2] == "X":
            player_X_wins()
            return 1
        elif gameArray[0][2] == "X" and gameArray[1][1] == "X" and gameArray[2][0] == "X":
            player_X_wins()
            return 1
        elif gameArray[0][0] == "X" and gameArray[1][1] == "X" and gameArray[2][2] == "X":
            player_X_wins()
            return 1
        elif gameArray[0] == ["O","O","O"]:
            player_O_wins()
            return 1
        elif gameArray[1] == ["O","O","O"]:
            player_O_wins()
            return 1
        elif gameArray[2] == ["O","O","O"]:
            player_O_wins()
            return 1
        elif gameArray[0][0] == "O" and gameArray[1][0] == "O" and gameArray[2][0] == "O":
            player_O_wins()
            return 1
        elif gameArray[0][1] == "O" and gameArray[1][1] == "O" and gameArray[2][1] == "O":
            player_O_wins()
            return 1
        elif gameArray[0][2] == "O" and gameArray[1][2] == "O" and gameArray[2][2] == "O":
            player_O_wins()
            return 1
        elif gameArray[0][2] == "O" and gameArray[1][1] == "O" and gameArray[2][0] == "O":
            player_O_wins()
            return 1
        elif gameArray[0][0] == "O" and gameArray[1][1] == "O" and gameArray[2][2] == "O":
            player_O_wins()
            return 1
        elif not gameArray[0][0] == " " and not gameArray[0][1] == " " and not gameArray[0][2] == " " and not gameArray[1][0] == " " and not gameArray[1][1] == " " and not gameArray[1][2] == " " and not gameArray[2][0] == " " and not gameArray[2][1] == " " and not gameArray[2][2] == " ":
            catsGame()
            return 1
        else:
            return 0

    def printGame():
        print(gameArray[0][0] + " |" + gameArray[0][1] + " |" + gameArray[0][2])
        print("--+--+--")
        print(gameArray[1][0] + " |" + gameArray[1][1] + " |" + gameArray[1][2])
        print("--+--+--")
        print(gameArray[2][0] + " |" + gameArray[2][1] + " |" + gameArray[2][2])

    def turnFunc(player):
        printGame()
        print("Turn: " + player)
        def gameOver():
            inputVar = input("Play again (Y/N) ")
            if inputVar == "Y":
                gameStart()
            elif inputVar == "N":
                pass
            else:
                print("Please enter a valid input")
                gameOver()
        def askForInput(turn):
            global inputVar

            inputVar = input("TL T TR L M R BL B BR (select a square) ")
            if turn == "O":
                if inputVar == "TL" and gameArray[0][0] == " ":
                    gameArray[0][0] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "T" and gameArray[0][1] == " ":
                    gameArray[0][1] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "TR" and gameArray[0][2] == " ":
                    gameArray[0][2] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "L" and gameArray[1][0] == " ":
                    gameArray[1][0] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "M" and gameArray[1][1] == " ":
                    gameArray[1][1] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "R" and gameArray[1][2] == " ":
                    gameArray[1][2] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "BL" and gameArray[2][0] == " ":
                    gameArray[2][0] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "B" and gameArray[2][1] == " ":
                    gameArray[2][1] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                elif inputVar == "BR" and gameArray[2][2] == " ":
                    gameArray[2][2] = "O"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("X")
                else:
                    print("Please enter a valid input")
                    turnFunc("O")
            elif turn == "X":
                if inputVar == "TL" and gameArray[0][0] == " ":
                    gameArray[0][0] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "T" and gameArray[0][1] == " ":
                    gameArray[0][1] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "TR" and gameArray[0][2] == " ":
                    gameArray[0][2] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "L" and gameArray[1][0] == " ":
                    gameArray[1][0] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "M" and gameArray[1][1] == " ":
                    gameArray[1][1] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "R" and gameArray[1][2] == " ":
                    gameArray[1][2] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "BL" and gameArray[2][0] == " ":
                    gameArray[2][0] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "B" and gameArray[2][1] == " ":
                    gameArray[2][1] = "X"
                    if checkForWinners(gameArray) == 1:
                        gameOver()
                    elif checkForWinners(gameArray) == 0:
                        turnFunc("O")
                elif inputVar == "BR" and gameArray[2][2] == " ":
                    gameArray[2][2] = "X"
                    turnFunc("O")
                else:
                    print("Please enter a valid input")
                    turnFunc("X")

        askForInput(player)

    turnFunc("X")

gameStart()