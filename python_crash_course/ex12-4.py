import sys
import pygame

def run_game():
    """This program takes the key pressed and then prints it to the screen"""
    # Initialize game and create a screen object
    pygame.init()

    screen_width = 1200
    screen_height = 800
    bg_color = (0, 0, 0)
  
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Print Event Keys")

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 300)

    # Start the main loop for the game
    while True:
        screen.fill(bg_color)

        key_input = check_events()

        textsurface = myfont.render(key_input, False, (250,250,90))
        screen.blit(textsurface,(0,0))

        # Make the most recently drawn screen visible
        pygame.display.update()

def check_events():
    """Respond to keypresses and return the key as a string"""
 
    # This gets one event from the Q if it is empty then it will wait, this is what keeps the key on the screen until another one is pressed.
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYUP:
        key_name = pygame.key.name(event.key)
        print(key_name)
        return str(key_name)

run_game()