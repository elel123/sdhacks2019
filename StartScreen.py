import pygame
from GameScene import GameScene

class StartScreen(GameScene):

	def __init__(self, gameDisplay, door1 =None, door2 =None):
		super().__init__("Start Screen", gameDisplay, door1, door2)

		self.roomImage = pygame.image.load('Images/start_screen.jpg')

		self.font = pygame.font.SysFont("comicsansms", 72)
		self.text = self.font.render("Play iCompost", True, (0,0,0))

	def drawScene(self, event):
		#Method to be called in an infinite loop
		if self.showScene:

			self.gameDisplay.blit(pygame.transform.scale(self.roomImage, (800,600)), (0,00))
			self.gameDisplay.blit(self.text, (200, 0))

		
