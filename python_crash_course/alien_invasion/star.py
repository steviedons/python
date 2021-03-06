from random import randint
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the star field"""

    def __init__(self, ai_settings, screen):
        """Initialize the star and set its starting position randomly"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        image_path = '/home/steve/python/python_crash_course/alien_invasion/images/shining2_small.png'
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Start each star at a random position on the screen 
        # the -25 is to pull the stars away from the screen edge
        self.rect.x = randint(0, ai_settings.screen_width-25)
        self.rect.y = randint(0, ai_settings.screen_height-25)

        # Store the stars exact postion
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star in its current position"""
        self.screen.blit(self.image, self.rect)
