import pygame
from pygame.sprite import Sprite

class Mermi(Sprite):
    """Gemiden ateşlenen mermileri kontrol eder."""

    def __init__(self, ayarlar, ekran, gemi):
        """Geminin mevcut pozisyonu temelli bir mermi objesi oluşturalım."""
        super(Mermi, self).__init__()
        self.ekran = ekran

        # (0,0) noktasınd bir mermi dörtgeni oluşturalım sonra bunu
        # doğru bir konuma yerleştirelim
        self.rect = pygame.Rect(0, 0, ayarlar.mermi_genişliği,   # self.dörtgen değişkenini self.rect ifadesi ile değiştiriyorum çünkü fonkisyonlar.py line 106 spritecollideany methodu rect objesi istiyor
                                   ayarlar.mermi_yüksekliği)
        self.rect.centery = gemi.dörtgen.centery
        self.rect.right = gemi.dörtgen.right

        # Mermini koordinatlarını ondalık sayı şeklinde depolayalım
        self.x = float(self.rect.x)
        self.renk = ayarlar.mermi_rengi
        self.hız = ayarlar.mermi_hızı

    
    def update(self):
        """ Mermiyi ekranın solundan sağına doğru hareket ettirir."""
        # Merminin ondalık değerini güncelleyelim.
        self.x += self.hız

        # Merminin koordinatalarını güncelleyelim.
        self.rect.x = self.x

    def mermi_çiz(self):
        """ Mermiyi ekrana basalım."""
        pygame.draw.rect(self.ekran, self.renk, self.rect)
