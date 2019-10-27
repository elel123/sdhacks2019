import pygame

class Door():

	def __init__(self, doorType, xPos, yPos, gameDisplay):
		self.xPos = xPos
		self.yPos = yPos
		self.doorType = doorType
		self.gameDisplay = gameDisplay

		self.doorCloseImg = pygame.image.load('Images/door_close')
		self.doorOpenImg = pygame.image.load('Images/door_open')

		self.signImg = pygame.Rect(xPos, yPos, 250, 150)

	def contains(self, mouseX, mouseY)
		if doorType == "door" and \
		   mouseX > self.xPos and mouseX < self.xPos + self.doorCloseImg.getWidth() and \
		   mouseY > self.yPos and mouseY < self.yPos + self.doorCloseImg.getHeight():

		   return True
		   
		elif doorType == "sign" and \
			 mouseX > self.xPos and mouseX < self.xPos + self.doorCloseImg.getWidth() and \
		     mouseY > self.yPos and mouseY < self.yPos + self.doorCloseImg.getHeight():

		    return True

		else:
			return False

	def doorClicked(self, event):
		mousePos = pygame.mouse.get_pos()
		mouseX = mousePos[0]
		mouseY = mousePos[1]
		if event.type == pygame.MOUSEBUTTONDOWN and self.contains(mouseX, mouseY):
			return True
		else
			return False


	def drawDoor(self, event):
		mousePos = pygame.mouse.get_pos()
		mouseX = mousePos[0]
		mouseY = mousePos[1]
		if doorType == "door":
			if self.contains(mouseX, mouseY):
				self.gameDisplay.blit(pygame.transform.scale(self.doorOpenImg, ((int)(self.trashImage.get_width()/5), (int)(self.trashImage.get_height()/5))), (self.xPos, self.yPos))
			else:
				self.gameDisplay.blit(pygame.transform.scale(self.doorCloseImg, ((int)(self.trashImage.get_width()/5), (int)(self.trashImage.get_height()/5))), (self.xPos, self.yPos))

		if doorType == "sign":
			if self.contains(mouseX, mouseY):
				#Yellow highlight
				buttonColor = [250, 255, 120]
			else:
				#Brown color for button
				buttonColor = [158, 134, 112]
			pygame.draw.rect(self.gameDisplay, buttonColor, self.signImg)