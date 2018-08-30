import copy





class Node:
    def __init__(self, boardState, moveDone, father = None,isVisited = 0 ):
        self.boardState = boardState
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.father = father
        self.childNodes = []

    def printBoardState(self):
        for i in range(len(self.boardState)):
            print(self.boardState[i])



    def getBlankPosition(self):
        for i in range(len(self.boardState)):
            for j in range(len(self.boardState[i])):
                if(self.boardState[i][j] == 0):
                    posY = i
                    posX = j
        return  posY, posX

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


    def createChildren(self):
        possibleMoves = self.checkPossibleMoves()
        print(possibleMoves)
        print("possible moves",len(possibleMoves))
        print(len(self.childNodes))
        for i in range(len(possibleMoves)):
            self.childNodes.append(Node(self.getNewBoard(possibleMoves[i]), possibleMoves[i],self))

        return self.childNodes


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



def breadthFirstSearch(initialBoard, finalBoard):
    #this will be the queue array to check the nodes
    #funciona con insert(0, item) y pop
    foundFinalBoard = False
    queue = []
    root = Node(initialBoard,"")
    queue.insert(0, root)
    numberOfActions = 0
    while(foundFinalBoard != True):
        print("number of Actions",numberOfActions)
        currentNode = queue.pop()
        print("board: ", numberOfActions)
        # currentNode.printBoardState()
        if(currentNode.boardState != finalBoard):
            children = currentNode.createChildren()
            for i in range(len(children)):
                currentNode.printBoardState()
                queue.insert(0, children[i])
        else:
            foundFinalBoard = True
            print("foundFinalBoard")

        numberOfActions+=1




def dephFirstSearch():
    pass
    #funciona con append y pop

if __name__ == '__main__':
    edoFinal = [[1,2,3],[4,5,6],[7,8,0]]

    edoInicial = [[0,1,2],[3,4,5],[6,7,8]]
    print("Proyecto 1 8-Puzzle Adrian Biller A01018940")
    # breadthFirstSearch(edoInicial, edoFinal)
    root = Node(edoInicial, "")
    children = root.createChildren()
    print("father")
    root.printBoardState()
    for i in range(len(children)):
        print("\nchild", i)
        print(children[i].moveDone)
        children[i].printBoardState()
    secondChildren = children[1].createChildren()

    print("\nfather")
    children[1].printBoardState()
    print("new children", len(secondChildren))
    for i in range(len(secondChildren)):
        print("\nchild2", i)
        secondChildren[i].printBoardState()
        print(secondChildren[i].moveDone)


    print("prueba\n")
    secondChildren[3].printBoardState()

    newnewChildren = secondChildren[3].createChildren()
    print("newnewChildren length", len(newnewChildren))
    for i in range(len(newnewChildren)):
        print("\nchild3 ", i)
        print(newnewChildren[i].moveDone)
        newnewChildren[i].printBoardState()
