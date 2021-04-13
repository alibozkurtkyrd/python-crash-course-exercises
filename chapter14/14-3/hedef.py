import pygame.font

class Hedef():
    """ Gemi tarafından vurulması hedeflenen diktdörtgensel cisim."""

    def __init__(self, ayarlar, ekran, msj):
        """ Hedef özelliklerine giriş yapalım."""
        self.ekran = ekran
        self.ekran_ölçü = ekran.get_rect()
        self.ayarlar = ayarlar

        # Hedefin boyut ve diğer özelliklerini içerir
        self.genişlik, self.uzunluk = 120, 200
        self.hedef_rengi = (139, 136, 120)
        self.yazı_rengi = (227, 207, 87)
        self.font = pygame.font.SysFont(None, 52)

        # Hedef objesini ekran sağına alalım
        self.rect = pygame.Rect(0, 0, self.genişlik, self.uzunluk) # self.dörtgen değikenini self.rect şeklinde değiştireceğim çünkü fonksiyonlar.py line 106 daki spritecollideany methodu rect ifadesi istiyor
        self.rect.right = (self.ekran_ölçü.right - 6) # -6 yı kendim koydum aksi halde götü görünüm oluyor
        self.y = float(self.rect.y)

        # Hedef mesajı
        self.msj_hazır(msj)

    def msj_hazır(self, msj):
        """Mesajı dörgensel bölgenin merkezine yazalım."""
        self.msj_resim = self.font.render(msj, True, self.yazı_rengi,
                                          self.hedef_rengi)
        self.msj_resim_ölçü = self.msj_resim.get_rect()
        self.msj_resim_ölçü.center = self.rect.center
        self.resim_y = float(self.msj_resim_ölçü.y)

    def sınır_kontrol(self):
        """Hedef objemiz ekranın uç noktalarına ulaşırsa doğru sonucunu döneleim."""
        if self.rect.top < 0:
            return True

        elif self.rect.bottom > self.ekran_ölçü.bottom:
            return True

    def şekil_çiz(self):
        # Hedef dörtgenimizi çizelim ve mesajı yazdıralım.
        self.ekran.fill(self.hedef_rengi, self.rect)
        self.ekran.blit(self.msj_resim, self.msj_resim_ölçü)

    def güncelle(self):
        """Hedef cimini aşağı yukarı hareket ettirelim."""
        self.y += (self.ayarlar.hedef_hızı *
                   self.ayarlar.hedef_yön)

        self.resim_y += (self.ayarlar.hedef_hızı *
                   self.ayarlar.hedef_yön)      # bunu yazmayınca hedef yazısı hareket etmediği için böyle yazdım
        
        
        self.rect.y = self.y
        self.msj_resim_ölçü.y = self.resim_y
