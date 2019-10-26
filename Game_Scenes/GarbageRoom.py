import pygame

class GarbageRoom(GameScene):

	def __init__(self, door1 =None, door2 =None):
		super().__init__("Garbage Room", door1, door2)
		roomImage = pygame.image.load('Images/garbage_room.jpg')

	def drawScene(self, event):
