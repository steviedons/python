import unittest
import pygame
from bullet import Bullet
from alien_settings import Settings
from ship import Ship

class TestBullet(unittest.TestCase):

    def test_bullet_y(self):
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        ship = Ship(ai_settings, screen)        
        new_bullet = Bullet(ai_settings, screen, ship)
