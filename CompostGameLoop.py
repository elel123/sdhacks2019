import pygame
from GameSceneManager import GameSceneManager
from Trash import Trash

#Initializes some elements of pygame
pygame.init()
#Sets up the use of fonts (text objects)
pygame.font.init()

#The screen size
screen_width = 800
screen_height = 600

gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Compost")
clock = pygame.time.Clock()

#Set up conditions for the infinite game loop
gameIsRunning = True


#Load the images
bananaImg = pygame.image.load('Images/banana.png')

#This loop constantly runs to keep the game running     
#  (until the player exits the window)
while gameIsRunning:

	sceneManager = GameSceneManager(gameDisplay);

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameIsRunning = False

		sceneManager.manage(event)

	
	

	#TEST (ADD A RECT)
	rect = pygame.Rect(0, 0, 800, 600)
	
	#pygame.draw.rect(gameDisplay, [255, 255, 255], rect)
	#gameDisplay.blit(pygame.transform.scale(bananaImg, (800, 600)), (0, 0))

	# def __init__(self, name, trashType, pickedUp, xPos, yPos, trashImage):
	# 	self.name = name
	# 	self.trashType = trashType
	# 	self.pickedUp = pickedUp
	# 	self.xPos = xPos
	# 	self.yPos = yPos
	# 	self.selected = False
	# 	self.trashImage = pygame.image.load('Images/' + trashImage)
	initTrashList = []

	initTrashList.append(Trash("Banana Peel", "Compost", False, xPos, yPos, 'Images/banana.png'))
	initTrashList.append(Trash('Soda can', 'Recycle', False, xPos, yPos, 'Images/can.png'))


	#Update the game
	clock.tick(60)
	pygame.display.flip()

#END OF THE WHILE-LOOP

#When the player decides to quit, end all threads
pygame.display.quit()
pygame.font.quit()
pygame.quit()
