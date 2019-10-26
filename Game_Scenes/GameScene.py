import pygame

#This class will serve as the "interface" for all the game scenes
class GameScene():

	def __init__(self, sceneName):
		#Some instance variables to be inherited by other gameScenes
		self.showScene = False
		self.sceneItems = []
		self.sceneName = sceneName



	def setSceneState(self):
		showScene = not(showScene)

	def changeScene(self, newScene):
		newScene.setSceneState()
		self.setSceneState()

	def getScene(self):
		return sceneName

	def addToScene(self, item):
		sceneItem.append(item)
	