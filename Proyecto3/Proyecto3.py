
#Proyecto 3 Adrian Biller A01018940

import copy
import random
import math
import time


#Node class for all nodes in the search tree
class Node:
    def __init__(self, board, queensAttacking):
        self.board = board
        self.queensAttacking = queensAttacking
        self.childNodes = []





#returns an array of all possible moves in current zero position
    def checkPossibleMoves(self):
        posY, posX = self.getBlankPosition()
        moves = []
        #check Up
        if(posY -1 >= 0):
            moves.append("U")
            #up is possible
        #check Down
        if(posY +1 <= len(self.boardState)-1):
            moves.append("D")
        #check Right
        if(posX +1 <= len(self.boardState[0])-1):
            moves.append("R")
        #check Left
        if(posX -1 >= 0):
            moves.append("L")
        # print(moves)
        # self.createChildren(moves)
        return moves

#creates and returns an array of all the possible moves sent to the child nodes including the new board position
    def createChildren(self):
        possibleMoves = self.checkPossibleMoves()
        # print(possibleMoves)
        # print("possible moves",len(possibleMoves))
        for i in range(len(possibleMoves)):
            self.childNodes.append(Node(self.getNewBoard(possibleMoves[i]), possibleMoves[i],self, 0))
        return self.childNodes

#reads the move specified and changes board accordingly
    def getNewBoard(self,move):
        posY, posX = self.getBlankPosition()
        newBoard = copy.deepcopy(self.boardState)
        if(move == "U"):
            newBoard[posY][posX] = newBoard[posY-1][posX]
            newBoard[posY-1][posX] = 0
        if(move == "D"):
            newBoard[posY][posX] = newBoard[posY+1][posX]
            newBoard[posY+1][posX] = 0
        if(move == "R"):
            newBoard[posY][posX] = newBoard[posY][posX+1]
            newBoard[posY][posX+1] = 0
        if(move == "L"):
            newBoard[posY][posX] = newBoard[posY][posX-1]
            newBoard[posY][posX-1] = 0

        # for i in range(len(newBoard)):
        #     print(newBoard[i])
        return newBoard




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


def getPossibleMoves(position, lateral, size):
    print(position)
    moves = []
    if(position[0] -1 >= 0):
        moves.append((position[0]-1, position[1]))
        #up is possible
    #check Down
    if(position[0] +1 <=size-1):
        moves.append((position[0]+1, position[1]))
    #check Right
    if(position[1] +1 <= size-1 and lateral):
        moves.append((position[0], position[1]+1))
    #check Left
    if(position[1] -1 >= 0 and lateral):
        moves.append((position[0], position[1]-1))
    # print(moves)
    # self.createChildren(moves)
    return moves



def hillClimbing(N, board, lateral, M):
    #this will be the queue array to check the nodes
    evaluation = 1
    printBoard(board)
    evaluationFunction(board)
    queenPositions = getQueens(board)

    print("moves with:", queenPositions[0] , "\n", getPossibleMoves(queenPositions[0], lateral, N))

    # root = Node(initialBoard,"", None, 0)
    # queue.insert(0, root)

    # while(evaluation != 0):
    #     currentNode = queue.pop(0)
    #     print("current node", currentNode.heuristic)
    #     #if current node does not have the answer then expand and create children with possible moves and add them to the queue
    #     if(currentNode.boardState != finalBoard):
    #         visitedNodes.append(currentNode)
    #         children = currentNode.createChildren()
    #         for i in range(len(children)):
    #             # print("child")
    #             # currentNode.printBoardState()
    #             # print("\n")
    #             if(checkIfVisited(children[i], visitedNodes) == 0):
    #                 children[i].checkH2(finalBoard)
    #                 queue.insert(0, children[i])
    #
    #         prioritizeNodes(queue)
    #     else:
    #         foundFinalBoard = True
    #
    #         print("Found Solution! ")
    #         return currentNode.returnSolutionMove([])
    #
    #     numberOfActions+=1





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
    print(busquedaHC(5, False, 5))
    # main()
