import pygame
from GameScene import GameScene

class StartScreen(GameScreen):

	def __init__(self, gameDisplay, door1 =None, door2 =None):
		super().init("Start Screen", gameDisplay, door1, door2)
		