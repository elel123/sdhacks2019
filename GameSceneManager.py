import pygame
from GameScene import GameScene
from GarbageRoom import GarbageRoom


class GameSceneManager():


	def __init__(self, gameDisplay):
		""" 
	    GameSceneManager Object
	    
	    Attributes
	    ----------
	        gameScenes : list of GameScenes
	            Contains all the game scenes that we'll use in the game
	    """
		#List that contains all the scenes
		self.gameScenes = [GarbageRoom(gameDisplay), None]

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


