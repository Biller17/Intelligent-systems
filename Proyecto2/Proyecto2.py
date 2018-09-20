
#Proyecto 2 Adrian Biller A01018940

import copy
import random
import time


#Node class for all nodes in the search tree
class Node:
    def __init__(self, boardState, moveDone, father,isVisited):
        self.boardState = boardState
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.father = father
        self.childNodes = []
        self.heuristic = 0


    def printBoardState(self):
        for i in range(len(self.boardState)):
            print(self.boardState[i])


#gets matrix position of zero in the board
    def getBlankPosition(self):
        for i in range(len(self.boardState)):
            for j in range(len(self.boardState[i])):
                if(self.boardState[i][j] == 0):
                    posY = i
                    posX = j
        return  posY, posX

    def getValuePosition(self, value, finalBoard):
        for i in range(len(finalBoard)):
            for j in range(len(finalBoard)):
                if(value  == finalBoard[i][j]):
                    return i, j

    def checkH1(self, finalBoard):
        heuristic = 0
        for i in range(len(self.boardState)):
            for j in range(len(self.boardState[i])):
                if(self.boardState[i][j] != finalBoard[i][j]):
                    heuristic += 1
        self.heuristic = heuristic
        # return heuristic

    def checkH2(self, finalBoard):
        heuristic = 0
        for i in range(len(self.boardState)):
            for j in range(len(self.boardState[i])):
                x,y = self.getValuePosition(self.boardState[i][j], finalBoard)
                heuristic += (abs(i - x) + abs(j - y))
        self.heuristic = heuristic



        # print("checking heuristic 2")


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

#recursive function that returns all the moves done to reach the node with the solution
    def returnSolutionMove(self,moveset):
        # print(moveset)
        if(self.father == None):
            return moveset
        else:
            moveset.insert(0,self.moveDone)
            self.father.returnSolutionMove(moveset)
        return moveset




def checkIfVisited(node, nodeArray):
    for i in range(len(nodeArray)):
        if(node.boardState == nodeArray[i].boardState):
            return 1
    return 0



def prioritizeNodes(queue):
    quicksort(queue, 0, len(queue)-1)
    # for i in range(len(queue)):
    #     print("h:", queue[i].heuristic, end="")


def quicksort(array, left, right):
    if(left >= right):
        return 0
    pivot = array[ int((left + right) / 2)]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index -1)
    quicksort(array, index, right)


def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left].heuristic < pivot.heuristic ):
            left += 1
        while(array[right].heuristic > pivot.heuristic):
            right -= 1
        if(left <= right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    return left



#a* algorithm with heuristic of out of place numbers
def astarH1(initialBoard, finalBoard):
    #this will be the queue array to check the nodes
    queue = []
    visitedNodes = []
    foundFinalBoard = False
    root = Node(initialBoard,"", None, 0)
    queue.insert(0, root)
    numberOfActions = 0
    while(foundFinalBoard != True):
        currentNode = queue.pop(0)
        print("board: ", numberOfActions)
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(currentNode.boardState != finalBoard):
            visitedNodes.append(currentNode)
            children = currentNode.createChildren()
            for i in range(len(children)):
                # print("child")
                # currentNode.printBoardState()
                # print("\n")
                if(checkIfVisited(children[i], visitedNodes) == 0):
                    print(children[i].checkH1(finalBoard))
                    queue.insert(0, children[i])
            prioritizeNodes(queue)
        else:
            foundFinalBoard = True

            print("Found Solution! ")
            return currentNode.returnSolutionMove([])

        numberOfActions+=1



#a* algorithm with heuristic of mannhatan distances
def astarH2(initialBoard, finalBoard):
    #this will be the queue array to check the nodes
    queue = []
    visitedNodes = []
    foundFinalBoard = False
    root = Node(initialBoard,"", None, 0)
    queue.insert(0, root)
    numberOfActions = 0
    while(foundFinalBoard != True):
        currentNode = queue.pop(0)
        print("current node", currentNode.heuristic)
        print("board: ", numberOfActions)
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(currentNode.boardState != finalBoard):
            visitedNodes.append(currentNode)
            children = currentNode.createChildren()
            for i in range(len(children)):
                # print("child")
                # currentNode.printBoardState()
                # print("\n")
                if(checkIfVisited(children[i], visitedNodes) == 0):
                    children[i].checkH2(finalBoard)
                    queue.insert(0, children[i])

            prioritizeNodes(queue)
        else:
            foundFinalBoard = True

            print("Found Solution! ")
            return currentNode.returnSolutionMove([])

        numberOfActions+=1







def busquedaAstar(edoInicial, edoFinal, heuristica):
    start_time = time.time()
    solution = []
    if(heuristica == '0'):
         #numero de cuadros fuera de su lugar
        solution = astarH1(edoInicial, edoFinal)
        print("El programa tomó %s segundos " % (time.time() - start_time))
    else:
        #numero de distancias mannhatan
        solution = astarH2(edoInicial, edoFinal)
        print("El programa tomó %s segundos " % (time.time() - start_time))
    return solution

if __name__ == '__main__':
    edoFinal = [[1,2,3],[4,5,6],[7,8,0]]

    edoInicial = [[0,1,2],[4,5,3],[7,8,6]]
    print("Proyecto 1 8-Puzzle Adrian Biller A01018940")

    option = input("0 Para usar heuristica de numero de bloques fuera de lugar \n1 para usar heuristica de distancias mannhatan\n")

    # breadthFirstSearch(edoInicial, edoFinal)
    # dephFirstSearch(edoInicial,edoFinal)
    print(busquedaAstar(edoInicial, edoFinal, option))
    # main()
