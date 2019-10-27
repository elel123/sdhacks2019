import pygame
from GameScene import GameScene

class GarbageRoom(GameScene):

	def __init__(self, gameDisplay, door1 =None, door2 =None):
		#invoke the super classes' constructor
		super().__init__("Garbage Room", gameDisplay, door1, door2)


		roomImage = pygame.image.load('Images/garbage_room.jpg')




		self.inventory = pygame.Rect(0, 500, 100,800)


	def drawScene(self, event):
		#Method to be called in an infinite loop
		if self.showScene:
			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,600)), (0,0))
			pygame.draw.rect(self.gameDisplay, [122,112,43], self.inventory)






