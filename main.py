#---------Global Variable---------

#Game Board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]
#Game Still Going 
gameStillGoing = True
#Who Won or Lost
winner = None
#Whose turn is it
currentPlayer = "X"

#Display the board
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#Play the game
def playGame():
    #Display initial board
    displayBoard()

    #Loop while game continues
    while gameStillGoing:
        handleTurn(currentPlayer)
        
        checkIfGameOver()

        #flip between the players
        flipPlayer()

        #The game has ended here

    if winner == "X" or winner == "O" :
        print(winner + " won!") 
    elif winner == "None":
        print("Tie.")


def handleTurn(player):
    position = input("Chose a position from 1-9: ")
    position = (int)(position) - 1

    board[position] = 'X'
    displayBoard();


def checkIfGameOver():
    checkIfWin()
    checkIfTie()


def flipPlayer():
    return

def checkIfWin():

    #Sets up global var, allows us to use winner
    global winner


    #check rows
    rowWinner = checkRows()
    #check coloumns
    columnWinner = checkColumns()
    #check diaganols
    diaganolWinner = checkDiaganols()

    
    if rowWinner:
        winner = rowWinner()
    elif columnWinner:
        winner = columnWinner()
    elif diaganolWinner:
        winner = diaganolWinner()
    else:
        winner = None
    return


def checkRows():
    #Set up global variable
    global gameStillGoing
    #Check if any of the rows have the same value (and are not empty)
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    #Flag that there is a win if any rows match
    if row1 or row2 or row3:
        gameStillGoing = False
    #Return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkColumns():
    return


def checkDiaganols():
    return


def checkIfTie():
    #check rows
    #check coloumns
    #check diagnols
    return


playGame()