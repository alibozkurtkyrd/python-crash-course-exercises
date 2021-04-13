import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the fleet."""

    def __init__(self, ayarlar, screen):
        """Initialize the star and set its starting position."""
        super(Raindrop, self).__init__()
        self.screen = screen
        self.ayarlar = ayarlar

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop2.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop  near the top left of the screen
        self.rect.x = 0.5 * self.rect.width
        self.rect.y = 0.5 * self.rect.height

        # Store the raindrop's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the raindrop below."""
        self.y += self.ayarlar.raindrop_speed_factor
        self.rect.y = self.y
        #buraya check_edges fonksiyonunu kontrol çalıştıracak bir şey gerekebilir
    def check_edges(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= (screen_rect.bottom):
            return True
    
    
