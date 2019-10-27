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


		initTrashList = []

		initTrashList.append(Trash("Banana Peel", "Compost", False, 0, 50, 'banana.png'))
		initTrashList.append(Trash('Soda can', 'Recycle', False, 50, 50, 'can.png'))
		initTrashList.append(Trash('Beer bottle', 'Recycle', False, 100, 50, 'bottle.png'))
		initTrashList.append(Trash('Chip bag', 'Landfill', False, 150, 50, 'chip_bag.png'))
		initTrashList.append(Trash('Apple core', 'Compost', False, 200, 50, 'apple_core.png'))
		initTrashList.append(Trash('Balloon', 'Landfill', False, 250, 50, 'balloon.png'))
		initTrashList.append(Trash('Watermelon', 'Compost', False, 300, 50, 'watermelon.png'))


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


