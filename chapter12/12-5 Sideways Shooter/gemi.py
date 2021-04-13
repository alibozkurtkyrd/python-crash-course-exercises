import pygame

class Gemi():

    def __init__(self, ui_ayarlar, ekran):
        """ Gemi için başlangıç ve geminin başlangıç posizyonunu ayarlayalım."""
        self.ekran = ekran
        self.ui_ayarlar = ui_ayarlar

        # Geminin resmin yükleme ve onun diktörtengelsel ölçülerini alma
        self.resim = pygame.image.load('images/shipyan.bmp')
        self.dörtgen = self.resim.get_rect()
        self.ekran_dörtgeni = ekran.get_rect()

        # her bir yeni gemi objemizi ekran solunun altına yerleştirelim
        self.dörtgen.centery = self.ekran_dörtgeni.centery
        self.dörtgen.left = self.ekran_dörtgeni.left

        # Geminin ondalık değerdeki merkezini depolayalım.
        self.merkez = float(self.dörtgen.centery)

        # bayrak hareketi
        self.yukarı = False
        self.aşağı = False

    def güncelle(self):
        """ Bayrak haraketleri temelinde geminin posizyonunu değerlendirelim"""

        # geminin merkez değerinin güncelleyelim
        if self.yukarı and self.dörtgen.top > 0:
            self.merkez -= self.ui_ayarlar.gemi_hızı
        if self.aşağı and self.dörtgen.bottom < self.ekran_dörtgeni.bottom:
            self.merkez += self.ui_ayarlar.gemi_hızı

        # self.merkez değerine göre geminin y doğrultusundaki değerini güncelleyelim
        self.dörtgen.centery = self.merkez

    def blitme(self):
        """Geminin mevcut konumu ile ekrana basalım"""
        self.ekran.blit(self.resim, self.dörtgen)
        

        

