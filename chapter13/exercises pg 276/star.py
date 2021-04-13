import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, settings, screen):
        """Initialize the star and set its starting position."""
        super(Star, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = 0.5 * self.rect.width
        self.rect.y = 0.5 * self.rect.height # I want to make a little difference by multiplying 0.5
        
       # Store the star's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)
