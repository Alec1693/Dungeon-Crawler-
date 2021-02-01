import sys
from random import randint


def main():
    setupVars = []
    setupVars = Setup() ##assign the list setupVars to accept the function Setup() list
    board = setupVars[0] ##2d board array is the first element of setupVars, create variable to hold this list index
    pogIndex = setupVars[1] ##first index value of where pot of gold is located
    userIndex = setupVars[2] ##userIndex 0,0
    gameOver = False ##bool variable to check if game is complete before running main again
    board[userIndex[0]][userIndex[1]] = 1 ##denotes the location of user on the board, starting location 0,0 now displays 1
    ##assign a variable to function Welcome
    isWelcome = Welcome()
    ##if the user types the correct input Welcome() returns true, and passes through if statement
    if isWelcome:
        ##add userIndex location to gameboard
        ShowBoard(board)
        while gameOver == False: 
            direction = UserDirection() ##map the func call UserDirection to a variable to hold the direction they select
            if direction == 1:##Up direction
                updateIndex = Move(direction,userIndex) ##map func Move to a variable that holds the updated index if the index location is valid, if not it returns false
                if updateIndex != False:
                    board = SwapSpaces(board,userIndex,updateIndex) ##func supposed to swap 1 and 0 locations for the current user index
                    ShowBoard(board)
                    userIndex = updateIndex ##change the users index to the updated index location
                    print(str(userIndex))
                    ##check if the location is the pot of gold
                    if userIndex == pogIndex:
                        gameOver = True
                        WinnerDisplay()
                        break

                    ##if so change gameOver bool to True
                else:
                    print("You can't move up anymore.")
            elif direction == 2:
                updateIndex = Move(direction,userIndex)
                if updateIndex != False:
                    board = SwapSpaces(board,userIndex,updateIndex)
                    ShowBoard(board)
                    userIndex = updateIndex
                    print(str(userIndex))
                    ##check if the location is the pot of gold
                    if userIndex == pogIndex:
                        gameOver = True
                        WinnerDisplay()
                        break
                else:
                    print("You can't move down anymore.")
            elif direction == 3:
                updateIndex = Move(direction,userIndex)
                if updateIndex != False:
                    board = SwapSpaces(board,userIndex,updateIndex)
                    ShowBoard(board)
                    userIndex = updateIndex
                    print(str(userIndex))
                    ##check if the location is the pot of gold
                    if userIndex == pogIndex:
                        gameOver = True
                        WinnerDisplay()
                        break
                else:
                    print("You can't move left anymore.")
            elif direction == 4:
                updateIndex = Move(direction,userIndex)
                if updateIndex != False:
                    board = SwapSpaces(board,userIndex,updateIndex)
                    ShowBoard(board)
                    userIndex = updateIndex
                    print(str(userIndex))
                    ##check if the location is the pot of gold
                    if userIndex == pogIndex:
                        gameOver = True
                        WinnerDisplay()
                        break
                else:
                    print("You can't move right anymore.")
            elif direction == 5:
                print("I guess I can help you cheat >;).. \nThe Pot of Gold Location is " + str(pogIndex))
            else:
                print("That's not a valid direction")

def WinnerDisplay():
    message = print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou found the Pot of Gold!! \n\nNow take your loot and scram!")
    return message


def SwapSpaces(board,userIndex,updateIndex):
    newBoard = Setup() ##create a new var to grab a new board array
    newBoard = newBoard[0]
    newBoard[updateIndex[0]][updateIndex[1]] = 1
    return newBoard

def Move(direction,userIndex):
    if direction == 1:##
        tempIndex = userIndex[0] ##hold the value of the current index in a temp location
        tempIndex += 1##increment the temp index by 1 since movement is up
        if tempIndex > 9: ##if the temp Index is more than 9 it is out of bounds
            return False
        else:
            userIndex[0] = tempIndex ##the temp index is in bounds, so we change the value of the userIndex to hold next move(tempIndex)
            return userIndex
    elif direction == 2:
        tempIndex = userIndex[0]
        tempIndex -= 1
        if tempIndex < 0:
            return False
        else:
            userIndex[0] = tempIndex
            return userIndex
    elif direction == 3:
        tempIndex = userIndex[1]
        tempIndex -= 1
        if tempIndex < 0:
            return False
        else:
            userIndex[1] = tempIndex
            return userIndex
    elif direction == 4:
        tempIndex = userIndex[1]
        tempIndex += 1
        if tempIndex > 9:
            return False
        else:
            userIndex[1] = tempIndex
            return userIndex


##UserDirection function accepts inputs w,a,s,d as directional movement request
##if the input isn't a string the func notifies the user the input is incorrect/runs until they type a string
##return int value for direction, or false if no valid input option is selected
def UserDirection():
    while True:
        try:
            userKey = str(input("\n:"))
        except ValueError:
            print("Sorry, that input is incorrect")
        else:
            break
    userKey = userKey.lower()

    if userKey == "w":
        return 1
    elif userKey == "s":
        return 2
    elif userKey == "a":
        return 3
    elif userKey == "d":
        return 4
    elif userKey == "h":
        return 5
    else:
        return False
        


