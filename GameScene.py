import pygame

#This class will serve as the "interface" for all the game scenes
class GameScene():

	def __init__(self, sceneName, gameDisplay, door1 =None, door2 =None):
		#Some instance variables to be inherited by other gameScenes
		self.showScene = False
		self.sceneItems = []
		self.sceneName = sceneName

		#The doors to be used
		self.door1 = door1
		self.door2 = door2

		self.gameDisplay = gameDisplay


	def setSceneState(self):
		self.showScene = not(self.showScene)




	def changeScene(self, newScene):
		"""Changes the scene to a new scene

    	Attributes
    	----------
    		newScene : GameScene
    			the new scene to be drawn
    	"""
		newScene.setSceneState()
		self.setSceneState()

	def getScene(self):
		return sceneName


	def addToScene(self, item):
		"""Adds an item (trash) to the game scene

    	Attributes
    	----------
    		trash : Trash
    			the trash to be added
    	"""
		sceneItem.append(item)



	def drawScene(self, event):
		"""Will be called by the game manager and will constantly run
		Will use the instance boolean showScene to control whether the 
		scene will draw or not. 

		Abstract, to be implemented

		Attributes
		----------
			event : pygame event
				This is the event passed into Game
		"""

	