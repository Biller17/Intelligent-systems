
#Proyecto 1 Adrian Biller A01018940

import copy
import random



#Node class for all nodes in the search tree
class Node:
    def __init__(self, boardState, moveDone, father,isVisited):
        self.boardState = boardState
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.father = father
        self.childNodes = []


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



#breadth first search algorithm implementing queue

def breadthFirstSearch(initialBoard, finalBoard):
    #this will be the queue array to check the nodes
    queue = []
    foundFinalBoard = False
    root = Node(initialBoard,"", None, 0)
    queue.insert(0, root)
    numberOfActions = 0
    while(foundFinalBoard != True):
        currentNode = queue.pop()
        print("board: ", numberOfActions)
        #if current node does not have the answer then expand and create children with possible moves and add them to the queue
        if(currentNode.boardState != finalBoard):
            children = currentNode.createChildren()
            for i in range(len(children)):
                # print("child")
                # currentNode.printBoardState()
                # print("\n")
                queue.insert(0, children[i])
        else:
            foundFinalBoard = True

            print("Found Solution! ")
            print(currentNode.returnSolutionMove([]))

        numberOfActions+=1





def dephFirstSearch(initialBoard, finalBoard):
    #this will be the queue array to check the nodes
    #funciona con insert(0, item) y pop
    foundFinalBoard = False
    stack = []
    root = Node(initialBoard,"", None, 0)
    stack.insert(0, root)
    numberOfActions = 0
    while(foundFinalBoard != True):
        # print("number of Actions",numberOfActions)
        currentNode = stack.pop()
        print("board: ", numberOfActions)
        # currentNode.printBoardState()
        #if current node does not have the answer then expand and create children with possible moves and add them to the stack
        if(currentNode.boardState != finalBoard):
            children = currentNode.createChildren()
            random.shuffle(children)
            for i in range(len(children)):
                # print("child")
                # currentNode.printBoardState()
                # print("\n")
                stack.append(children[i])
        else:
            foundFinalBoard = True

            print("Found Solution! ")
            print(currentNode.returnSolutionMove([]))

        numberOfActions+=1




def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
     if(algoritmo == 0):
         #breadthFirstSearch
         breadthFirstSearch(edoInicial, edoFinal)
     else:
        dephFirstSearch(edoInicial, edoFinal)

if __name__ == '__main__':
    edoFinal = [[1,2,3],[4,5,6],[7,8,0]]

    edoInicial = [[0,1,2],[4,5,3],[7,8,6]]
    print("Proyecto 1 8-Puzzle Adrian Biller A01018940")
    # breadthFirstSearch(edoInicial, edoFinal)
    # dephFirstSearch(edoInicial,edoFinal)
    option = input("0 Para Breadth first search / 1 para Deph first search\n")
    busquedaNoInformada(edoInicial, edoFinal, option)
