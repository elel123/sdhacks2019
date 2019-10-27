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

		#Position of the trash on the screen
		self.xPos = xPos
		self.yPos = yPos

		#Used for dragging
		self.xOldMousePos = 0
		self.yOldMousePos = 0

		self.pickedUp = False
		self.selected = False
		self.trashImage = pygame.image.load('Images/'+trashImage)
		self.screen = gameDisplay
		self.canMove = False
		self.show = True


	def move(self, deltaX, deltaY):
		self.xPos = self.xPos + deltaX
		self.yPos = self.yPos + deltaY

	def changeTrash(self, name, trashType):
		self.name = name
		self.trashType = trashType

	def getType(self):
		return self.trashType 

	def select(self):
		self.selected = True
	
	def deselect(self):
		self.selected = False

	def getPos(self):
		return (self.xPos, self.yPos)

	def contains(self, mouseX, mouseY):
		imageWidth = self.trashImage.get_width()
		imageHeight = self.trashImage.get_height()
		mouse_pos = pygame.mouse.get_pos()
		if ( mouse_pos[0] < self.xPos + imageWidth and 
			 mouse_pos[1] < self.yPos +imageHeight and 
			 mouse_pos[0] > self.xPos and mouse_pos[1] > self.yPos):
			return True
		return False

	def hide(self):
		self.show = False

	def setMove(self, moveStatus):
		self.canMove = moveStatus


	def drawTrash(self, event):

		if self.show:
			self.screen.blit(pygame.transform.scale(self.trashImage, ((int)(self.trashImage.get_width()/20), (int)(self.trashImage.get_height()/20))), (self.xPos, self.yPos))
		
		if self.canMove:
			self.dragTrash(event)


	def dragTrash(self, event):
		mouse_pos = pygame.mouse.get_pos()

		mouse_x = mouse_pos[0] 
		mouse_y = mouse_pos[1]

		if ( self.contains(mouse_pos[0], mouse_pos[1]) and 
			 event.type == pygame.MOUSEBUTTONDOWN and not(self.selected)):
			self.selected = True
			self.xOldMousePos = mouse_x
			self.yOldMousePos = mouse_y

		elif event.type == pygame.MOUSEBUTTONUP:
			self.selected = False

		if self.selected:
			self.move(mouse_x - self.xOldMousePos, mouse_y - self.yOldMousePos)
			self.xOldMousePos = mouse_x
			self.yOldMousePos = mouse_y