import pygame
from pygame.sprite import Sprite

class Mermi(Sprite):
    """Bu sınıf gemiden ateşlenen mermileri kontrolü yönetmek için kuruldu"""

    def __init__(self, ui_ayarlar, ekran, gemi):
        """Geminin mevcut pozisyonuna göre bir mermi objesi oluşturalım."""
        super(Mermi, self).__init__()
        #super().__init__(ui_ayarlar, ekran, gemi) # this is not worked python 3 syntax
        self.ekran = ekran

        # (0,0) noktasında bir mermi dörtgeni oluşturalım sonrada bunu doğru yerine koyalım
        self.dörtgen = pygame.Rect(0, 0, ui_ayarlar.mermi_genişliği,
                                   ui_ayarlar.mermi_yüksekliği)
        self.dörtgen.centery = gemi.dörtgen.centery
        self.dörtgen.right = gemi.dörtgen.right

        # Merminin koordinatlarını ondalık sayı şeklinde depolayalım
        self.x = float(self.dörtgen.x)
        self.renk = ui_ayarlar.mermi_rengi
        self.hız = ui_ayarlar.mermi_hızı

    def güncelle(self):
        """ Mermiyi ekranının solundan sağına doğru haraket ettirelim"""
        # Merminin ondalık değerini güncelleyelim
        self.x += self.hız   # bullet.py(orjinal)de '+' değil '-' oluyordu ama x yönü soldan sağa doğru artıyor o yüzden
        # Merminin koordinatını güncelleyelim
        self.dörtgen.x = self.x

    def mermi_çiz(self):
        """ Mermiyi çizelim yani ekranda görünür hale getirelim"""
        pygame.draw.rect(self.ekran, self.renk, self.dörtgen)
