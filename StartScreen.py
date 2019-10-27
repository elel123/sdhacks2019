import pygame
from GameScene import GameScene

class StartScreen(GameScreen):

	def __init__(self, gameDisplay, door1 =None, door2 =None):
		super().init("Start Screen", gameDisplay, door1, door2)

		self.roomImage = pygame.image.load('Images/start_screen.jpg')

		self.font = pygame.font.SysFont("comicsansms", 72)
		self.text = font.render("Play iCompost")


