





class Node:
    def __init__(self, boardState, moveDone,isVisited = 0 , childNodes = []):
        self.boardState = boardState
        self.moveDone = moveDone
        self.isVisited = isVisited
        self.childNodes = childNodes

    def printBoardState(self):
        for i in range(len(self.boardState)):
            print(self.boardState[i])

    def checkPossibleMoves(self):
        for i in range(len(self.boardState)):
            for j in range(len(self.boardState[i])):
                if(self.boardState[i][j] == 0):
                    posY = i
                    posX = j
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

        self.createChilds(moves)


    def createChilds(self, possibleMoves):
        for i in range(len(possibleMoves)):
            self.getNewBoard(possibleMoves[i])

    def getNewBoard(self,move):
        if(move == "U"):
            
        if(move == "D"):

        if(move == "R"):

        if(move == "L"):








if __name__ == '__main__':
    edoFinal = [[1,2,3],[4,5,6],[7,8,0]]

    edoInicial = [[0,1,2],[3,4,5],[6,7,8]]
    print("Proyecto 1 8-Puzzle Adrian Biller A01018940")
    root = Node(edoInicial, "")
    root.printBoardState()
    root.checkPossibleMoves()
