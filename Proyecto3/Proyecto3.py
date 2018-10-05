
#Proyecto 3 Adrian Biller A01018940

import copy
import random
import math
import time



def getQueens(board):
    queens = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 1):
                queens.append((i,j))
    return queens


def evaluationFunction(board):
    heuristic = 0
    queenPositions = getQueens(board)
    for i in range(len(queenPositions)):
        currentQueen = queenPositions.pop(0)
        for j in range(len(queenPositions)):
            #checking if there are attacks in x axis
            if(currentQueen[0] == queenPositions[j][0]):
                heuristic += 1
            #checking if there are attacks in y axis
            if(currentQueen[1] == queenPositions[j][1]):
                heuristic += 1
            #checking if there are diagonal
            if(abs(currentQueen[0] - queenPositions[j][0]) == abs(currentQueen[1] - queenPositions[j][1])):
                heuristic += 1
    return heuristic



def printBoard(board):
    for i in range(len(board)):
        print(board[i])


def getPossibleMoves(position, size):
    # print(position)
    moves = []
    if(position[0] -1 >= 0):
        moves.append((position[0]-1, position[1]))
        #up is possible
    #check Down
    if(position[0] +1 <=size-1):
        moves.append((position[0]+1, position[1]))
    return moves



def getNewBoard(oldPos, newPos, board):
    print("old board")
    printBoard(board)
    temp = copy.deepcopy(board)
    temp[oldPos[0]][oldPos[1]] = 0
    temp[newPos[0]][newPos[1]] = 1
    print("new board")
    printBoard(temp)
    return temp

def checkIfVisited(visitedList, board):
    for i in range(len(visitedList)):
        if(visitedList[i] == board):
            print("ya fue visitado")
            return True
    return False



def hillClimbing(N, board, lateral, M):
    visited = []
    evaluation = evaluationFunction(board)
    queenPositions = getQueens(board)
    bestNeighbor = board
    numOfResets = 0
    reset = True
    while(evaluation != 0):
        print("*********************************************************** EVALUATION", evaluation, "******************************************")
        for i in range(len(queenPositions)):
            currentNeighbor = queenPositions.pop(0)
            possibleMoves = getPossibleMoves(currentNeighbor, N)
            for j in range(len(possibleMoves)):
                tempBoard = getNewBoard(currentNeighbor, possibleMoves[j], board)
                if(checkIfVisited(visited,tempBoard)):
                    break
                neighborEvaluation = evaluationFunction(tempBoard)
                if(neighborEvaluation <= evaluation and lateral):
                    bestNeighbor = tempBoard
                    evaluation = neighborEvaluation
                    reset = False
                elif(neighborEvaluation < evaluation):
                    bestNeighbor = tempBoard
                    evaluation = neighborEvaluation
                    reset = False

                visited.append(tempBoard)

            if(reset and numOfResets <= M):
                visited = []
                board = generateBoard(N)
                reset = True
                numOfResets += 1

            board = bestNeighbor
            queenPositions = getQueens(board)
    return board



def generateBoard(size):
    board = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        board[math.floor(random.uniform(0, size))][i] = 1
    return board

def busquedaHC(N, lateral, M):
    start_time = time.time()
    board = generateBoard(N)
    solution = hillClimbing(N, board, lateral, M)
    # print("El programa tomó %s segundos " % (time.time() - start_time))
    return solution

if __name__ == '__main__':
    print("Proyecto 3 N-Reinas Adrian Biller A01018940")

    # breadthFirstSearch(edoInicial, edoFinal)
    # dephFirstSearch(edoInicial,edoFinal)
    print(busquedaHC(8, True, 5))
    # main()
