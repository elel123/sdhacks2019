import pygame

class GameSceneManager():
	""" 
    GameSceneManager Object
    
    Attributes
    ----------
        gameScenes : list of GameScenes
            Contains all the game scenes that we'll use in the game
    """

	def __init__(self):
		#List that contains all the scenes
		gameScenes = [StartScene()]

		#turn on the start screen
		gameScenes[0].setSceneState()



	"""manage() controls the game scene

	Attributes
	----------
		event : the pygame event
			what we use to keep track of mouse clicks, mouse drags, etc

	"""
	def manage(self, event):
		#This method will be called in the game loop, so anything here will be constantly updated


