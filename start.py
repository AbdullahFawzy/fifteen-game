import pygame, sys


class Start:
    """
    This class is used to display the start page of the game
    """

    def __init__(self, width, height):
        "Constructor to intialize the window"
        self.gameDisplay = None
        self.display_width = width
        self.displayHeight = height
        self.clock = pygame.time.Clock()
        self.orange = (211, 91, 0)
        self.bright_red = (217, 39, 0)
        self.bright_orange = (234, 91, 0)

    def createWindow(self):
        "This method is used to create window and set caption"
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.displayHeight))
        pygame.display.set_caption("Fifteen Game")

    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, (255, 255    , 255))
        return self.textSurface, self.textSurface.get_rect()
    
    def messsage_display(self, text, x, y):
        "This method is to display text in spacified X, Y"
        self.largeText = pygame.font.SysFont('comicsansms', 50)
        self.TextSurf, self.TextRect = self.text_objects(text, self.largeText)
        self.TextRect.center = ((x),(y))
        self.gameDisplay.blit(self.TextSurf, self.TextRect)

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        "Create a button by and change the color when hover over it"
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x+w > self.mouse[0] > x and y+h > self.mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))

            if self.click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(self.gameDisplay, ic, (x,y,w,h))

        self.smallText = pygame.font.SysFont("comicsansms", 35)
        self.textSurf, self.textRect = self.text_objects(msg, self.smallText)
        self.textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(self.textSurf, self.textRect)
            

    def game_loop(self):
        "This method is to display all contents"
        self.gameExit = False

        self.createWindow()
        
        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.gameDisplay.fill(self.orange)
            self.messsage_display("FIFTEEN GAME", 250, 150)            
            
            #Create Start And Exit Button 
            self.button("Start", 100, 300, 75, 50, self.bright_red, self.orange)
            self.button("Exit", 334, 300, 75, 50, self.bright_red, self.orange)

            pygame.display.update()
            self.clock.tick(60)

    def getInput(self):
        "This method is taken to handle the users input"


if __name__ == "__main__":
    pygame.init()

    startObj = Start(500, 500)
    startObj.game_loop()
    pygame.quit()