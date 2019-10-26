import pygame

class GameSceneManager():

	def __init__(self):
		#List that contains all the scenes
		gameScenes = [StartScene()]

		#turn on the start screen
		gameScenes[0].setSceneState()


	def manage(self):
		#This method will be called in the game loop, so anything here will be constantly updated
		

