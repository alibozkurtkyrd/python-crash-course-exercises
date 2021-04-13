import pygame

class Position():

    def __init__(self, screen):
        """Initialize the position and set its starting position."""
        self.screen = screen

        # Load the image and get it rect.

        self.image = pygame.image.load('images/nepal_depremi.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new image  at the center of the screen.

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery # not ekranın altına değilde ortasını seçmiş oldum

    def blitme(self):
        
        """Draw the image at its current location."""
        self.screen.blit(self.image, self.rect)
         
