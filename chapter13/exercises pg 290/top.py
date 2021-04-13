from random import randint
import pygame
from pygame.sprite import Sprite
class Top(Sprite):
    
    """Top ile ilgili özellikleri barındırır."""

    def __init__(self, ayarlar, ekran):
        """Top için başlangıç ve topun başlangıç konumunu içerir"""
        super(Top, self).__init__()
        self.ekran = ekran
        self.ayarlar = ayarlar

        # Top resmimizi yükleyelim ve onun ölçülerini alalım
        self.image = pygame.image.load('images/ball3.bmp') # not: self.resim i self image şeklinde düzelmek zorundayım çünkü sprite da .toplar.draw(ekran) çalışmıyor
        self.rect = self.image.get_rect()       # NOT: aynı şekil self.ölçü de değişecek bir üst line daki aynı nedenden dolayı
        
        # Top un konumunu belirleyelim
        self.ekran_ölçü = ekran.get_rect()
        rastgele_y = randint((self.ekran_ölçü.top + self.rect.height),
                             (self.ekran_ölçü.bottom - (2.5 * self.rect.height))) # uç noktaları topun genişlik ve yüksekliğine göre ayarladım 
        rastgele_x = randint((self.ekran_ölçü.left + self.rect.width),
                             (self.ekran_ölçü.right - self.rect.width))
        self.rect.x = rastgele_x
        self.rect.y = rastgele_y

        # Top un tam konumunu kaydedelim
        self.y = float(self.rect.y)

    def blitme(self):
        """ Topun en son konumunu ekrana basalım."""
        self.ekran.blit(self.resim, self.ölçü)

    def update(self): # fonksiyon ismi önceden 'güncelle' ide ama toplar.update() ifadesi çalışmıyordu o yüzden böyle yaptım 
        """ Topu aşağıya doğru hareket ettirelim."""
        self.y += (self.ayarlar.top_hızı)

        self.rect.y = self.y


