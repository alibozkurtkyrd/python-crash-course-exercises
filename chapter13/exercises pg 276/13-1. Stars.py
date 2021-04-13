

import pygame

from pygame.sprite import Group

from star import Star

import functions

from settings import Settings

def run_game():
    
    #Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Stars")

    # Make a group of stars.
    stars = Group()
    
    # Create the fleet of stars.

    functions.create_fleet(settings, screen, stars)

    # Start the main loop for the game.

    while True:

        functions.check_events()
        functions.update_screen(settings, screen, stars)

run_game()
