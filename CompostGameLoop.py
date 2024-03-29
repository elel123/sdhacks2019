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

sceneManager = GameSceneManager(gameDisplay);

#Load the images
bananaImg = pygame.image.load('Images/banana.png')
appleImg = pygame.image.load('Images/apple_core.png')
balloonImg = pygame.image.load('Images/banana.png')
bottleImg = pygame.image.load('Images/bottle.png')
canImg = pygame.image.load('Images/can.png')
chipBagImg = pygame.image.load('Images/chip_bag.png')
watermelonImg = pygame.image.load('Images/watermelon.png')


#This loop constantly runs to keep the game running     
#  (until the player exits the window)
while gameIsRunning:

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameIsRunning = False

		sceneManager.manage(event)

	
	

	#TEST (ADD A RECT)
	rect = pygame.Rect(0, 0, 800, 600)
	
	#pygame.draw.rect(gameDisplay, [255, 255, 255], rect)
	#gameDisplay.blit(pygame.transform.scale(bananaImg, (800, 600)), (0, 0))

	#Update the game
	clock.tick(60)
	pygame.display.flip()

#END OF THE WHILE-LOOP

#When the player decides to quit, end all threads
pygame.display.quit()
pygame.font.quit()
pygame.quit()
