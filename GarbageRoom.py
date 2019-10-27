import pygame
from GameScene import GameScene
from Bin import Bin
from Trash import Trash

class GarbageRoom(GameScene):

	def __init__(self, gameDisplay, trashInv, door1 =None, door2 =None):
		#invoke the super classes' constructor
		super().__init__("Garbage Room", gameDisplay, door1, door2)


		self.roomImage = pygame.image.load('Images/garbage_room.jpg')
		self.inventory = pygame.Rect(0, 0, 800, 80)
		self.sceneItems = trashInv


		#The trash bins
		self.compostBin = Bin('compost', 200, 350, self.gameDisplay)
		self.landfillBin = Bin('landfill', 400, 350, self.gameDisplay)
		self.recycleBin = Bin('recycle', 600, 350, self.gameDisplay)

		#Used to keep track of which trash item is currently allowed for dragging
		self.trashIndex = 0
		self.sceneItems[self.trashIndex].setMove(True)



	def drawScene(self, event):
		#Method to be called in an infinite loop
		if self.showScene:


			pygame.draw.rect(self.gameDisplay, [122,112,43], self.inventory)
			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,520)), (0,80))
			

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

			for i in self.sceneItems:

				i.drawTrash(event)

			#Increment through the list of trash we currently have to only
			#  allow for moving trash one at a time.
			if (self.trashIndex < len(self.sceneItems)):

				#Allow for the next trash to be dragged
				self.sceneItems[self.trashIndex].setMove(True)

				if self.sceneItems[self.trashIndex].getType() == "Compost" and \
				   self.compostBin.contains(self.sceneItems[self.trashIndex].getPos()[0], \
				                       self.sceneItems[self.trashIndex].getPos()[1] ):

					self.sceneItems[self.trashIndex].setMove(False)
					self.sceneItems[self.trashIndex].hide()
					self.trashIndex = self.trashIndex + 1

				elif self.sceneItems[self.trashIndex].getType() == "Landfill" and \
				   self.landfillBin.contains(self.sceneItems[self.trashIndex].getPos()[0], \
				                       self.sceneItems[self.trashIndex].getPos()[1] ):

					self.sceneItems[self.trashIndex].setMove(False)
					self.sceneItems[self.trashIndex].hide()
					self.trashIndex = self.trashIndex + 1

				elif self.sceneItems[self.trashIndex].getType() == "Recycle" and \
				   self.recycleBin.contains(self.sceneItems[self.trashIndex].getPos()[0], \
				                       self.sceneItems[self.trashIndex].getPos()[1] ):

					self.sceneItems[self.trashIndex].setMove(False)
					self.sceneItems[self.trashIndex].hide()
					self.trashIndex = self.trashIndex + 1







			self.compostBin.drawBin()
			self.landfillBin.drawBin()
			self.recycleBin.drawBin()


