import pygame
from GameScene import GameScene
from GarbageRoom import GarbageRoom
from Trash import Trash


class GameSceneManager():


	def __init__(self, gameDisplay):
		""" 
	    GameSceneManager Object
	    
	    Attributes
	    ----------
	        gameScenes : list of GameScenes
	            Contains all the game scenes that we'll use in the game
	    """


		self.gameDisplay = gameDisplay

		initTrashList = []

		initTrashList.append(Trash("Banana Peel", "Compost", 0, 60, 'banana.png', self.gameDisplay))
		initTrashList.append(Trash('Soda can', 'Recycle', 100, 60, 'can2.png', self.gameDisplay))
		initTrashList.append(Trash('Beer bottle', 'Recycle', 200, 60, 'bottle.png', self.gameDisplay))
		initTrashList.append(Trash('Chip bag', 'Landfill', 300, 60, 'chip_bag.png', self.gameDisplay))
		initTrashList.append(Trash('Apple core', 'Compost', 400, 60, 'apple_core.png', self.gameDisplay))
		initTrashList.append(Trash('Balloon', 'Landfill', 450, 60, 'balloon2.png', self.gameDisplay))
		initTrashList.append(Trash('Watermelon', 'Compost', 550, 60, 'watermelon.png', self.gameDisplay))


		#List that contains all the scenes
		self.gameScenes = [GarbageRoom(gameDisplay, initTrashList), None]

		#turn on the start screen
		self.gameScenes[0].setSceneState()




	def manage(self, event):
		"""manage() controls the game scene

		Attributes
		----------
			event : the pygame event
				what we use to keep track of mouse clicks, mouse drags, etc

		"""
		#This method will be called in the game loop, so anything here will be constantly updated
		self.gameScenes[0].drawScene(event)


