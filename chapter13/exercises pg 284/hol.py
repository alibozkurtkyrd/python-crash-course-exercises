import pygame

class Hol():

    def __init__(self, ayarlar, ekran):
        """Hol için başlangıç ve onun başlangıç posizyonunu belirleme."""
        self.ekran = ekran
        self.ayarlar = ayarlar

        # Hol resmini yükleme ve onun ölçülerini alma.
        self.resim = pygame.image.load('images/hol3.bmp')
        self.rect = self.resim.get_rect()
        self.ekran_ölçü = ekran.get_rect()

        # ekranın alt köşesi merkezine cismi yerleştirelim
        self.rect.centerx = self.ekran_ölçü.centerx # Not: collide ifadesi rect ismini istiyor o yüzden self.ölçü ifadesini sildim
        self.rect.bottom = self.ekran_ölçü.bottom

        # geminin merkezini ondalık sayı olarak kaydedelim.
        self.merkez = float(self.rect.centerx)

        # bayrak kontrol hareketleri
        self.sağ_hareket = False
        self.sol_hareket = False

    def güncelle(self):
        """ bayrak hareketlrine bağlı olarak hol ün pozisyonunu kontrol eder"""
        # Geminin merkez değerini günceller ekranın değil
        if self.sağ_hareket and self.rect.right < self.ekran_ölçü.right:
            self.merkez += self.ayarlar.hol_hızı
        if self.sol_hareket and self.rect.left > 0:
            self.merkez -= self.ayarlar.hol_hızı

        # self.ölçü değerimizi güncelleyelim
        self.rect.centerx = self.merkez
        

    def blitme(self):
        """Holün mevcut pozisyonunu ekrana çizelim."""
        self.ekran.blit(self.resim, self.rect)
