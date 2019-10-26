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
        xPos : double
			The x-position of the trash sprite
		yPos : double
			The y-position of the trash sprite
    """

	def __init__(self, name, trashType, pickedUp, xPos, yPos):
		self.trashType = trashType
		self.pickedUp = pickedUp
		self.xPos = xPos
		self.yPos = yPos

	def move(deltaX, deltaY):
		self.xPos = xPos + deltaX
		self.yPos = yPos + deltaY

