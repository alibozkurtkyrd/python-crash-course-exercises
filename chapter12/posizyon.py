import pygame

class Posizyon():

    def __init__(self,ab_ayarlar,ekran):
        """Initialize the pozisyon and set it starting position."""
        self.ekran = ekran
        self.ab_ayarlar = ab_ayarlar

        # Load the ship image and get its rect.

        self.resim = pygame.image.load('images/ship.bmp')
        self.rect = self.resim.get_rect()
        self.ekran_rect = ekran.get_rect()

        # Start each new ship at the center of the screen.

        self.rect.centerx = self.ekran_rect.centerx
        self.rect.centery = self.ekran_rect.centery

        # Store a decimal value for the ship's center

        self.center_1 = float(self.rect.centerx)
        self.center_2 = float(self.rect.centery)

        # flag hareketi

        self.moving_right = False
        self.moving_left = False

        self.moving_up = False
        self.moving_down = False

    def güncelle(self):
        """flag hareketine göre cisminn pozisyonu günceller"""

        # cismin merkez değerini günceller
        if self.moving_right and self.rect.right < self.ekran_rect.right:
            self.center_1 += self.ab_ayarlar.cisim_hız_faktörü

        if self.moving_left and self.rect.left > 0:
            self.center_1 -= self.ab_ayarlar.cisim_hız_faktörü

        # rect objesini güncelle
        self.rect.centerx = self.center_1

        if self.moving_down and self.rect.bottom < self.ekran_rect.bottom:   # burada bottom yerine down demiştim - hata verdi            
            self.center_2 += self.ab_ayarlar.cisim_hız_faktörü
        if self.moving_up and  self.rect.top > 0:  # burada top yerine up yazmıştım-hata verdi
            self.center_2 -= self.ab_ayarlar.cisim_hız_faktörü


        # rect objesini güncelleme
        self.rect.centery = self.center_2
            
    def blitme(self):
        """Cismin mevcut konumunu çizme"""
        self.ekran.blit(self.resim, self.rect)
