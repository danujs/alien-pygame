import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
	"""Overall Class to manage game assets and behavior."""

	def __init__(self):
		"""initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

		#set the background color
		# self.bg_color = (255, 233, 230)


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#watch for keyboard and mouse events.
			self._check_events()
			
	def _check_events(self):
		"""Respond to keypresses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					# Move the ship to the right
					self.ship.rect.x += 1

			#redraw the screen during each pass through the loop
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			# Make the most recently drawn screen visible.
			pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
