import pygame

class Bin:

    def __init__(self, trashType, xPos, yPos, gameDisplay):
        self.trashType = trashType
        self.currentVolume = 0
        self.xPos = xPos
        self.yPos = yPos
        self.selected = False
        self.binImage = pygame.image.load('Images/' + trashType + '.png')
        self.binImageOpen = pygame.image.load('Images/open_' + trashType + '.png')
        self.gameDisplay = gameDisplay

    def acceptTrash(self, trash):
        if (self.trashType == trash.trashType):
            return True
        else:
            return False

    def getVolume(self):
        return self.currentVolume

    def move(self, deltaX, deltaY) :
        xPos+=deltaX
        yPos+=deltaY

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def contains(self, mouseX, mouseY):
        if mouseX < self.xPos + 200 and mouseX > self.xPos and \
           mouseY < self.yPos + 200 and mouseY > self.yPos:
           return True
        else:
            return False

    def drawBin(self):
        if self.selected:
            self.gameDisplay.blit(pygame.transform.scale(self.binImageOpen, (150, 250)), (self.xPos,self.yPos))
        else:
            self.gameDisplay.blit(pygame.transform.scale(self.binImage, (150, 250)), (self.xPos,self.yPos))


