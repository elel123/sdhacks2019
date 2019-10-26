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

	def __init__(self, name, trashType, pickedUp, xPos, yPos):
		self.name = name
		self.trashType = trashType
		self.pickedUp = pickedUp
		self.xPos = xPos
		self.yPos = yPos
		self.selected = False

	def move(self, deltaX, deltaY):
		self.xPos = xPos + deltaX
		self.yPos = yPos + deltaY

	def changeTrash(self, name, trashType):
		self.name = name
		self.trashType = trashType

	def pickUp(self):
		self.pickedUp = pickedUp

	def getType(self):
		return self.trashType 

	def select(self):
		self.selected = True
	
	def deselect(self):
		self.selected = False

