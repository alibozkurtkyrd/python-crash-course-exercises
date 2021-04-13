import pygame.font

class Buton():

    def __init__(self, ayarlar, ekran, msj):
        """Buton özelliklere giriş yapalım."""
        self.ekran = ekran
        self.ekran_ölçü = ekran.get_rect()

        # buttonun boyut ve diğer özelliklerini ayarlayalım.
        self.genişlik, self.uzunluk = 225, 75
        self.buton_rengi = (255,0,0)
        self.yazı_rengi = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)

        # Diktdörtgensel button objesini merkeze alalım.
        self.dörtgen = pygame.Rect(0, 0, self.genişlik, self.uzunluk)
        self.dörtgen.center = self.ekran_ölçü.center

        # Button mesajı
        self.hazır_msj(msj)

    def hazır_msj(self, msj):
        """Mesajı yukarıda oluşturduğumuz dörtgen merkezine yazalım."""
        self.mesaj_resmi = self.font.render(msj, True, self.yazı_rengi,
                                            self.buton_rengi)
        self.mesaj_resim_ölçüleri = self.mesaj_resmi.get_rect()
        self.mesaj_resim_ölçüleri.center = self.dörtgen.center

    def buton_çiz(self):
        # Butonu ekranı çizelim ve mesajı yazdıralım.
        self.ekran.fill(self.buton_rengi, self.dörtgen) # burada draw.rect fonksiyonunu kullansak ne olurdu acaba
        self.ekran.blit(self.mesaj_resmi, self.mesaj_resim_ölçüleri) #blit methoudunu gemi.py klasöründe de kullandık