def ShowBoard(board):
    print("\n\tFind the Pot of Gold\n\n" + "\t" + 
    str(board[9][0]) + " " + str(board[9][1]) + " " + str(board[9][2]) + " " + str(board[9][3]) + " " + str(board[9][4]) + " " + str(board[9][5]) + " " + str(board[9][6]) + " " + str(board[9][7]) + " " + str(board[9][8]) + " " + str(board[9][9]) +
    "\n" + "\t" + str(board[8][0]) + " " + str(board[8][1]) + " " + str(board[8][2]) + " " + str(board[8][3]) + " " + str(board[8][4]) + " " + str(board[8][5]) + " " + str(board[8][6]) + " " + str(board[8][7]) + " " + str(board[8][8]) + " " + str(board[8][9]) +
    "\n" + "\t" + str(board[7][0]) + " " + str(board[7][1]) + " " + str(board[7][2]) + " " + str(board[7][3]) + " " + str(board[7][4]) + " " + str(board[7][5]) + " " + str(board[7][6]) + " " + str(board[7][7]) + " " + str(board[7][8]) + " " + str(board[7][9]) +
    "\n" + "\t" + str(board[6][0]) + " " + str(board[6][1]) + " " + str(board[6][2]) + " " + str(board[6][3]) + " " + str(board[6][4]) + " " + str(board[6][5]) + " " + str(board[6][6]) + " " + str(board[6][7]) + " " + str(board[6][8]) + " " + str(board[6][9]) +
    "\n" + "\t" + str(board[5][0]) + " " + str(board[5][1]) + " " + str(board[5][2]) + " " + str(board[5][3]) + " " + str(board[5][4]) + " " + str(board[5][5]) + " " + str(board[5][6]) + " " + str(board[5][7]) + " " + str(board[5][8]) + " " + str(board[5][9]) +
    "\n" + "\t" + str(board[4][0]) + " " + str(board[4][1]) + " " + str(board[4][2]) + " " + str(board[4][3]) + " " + str(board[4][4]) + " " + str(board[4][5]) + " " + str(board[4][6]) + " " + str(board[4][7]) + " " + str(board[4][8]) + " " + str(board[4][9]) +
    "\n" + "\t" + str(board[3][0]) + " " + str(board[3][1]) + " " + str(board[3][2]) + " " + str(board[3][3]) + " " + str(board[3][4]) + " " + str(board[3][5]) + " " + str(board[3][6]) + " " + str(board[3][7]) + " " + str(board[3][8]) + " " + str(board[3][9]) +
    "\n" + "\t" + str(board[2][0]) + " " + str(board[2][1]) + " " + str(board[2][2]) + " " + str(board[2][3]) + " " + str(board[2][4]) + " " + str(board[2][5]) + " " + str(board[2][6]) + " " + str(board[2][7]) + " " + str(board[2][8]) + " " + str(board[2][9]) +
    "\n" + "\t" + str(board[1][0]) + " " + str(board[1][1]) + " " + str(board[1][2]) + " " + str(board[1][3]) + " " + str(board[1][4]) + " " + str(board[1][5]) + " " + str(board[1][6]) + " " + str(board[1][7]) + " " + str(board[1][8]) + " " + str(board[1][9]) +
    "\n" + "\t" + str(board[0][0]) + " " + str(board[0][1]) + " " + str(board[0][2]) + " " + str(board[0][3]) + " " + str(board[0][4]) + " " + str(board[0][5]) + " " + str(board[0][6]) + " " + str(board[0][7]) + " " + str(board[0][8]) + " " + str(board[0][9]))

def Setup():
##initialize board list
    board = []
##nested for, creates 10 lists,10 elements in each
    for i in range(10):
        new = []
        for j in range(10):
            new.append(0)
        board.append(new)
##create 2 random numbers between 0 and 9
##these numbers are coordinates that will pass to the pogIndex
    val1 = randint(0, 9)
    val2 = randint(0, 9)
    pogIndex = [val1,val2]
##create the starting index for the player
    startIndex = [0,0]

    return [board,pogIndex,startIndex]  

##Func prints greeting to user, asks if they wish to play
##if so func returns True, if not the program terminates 
def Welcome():
    print("I hope you're feeling lucky! Would you like to search for the \n\t\t\tPot of Gold?\n\nPress 1 to Start\nPress 2 to Quit\n")
    while True:
        try:
            userInput = int(input(":"))
        except ValueError:
            print("Sorry, that isn't a valid input. Try again")
            continue
        else:
            break

    if userInput == 1:
        print("Welcome to the Hunt! The movements of this game are \n\n\t\t     UP(W)\n\t\tLEFT(A)\tRIGHT(D)\n\t\t    DOWN(S)\n\n" +
          "You must hit ENTER after every movement selection.\n\nP.S. If you want to cheat and reveal the Pot of Gold location, type H")
        return True
    else:
        sys.exit(0)

main()



