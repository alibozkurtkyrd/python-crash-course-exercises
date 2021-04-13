
import pygame

from settings import Settings

from position import Position

def run_game():
    """Initialize exercise and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen= pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Deneme")

    # Make a image.

    image = Position(screen)

    screen.fill(ai_settings.bg_color)
    image.blitme()  # position modülü burada işe yaramış oldu gösterirken
    pygame.display.flip()

run_game()
    
