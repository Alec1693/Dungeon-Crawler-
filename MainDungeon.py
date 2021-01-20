import sys
from NPC import NPC
from GameBoard import GameBoard
from random import randint

def main():
    validInput = False
    gameOver = False
    board = SetBoard()
    position = (0,0)
    ##set up the gameboard object
    realBoard = GameBoard(board,position)
    
    while validInput == False:
        answer = OpeningQuestion()

        if answer == 1:
            ShowBoard(realBoard.get_board())
            ##Open Game Function
            moveChoice = UserMove()
            realBoard.set_cPosition(ChangePosition(moveChoice,realBoard.get_cPosition())) 
            print(str(realBoard.get_cPosition()))
            validInput = True
        elif answer == 2:
            sys.exit(0)
            validInput = True
        else:
            print("Sorry, that's an invalid option. Try again.")

##Func moves player accross board
##if the move is out of the board range it should return as false
def ChangePosition(direction,cPosition):
    if direction == 1:
        ##move up
        tempVal = cPosition[0]
        tempVal += 1
        if cPosition[tempVal] >= 10:
            ##out of range
            return False
        else:
            return cPosition[tempVal]
    elif direction == 2:
        ##move down
        tempVal = cPosition[0]
        tempVal -= 1
        if cPosition[tempVal] < 0:
            return False
        else:
            return cPosition[tempVal]
    elif direction == 3:
        ##move left
        tempVal = cPosition[1]
        tempVal -= 1
        if cPosition[tempVal] < 0:
            return False
        else:
            return cPosition[tempVal]
    elif direction == 4:
        ##move right
        tempVal = cPosition[1]
        tempVal += 1
        if cPosition[tempVal] >= 10:
            return False
        else:
            return cPosition[tempVal]
    else:
        return False


####Function to check bounds of move choice on the board
##def BoundCheck(direction,board,cPosition):
##    ##check that bounds arent greater than 9
##    if board

##This function will get the movement input from the user
def UserMove():
    while True:
        try:
            userSelection = input("Starting point is the bottom left corner.\n You shall type (Left,Right,Up,Down)\nto move across the game board.")
        except ValueError:
            print("Sorry, I didn't understand that movement.")
        else:
            break
    userSelection = userSelection.lower()

    if userSelection == "up":
        return 1
    elif userSelection == "down":
        return 2
    elif userSelection == "left":
        return 3
    elif userSelection == "right":
        return 4
    else:
        return False
        

##function to initialize new game board
def SetBoard():
    board = []
##steps through 10 times, assigning 10 elements to each for i iteration, then appends each row of 10 elements to the board []
    for i in range(10):
        new = []
        for j in range(10):
            new.append(0)
        board.append(new)
    return board
        

def StartNPC():
    npcAlec = NPC("Alec","You found me!",[4,4])
    npcDakoda = NPC("Dakoda","Wassup brudah :)",[6,7])
    npcZach = NPC("Zach","Hola Friendo",[5,2])


def ShowBoard(board):
    print("\t  Dungeon Crawler\n" + "\t" + 
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
##create the starting index for the player
    startIndex = [0,0]

    return [board,val1,val2,startIndex]  

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
          "You must hit ENTER after every movement selection.")
        return True
    else:
        sys.exit(0)

main()



