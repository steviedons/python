import pygame
from pygame.sprite import Group
from alien_settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    #Make a group to store the bullets in
    bullets = Group()
    # Make an alien
    aliens = Group()
    stars = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    gf.create_star_field(ai_settings, screen, stars)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stars)

run_game()
