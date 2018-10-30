import copy
import random


#proyecto4 Othello
#Adrian Biller A01018940


boardsize = 8
#declaring board
board = [['|  ' for x in range(boardsize)] for y in range(boardsize)]

#initializing four chips in center
def createBoard():
    #getting center value
    initialpos = int((boardsize - 2) / 2)
    #setting initial black chips
    board[initialpos][initialpos] = '| B'
    board[boardsize -(initialpos+1)][boardsize - (initialpos+1)] = '| B'
    #setting initial white chips
    board[boardsize - (initialpos+1)][initialpos] = '| W'
    board[initialpos][boardsize -(initialpos+1)] = '| W'











def movePosition(board, x, y, player):
    #position is off board
    if(x < 0 or x > boardsize - 1 or y < 0 or y > boardsize - 1):
        return False
    #position is taken
    if (board[y][x] != '|  '):
        return False
    #checking the turned chips if making that move
    temp = copy.deepcopy(board)
    tempBoard, turnedChips = playerMove(temp, x, y, player)
    #no turned chips so move is not valid
    if (turnedChips == 0):
        return False
    #Move is valid
    return True


def playerMove(board, x, y, player_color):
    #directions where chips could be turned
    xDirections = [-1, 0, 1, -1, 1, -1, 0, 1]
    yDirections = [-1, -1, -1, 0, 0, 1, 1, 1]
    turnedChips = 0
    #placing player chip
    board[y][x] = player_color
    #checking all directions
    for j in range(len(yDirections)):
        tempChips = 0
        for i in range(boardsize):
            #getting positions for possible temporary chips that could be turned
            jx = x + xDirections[j] * (i + 1)
            jy = y + yDirections[j] * (i + 1)
            if (jx < 0 or jx > boardsize - 1 or jy < 0 or jy > boardsize - 1):
                tempChips = 0;
                break
            elif board[jy][jx] == player_color:
                break
            elif board[jy][jx] == '|  ':
                tempChips = 0;
                break
            else:
                tempChips += 1
        for i in range(tempChips):
            dx = x + xDirections[j] * (i + 1)
            dy = y + yDirections[j] * (i + 1)
            board[jy][jx] = player_color
            #returning turned chips from the temporary
        turnedChips += tempChips
    return(board, turnedChips)

def checkFullBoard(board, player_color):
    for y in range(boardsize):
        for x in range(boardsize):
            #checking all possible moves that can be done
            if movePosition(board, x, y, player_color):
                return False
    return True

def getFinalScore(board, player_color):
    score = 0
    for y in range(boardsize):
        for x in range(boardsize):
            if board[y][x] == player_color:
                if((x == 0 or x == boardsize - 1) and (y == 0 or y == boardsize - 1)):
                    score += 4
                elif( (x == 0 or x == boardsize - 1) or (y == 0 or y == boardsize - 1)):
                    score += 2
                else:
                    score += 1
    return score


def aiTurn(board, player_color):
    maxPoints = 0
    mx = -1; my = -1
    for y in range(boardsize):
        for x in range(boardsize):
            if movePosition(board, x, y, player_color):
                temp = copy.deepcopy(board)
                #getting temporary board and possible chips turned
                tempBoard, turnedChips = playerMove(temp, x, y, player_color)
                #getting possible points from minimax algorithm
                points = MinMax(True, tempBoard, player_color, level)
                if points > maxPoints:
                    maxPoints = points
                    mx = x; my = y
    return (mx, my)


def MinMax(minOrmax, board, player, level):
    if level == 0 or checkFullBoard(board, player):
        return getFinalScore(board, player)
    choice = 0
    if minOrmax:
        for y in range(boardsize):
            for x in range(boardsize):
                if movePosition(board, x, y, player):
                    temp = copy.deepcopy(board)
                    tempBoard, turnedChips = playerMove(temp, x, y, player)
                    #calling recursive algorithm as min
                    newVal = MinMax(False, tempBoard, player, level - 1)
                    #choosing max value
                    choice = max(choice, newVal)
    else:
        for y in range(boardsize):
            for x in range(boardsize):
                if movePosition(board, x, y, player):
                    temp = copy.deepcopy(board)
                    tempBoard, turnedChips = playerMove(temp, x, y, player)
                    #calling recutrsive algorithm as min
                    newVal = MinMax(True, tempBoard, player, level - 1)

                    choice = min(choice, newVal)
    return choice





#game function
def othello(level, fichas, inicia):
    global board


    if (fichas == 0):
        ai_color = '| B'
        user_color = '| W'
    else:
        ai_color = '| W'
        user_color = '| B'

    currentTurn = '| B'
    player = inicia

    #initializing board
    createBoard()

    print("Player's chips: ", user_color)
    print("AI's chips: ", ai_color)
    while True:
        for p in range(2):
            printCurrentBoard()
            if checkFullBoard(board, currentTurn):
                userScore = str(getFinalScore(board, user_color))
                aiScore = str(getFinalScore(board, ai_color))
                print(user_color, " score: ", userScore)
                print(ai_color, " score: ", aiScore)
                if(userScore > aiScore):
                    print("You win!")
                elif(aiScore > userScore):
                    print("AI wins!")
                else:
                    print("Draw")
                return 0
            elif player == 0: # player 1 turn
                print( "It's your turn")
                while True:
                    currentTurn = user_color
                    x = input("Insert column (A, B, ...)    ").upper()
                    y = int(input("Insert row (1, 2, ...)       "))
                    # (x, y) = list(xy)
                    if(x == 'A'):
                        x = 0
                    elif(x == 'B'):
                        x = 1
                    elif(x == 'C'):
                        x = 2
                    elif(x == 'D'):
                        x = 3
                    elif(x == 'E'):
                        x = 4
                    elif(x == 'F'):
                        x = 5
                    elif(x == 'G'):
                        x = 6
                    elif(x == 'H'):
                        x = 7
                    if movePosition(board, x, y, user_color):
                        board, turnedChips = playerMove(board, x, y, user_color)
                        player = 1
                        printCurrentBoard()
                        break
                    else:
                        print("Choose another position")
            else:
                print("AI moves")
                currentTurn = ai_color
                x, y = aiTurn(board, ai_color)
                if(x != -1 and y != -1):
                    (board, turnedChips) = playerMove(board, x, y, ai_color)
                    player = 0





def printCurrentBoard():
    letters = ['  A', ' B', ' C', ' D', ' E', ' F', ' G', ' H']
    size = len(str(boardsize - 1))
    row = ''
    for x in range(boardsize):
        row +=' ' + letters[x] + ' '
    print(row)
    for y in range(boardsize):
        row = ''
        for x in range(boardsize):
            row += board[y][x]
            row += ' ' * size
        print(str(y), row , "|",str(y))
    row = ''
    for x in range(boardsize):
        row += ' ' + letters[x] + ' '
    print(row)

if __name__ == '__main__':
    print("Proyecto 4 Othello Adrian Biller A01018940")

    level = 4
    level = int(input("Select dificulty level: 1, 2, 3, 4"))
    if(level):
        print("Level", level, "selected")
        inicia = str(random.randint(0,1))
        fichas = int(input("Choose chip color 0 = White 1 = Black"))
        othello(level, fichas, inicia)
    else:
        print("Invalid option")
