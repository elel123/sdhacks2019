import pygame

class Door():

	def __init__(self, doorType, xPos, yPos, gameDisplay):
		self.xPos = xPos
		self.yPos = yPos
		self.doorType = doorType
		self.gameDisplay = gameDisplay

		self.doorCloseImg = pygame.image.load('Images/door_close')
		self.doorOpenImg = pygame.image.load('Images/door_open')

	def contains(self, mouseX, mouseY)
		if doorType == "door" and \
		   mouseX > self.xPos and mouseX < self.xPos + self.doorCloseImg.getWidth() and \
		   mouseY > self.yPos and mouseY < self.yPos + self.doorCloseImg.getHeight():

		   return True
		elif doorType == "sign" and \
			 mouseX > self.xPos and mouseX < self.xPos + self.doorCloseImg.getWidth() and \
		     mouseY > self.yPos and mouseY < self.yPos + self.doorCloseImg.getHeight()::

		else:
			return False

	def drawDoor(self, event):