import pygame

class Gemi():

    def __init__(self, ayarlar, ekran):
        """ Gemi için initialize yapalım ve geminin başlangıç pozisyonunu ayarlayalım."""
        self.ekran = ekran
        self.ayarlar = ayarlar

        # Gemi resmini yükle ve onun dikdörtgensel ölçülerini alalım.
        self.resim = pygame.image.load('images/shipyan.bmp')
        self.dörtgen = self.resim.get_rect()
        self.ekran_ölçü = ekran.get_rect()

        # Gemi objemiz ekranın sol altına yerleştirelim
        self.dörtgen.centery = self.ekran_ölçü.centery
        self.dörtgen.left = self.ekran_ölçü.left

        # Geminin merkez değerlerini ondalık birimde depolayılım.
        self.merkez = float(self.dörtgen.centery)

        # bayrak oluşturalım
        self.yukarı = False
        self.aşağı = False

    def merkez_gemi(self):
        """Gemi objemiz başlangıç durumu olan ekranın sol ortasına getirir."""
        self.merkez = self.ekran_ölçü.centery

    def güncelle(self):
        """ Bayrak hareketleri temelinde geminin posizyonunu değerlendirelim."""

        # Geminin merkez değerini güncelleyelim.
        if self.yukarı and self.dörtgen.top > 0:
            self.merkez -= self.ayarlar.gemi_hızı

        if self.aşağı and self.dörtgen.bottom < self.ekran_ölçü.bottom:
            self.merkez += self.ayarlar.gemi_hızı

        # self.merkze değerini güncelleyelim.
        self.dörtgen.centery = self.merkez

    def blitme(self):
        """ Geminin mevcut konumunu ekrana basalım."""
        self.ekran.blit(self.resim, self.dörtgen)
