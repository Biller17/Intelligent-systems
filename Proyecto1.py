import copy





class Node:
    def __init__(self, boardState, moveDone, father = None,isVisited = 0 , childNodes = []):
        self.boardState = boardState
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.childNodes = childNodes
        self.father = father

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
        self.createChilds(moves)


    def createChilds(self, possibleMoves):
        for i in range(len(possibleMoves)):
            self.childNodes.append(Node(self.getNewBoard(possibleMoves[i]), possibleMoves[i],self))

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



def breadthFirstSearch():


if __name__ == '__main__':
    edoFinal = [[1,2,3],[4,5,6],[7,8,0]]

    edoInicial = [[0,1,2],[3,4,5],[6,7,8]]
    print("Proyecto 1 8-Puzzle Adrian Biller A01018940")
    root = Node(edoInicial, "")
    # root.printBoardState()
    root.checkPossibleMoves()
