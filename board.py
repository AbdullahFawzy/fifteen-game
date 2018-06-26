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

    def printBoard(self):
        "printing the board"
        for i in range(self.__size):
            for j in self.__board[i]:
                if j == 0: print(" _", end = ' ')
                else:
                    print("%2d" % j, end = ' ')
            print()

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
