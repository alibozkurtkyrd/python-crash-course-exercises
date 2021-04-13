
import pygame

from pygame.sprite import Group

from ayarlar import Ayarlar

import fonksiyonlar

from raindrop import Raindrop

def run_game():

    # Initialize game and create a screen object.
    pygame.init()
    ayarlar = Ayarlar()
    screen = pygame.display.set_mode(
        (ayarlar.screen_width, ayarlar.screen_height))
    pygame.display.set_caption("Raindrops")

    # Make a group of raindrops.
    raindrops = Group()

    #Create the fleet of raindrops.

    fonksiyonlar.create_fleet(ayarlar, screen, raindrops)

    # Start the main loop for the game.

    while True:
        fonksiyonlar.check_events()
        fonksiyonlar.update_raindrops(ayarlar, raindrops, screen)
        fonksiyonlar.update_screen(ayarlar, screen, raindrops)
        
run_game()
