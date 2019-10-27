import pygame
from GameScene import GameScene
from Bin import Bin

class GarbageRoom(GameScene):

	def __init__(self, gameDisplay, door1 =None, door2 =None):
		#invoke the super classes' constructor
		super().__init__("Garbage Room", gameDisplay, door1, door2)


		self.roomImage = pygame.image.load('Images/garbage_room.jpg')
		self.inventory = pygame.Rect(0, 0, 800, 50)

		#The trash bins
		self.compostBin = Bin('compost', 200, 350, self.gameDisplay)
		self.landfillBin = Bin('landfill', 350, 350, self.gameDisplay)
		self.recycleBin = Bin('recycle', 500, 350, self.gameDisplay)


	def drawScene(self, event):
		#Method to be called in an infinite loop
		if self.showScene:
			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,550)), (0,50))
			pygame.draw.rect(self.gameDisplay, [122,112,43], self.inventory)
			self.compostBin.drawBin()
			self.landfillBin.drawBin()
			self.recycleBin.drawBin()







