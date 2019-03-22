import pygame, sys

class Board():
    """
    This class to print game's board,
    checking the validity of the move nedded.
    """

    def __init__(self, board, fboard, size):
        "Intialization for size and board"
        self.__board = board
        self.__size = size
        self.__fboard = fboard
        self.__zero = [self.__size-1]*2

    def printBoard(self, obj):
        "printing the board"
        startX = 50*(self.__size)+self.__size
        startY = 50*(self.__size)+self.__size
        startX = (400-startX)//2
        startY = (400-startY)//2

        for i in range(self.__size):
            count = 1
            for j in self.__board[i]:
                obj.checkQuit() #check if the user want to close the window immediately
                if j != 0:
                    obj.drawRect(startX+(50)*count+(1*(count-1)), startY+51*(i+1)+10, 50, 50, (217, 39, 0), str(j))
                else:
                    obj.drawRect(startX+(50)*count+(1*(count-1)), startY+51*(i+1)+10, 50, 50, (43, 0, 0), "-")
                pygame.display.update()
                count+=1
    
    def getBoard(self):
        return self.__board

    def setBoard(self, board):
        self.__board = board

    def checkWinner(self):
        "Checking the end of the game"
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__fboard[i][j] != self.__board[i][j]:
                    return False
        return True


    def checkMove(self, move):
        "Check the validity of a move required"
        for i in range(self.__size):
            for j in range(self.__size):
                #spotting the target and check the validity of the move
                if self.__board[i][j] == move:
                    #check if the absloute value of 1 in one side and 0 in the other to avoid parallel moves.
                    if 1 in (abs(i-self.__zero[0]), abs(j-self.__zero[1])) and 0 in (abs(i-self.__zero[0]), abs(j-self.__zero[1])):
                        self.doAMove(i, j)
                    else: print("Invalid Move\n")
                    return

    def doAMove(self, ti, tj):
        "perform the move after checking its validity"
        self.__board[self.__zero[0]][self.__zero[1]], self.__board[ti][tj] = self.__board[ti][tj], self.__board[self.__zero[0]][self.__zero[1]]
        self.__zero[0], self.__zero[1] = ti, tj #update the zero's spot
    
    def makeMove(self, obj):
        moves = [-1, -1, -1, -1]
        key = obj.getKeyPressed()

        for i in range(self.__size):
            for j in range(self.__size):
                if self.__board[i][j] == 0:
                    if j != 0:
                        moves[0] = self.__board[i][j-1]
                    if j != self.__size-1:
                        moves[1] = self.__board[i][j+1]
                    if i != self.__size-1:
                         moves[3] = self.__board[i+1][j]
                    if i != 0:
                        moves[2] = self.__board[i-1][j]
        if key != 0:
            self.checkMove(moves[key-1])

        
