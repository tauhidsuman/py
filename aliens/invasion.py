import pygame
from ship import Ship

def run_game():
	"Initialize game and create a screen object."
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('Alien Invasion')

	#Set background color
	bg_color = (255,0,0)

	#Make a ship
	ship = Ship(screen)

	#Start the main loop
	while True:
		#Watch for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit(1)

		#Redraw the screen with bg_color
		screen.fill(bg_color)
		ship.blitme()

		#Display most recently drawn screen
		pygame.display.flip()

run_game()