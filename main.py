from start import Start
import pygame, sys
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
            self.keys = pygame.key.get_pressed()

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

    def createGameDisplay(self, obj):
        obj.createGameDisplay()
        pygame.display.update()


if __name__ == "__main__":
    plays = {} #storing the number of plays
    
    #connect the backend with frontend
    pygame.init()
    screen_width = 500
    screen_height = 500
    startObj = Start(screen_width, screen_height)
    
    while 1:
        startObj.start_loop()
        print("\nPlayer #{}:\n".format(len(plays)+1))

        while startObj.getStart(): #Catch ant input error from the user's size
            pygame.time.wait(200) #delay to avoid choosing the grip mistakenly
            startObj.chooseGridSize()
            
            try:
                print "size: ",
                size = startObj.getGridSize()
                print size
            except ValueError as VE:
                print("{}\n".format(VE))
            else:
                if size < 3 or size > 9:
                    print("\nThe size between (3, 9)\n")
                    continue
                break

        obj = Main(size)
        plays[obj] = obj.createGame() #creating new object with required size
        obj.createGameDisplay(startObj) #create new window with canvas

        #keep playing until the current board equals the final board
        while True:
            if plays[obj].checkWinner():
                plays[obj].printBoard(startObj)
                break
            plays[obj].printBoard(startObj)
            plays[obj].makeMove(startObj)
            
        startObj.messsage_display("Congrats!", 250, 400)
        pygame.display.update()
        print("\n~Congrats!\n")
        pygame.time.delay(2000)
        pygame.quit()
        quit()

   