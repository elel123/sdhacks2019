import pygame

class Bin:

    def __init__(self, trashType, currentVolume, xPos, yPos):
        self.trashType = trashType
        self.currentVolume = currentVolume
        self.xPos = xPos
        self.yPos = yPos
        self.selected = False

    def acceptTrash(self, trash):
        if (self.trashType == trash.trashType):
            return True
        else:
            return False

    def getVolume(self):
        return self.currentVolume

    def move(self, deltaX, deltaY) :
        self.xPos+=deltaX
        self.yPos+=deltaY

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False
