import pygame
from GameScene import GameScene
from Bin import Bin
from Trash import Trash

class GarbageRoom(GameScene):

	def __init__(self, gameDisplay, trashInv, door1 =None, door2 =None):
		#invoke the super classes' constructor
		super().__init__("Garbage Room", gameDisplay, door1, door2)


		self.roomImage = pygame.image.load('Images/garbage_room.jpg')
		self.inventory = pygame.Rect(0, 0, 800, 50)
		self.sceneItems = trashInv

		#The trash bins
		self.compostBin = Bin('compost', 200, 350, self.gameDisplay)
		self.landfillBin = Bin('landfill', 400, 350, self.gameDisplay)
		self.recycleBin = Bin('recycle', 600, 350, self.gameDisplay)
		self.trash = Trash('banana','compost', False, 30, 30, 'banana.png', self.gameDisplay)


	def drawScene(self, event):
		#Method to be called in an infinite loop
		if self.showScene:
			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,550)), (0,50))
			self.trash.drawTrash()
			pygame.draw.rect(self.gameDisplay, [122,112,43], self.inventory)

			#Check if the mouse has hovered over the bins
			mousePos = pygame.mouse.get_pos()

			if self.compostBin.contains(mousePos[0], mousePos[1]):
				self.compostBin.select()
			else:
				self.compostBin.deselect()

			if self.landfillBin.contains(mousePos[0], mousePos[1]):
				self.landfillBin.select()
			else:
				self.landfillBin.deselect()			

			if self.recycleBin.contains(mousePos[0], mousePos[1]):
				self.recycleBin.select()
			else:
				self.recycleBin.deselect()
			
			# A list in

			for i in len(self.sceneItems):
				self.sceneItems[i].drawTrash()

			self.compostBin.drawBin()
			self.landfillBin.drawBin()
			self.recycleBin.drawBin()


