import pygame, sys

class Start(object):
    """
    This class is used to display the start page of the game
    """

    def __init__(self, width, height):
        "Constructor to intialize the window"
        self.gameDisplay = None
        self.display_width = width
        self.displayHeight = height
        self.clock = pygame.time.Clock()
        self.gameExit = False
        self.grid = True
        self.gridSize = -1

        self.orange = (211, 91, 0)
        self.bright_red = (217, 39, 0)
        self.bright_orange = (234, 91, 0)
        self.white = (255, 255, 255)
        self.brown = (43, 0, 0)
        self.start = False

    def createWindow(self):
        "This method is used to create window and set caption"
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.displayHeight))
        pygame.display.set_caption("Fifteen Game")

    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.white)
        return self.textSurface, self.textSurface.get_rect()
    
    def messsage_display(self, text, x, y):
        "This method is to display text in spacified X, Y"
        self.largeText = pygame.font.SysFont('comicsansms', 50)
        self.TextSurf, self.TextRect = self.text_objects(text, self.largeText)
        self.TextRect.center = ((x),(y))
        self.gameDisplay.blit(self.TextSurf, self.TextRect)

    def button(self, msg, x, y, w, h, ic = (217, 39, 0), ac = (234, 91, 0), action=None):
        "Create a button by and change the color when hover over it"
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x+w > self.mouse[0] > x and y+h > self.mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))

            if self.click[0] == 1 and action == "start":
                self.start = True
                self.gameExit = True
            elif self.click[0] == 1 and action == "exit":
                pygame.quit()
                quit()
            elif self.click[0] == 1 and action >= 3 and action < 9:
                for i in range(3, 9):
                    if i == action:
                        self.grid = False
                        self.gridSize = action
        else:
            pygame.draw.rect(self.gameDisplay, ic, (x,y,w,h))   

        self.smallText = pygame.font.SysFont("comicsansms", 35)
        self.textSurf, self.textRect = self.text_objects(msg, self.smallText)
        self.textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(self.textSurf, self.textRect)
            

    def start_loop(self):
        "This method is to display all contents"
        self.createWindow()
        
        while not self.gameExit:
            self.checkQuit()
            self.createGameDisplay()
            self.messsage_display("FIFTEEN GAME", 250, 150)            
            
            #Create Start And Exit Button 
            self.button("Start", 100, 300, 75, 50, self.bright_red, self.orange, "start")
            self.button("Exit", 334, 300, 75, 50, self.bright_red, self.orange, "exit")
 
            pygame.display.update()
            self.clock.tick(60)

    def chooseGridSize(self):
        "This method is to choose the grid size"

        while self.grid:
            self.checkQuit()
            
            self.createGameDisplay()
            self.messsage_display("CHOOSE GRID SIZE", 250, 150)

            #Size buttons
            self.button("3X3", 125, 250, 60, 50, self.bright_red, self.orange, 3)
            self.button("4X4", 225, 250, 60, 50, self.bright_red, self.orange, 4)
            self.button("5X5", 325, 250, 60, 50, self.bright_red, self.orange, 5)

            self.button("6X6", 125, 320, 60, 50, self.bright_red, self.orange, 6)
            self.button("7X7", 225, 320, 60, 50, self.bright_red, self.orange, 7)
            self.button("8X8", 325, 320, 60, 50, self.bright_red, self.orange, 8)
                    
            pygame.display.update()
            self.clock.tick(60)

    def getGridSize(self):
        "This method is to return the grid size choosen"
        return self.gridSize

    def getStart(self):
        return self.start
        
    def getGameDisplay(self):
        return self.gameDisplay()

    def checkQuit(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
    def createGameDisplay(self):
        self.gameDisplay.fill(self.bright_orange)

    def createCanvas(self, x, y, w, h):
        pygame.draw.rect(self.gameDisplay, self.brown,(x, y, w, h))

    def drawRect(self, x, y, w, h, color, txt):
        pygame.draw.rect(self.gameDisplay, color, pygame.Rect(x, y, w, h))
        smallText = pygame.font.SysFont('comicsansms', 30)
        textSurf, textRect = self.text_objects(txt, smallText)
        textRect.center = (x+(w/2), y+(h/2))
        self.gameDisplay.blit(textSurf, textRect)
 
    def getKeyPressed(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return 1
                if event.key == pygame.K_RIGHT:
                    return 2
                if event.key == pygame.K_UP:
                    return 3
                if event.key == pygame.K_DOWN:
                    return 4
        return 0