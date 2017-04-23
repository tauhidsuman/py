import pygame
import os

class Ship():
	def __init__(self, screen):
		"Initialize ship and set starting pos"
		self.screen = screen

		#Load ship image and get rect
		self.image = pygame.image.load(os.path.join('res', 'ship.bmp'))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start ship at bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"Draw ship at current location"
		self.screen.blit(self.image, self.rect)