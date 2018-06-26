import board
import math

class Main:
    """
    This class is to create the initial board list
    , get board's size from the user
    , and run the program
    """

    def __init__(self, size):
        "Constructor to initialize board's size and create the board"
        if size >= 3 or size <= 9:
            self.__size = size
            self.__board = [[] for i in range(self.__size)]
            self.__fboard = [[] for i in range(self.__size)]
            self.__zero = [self.__size-1, self.__size-1]
            self.createBoard()
            self.createFinalBoard()

    def getSize(self):
        return self.__size

    def getBoard(self):
        return self.__board

    def createBoard(self):
        "Method to Intialize the very first board"
        num = self.__size * self.__size
        for i in range(self.__size):
            for j in range(self.__size):
                num -= 1
                if self.__size % 2 == 0:
                    if num == 2:
                        self.__board[i] += [1]
                        continue
                    elif num == 1:
                        self.__board[i] += [2]
                        continue
                self.__board[i] += [num]

    def createFinalBoard(self):
        "Methos to create final board"
        num = 1
        for i in range(self.__size):
            for j in range(self.__size):
                self.__fboard[i] += [num]
                num += 1
        self.__fboard[self.__size-1][self.__size-1] = 0

    def createGame(self):
        "Method to create object if there are more than one attempt"
        return board.Board(self.__board, self.__fboard, self.__size)


if __name__ == "__main__":
    plays = {} #storing the number of plays

    while 1:
        print("\nPlayer #{}:\n".format(len(plays)+1))

        while True: #Catch ant input error from the user's size
            try:
                size = int(input("Size: "))
            except ValueError as VE:
                print("{}\n".format(VE))
            else:
                if size < 3 or size > 9:
                    print("\nThe size between (3, 9)\n")
                    continue
                break
        obj = Main(size)
        plays[obj] = obj.createGame() #creating new object with required size

        #keep playing until the current board equals the final board
        while not plays[obj].checkWinner():
            plays[obj].printBoard()

            while True: #Catch an input error from the user's move
                try:
                    move = int(input("\nMove: "))
                except ValueError as VE:
                    print("{}\n".format(VE))
                else:
                    if move < 1 or move >= int(math.pow(size, 2)):
                        print("The move between ({}, {})".format(1, int(math.pow(size, 2)-1)))
                        continue
                    break
            plays[obj].checkMove(move)

        print("\n~Congrats!\n")

        while True: #Catch an input error and force the user to enter only one character
            repeat = input("Play Again(Y/N): ")
            if len(repeat) != 1:
                print("Enter only one cahracter\n")
                continue
            elif 'y' not in repeat.lower() and 'n' not in repeat.lower():
                print("Please enter (Y/N)\n")
                continue
            break
        #exit from the game
        if 'n' in repeat.lower():
            print("\nSee You Soon!\n")
            break
