import pygame

#This class manages all our trash
class Trash():
	""" 
    Trash object
    
    Attributes
    ----------
        name : string
            Name of the trash
        trashType : string
            Either compost, landfill, or recyclable 
        pickedUp : boolean
			Indicates whether trash has been picked up or not
		selected : boolean
			Boolean to help with highlighting trash when hovered over
        xPos : double
			The x-position of the trash sprite
		yPos : double
			The y-position of the trash sprite
    """

	def __init__(self, name, trashType, xPos, yPos, trashImage, gameDisplay):
		self.name = name
		self.trashType = trashType
		self.xPos = xPos
		self.pickedUp = False
		self.yPos = yPos
		self.selected = False
		self.trashImage = pygame.image.load('Images/'+trashImage)
		self.screen = gameDisplay


	def move(self, deltaX, deltaY):
		self.xPos = xPos + deltaX
		self.yPos = yPos + deltaY

	def changeTrash(self, name, trashType):
		self.name = name
		self.trashType = trashType

	def getType(self):
		return self.trashType 

	def select(self):
		self.selected = True
	
	def deselect(self):
		self.selected = False

	def contains(self, mouseX, mouseY):
		imageWidth = self.trashImage.get_width()
		imageHeight = self.trashImage.get_height()
		mouse_pos = pygame.mouse.get_pos()
		if ( mouse_pos[0] < self.xPos + imageWidth and 
			 mouse_pos[1] < self.yPos +imageHeight and 
			 mouse_pos[0] > self.xPos and mouse_pos[1] > self.yPos):
			return True
		return False

	def drawTrash(self, event):
		self.screen.blit(pygame.transform.scale(self.trashImage, (75, 75)), (self.xPos, self.yPos))
		self.dragTrash(event)

	def dragTrash(self, event):
		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0] 
		mouse_y = mouse_pos[1]
		if ( self.contains(mouse_pos[0], mouse_pos[1]) and 
			 event.type == pygame.MOUSEBUTTONDOWN):
			self.selected = True
		elif event.type == pygame.MOUSEBUTTONUP:
			self.selected = False

		if self.selected:
			self.xPos = mouse_x
			self.yPos = mouse_y