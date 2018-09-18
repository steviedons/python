import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting point"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('/home/steve/python/python_crash_course/alien_invasion/images/space_ship64.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Start each new ship at the bottom center of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the position of the ship based on the moving_right flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        