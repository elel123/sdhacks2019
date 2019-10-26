import pygame

class GarbageRoom(GameScene):

	def __init__(self, door1 =None, door2 =None, gameDisplay=None):
		super().__init__("Garbage Room", door1, door2, gameDisplay)
		roomImage = pygame.image.load('Images/garbage_room.jpg')
		self.inventory = pygame.Rect(0, 500, 100,800)

	def drawScene(self, event):
		pygame.draw.rect(self.gameDisplay, [122,112,43], self.inventory)
		if self.showScene:
			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,600)), (0,0))
