import pygame

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

#This loop constantly runs to keep the game running
#  (until the player exits the window)
while gameIsRunning:

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameIsRunning = False

	sceneManager = GameSceneManager();
	sceneManager.manage()

	#Update the game
	clock.tick(60)
	pygame.display.flip()

#END OF THE WHILE-LOOP

#When the player decides to quit, end all threads
pygame.display.quit()
pygame.font.quit()
pygame.quit()
