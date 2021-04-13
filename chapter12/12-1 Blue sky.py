
import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("sanırım pencere adı") #bu açılan oyun penceresinin adı 

    bg_color = (0, 0, 230)


    screen.fill(bg_color)
    pygame.display.flip()

run_game()
