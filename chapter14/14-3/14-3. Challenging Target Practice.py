
import pygame
from ayarlar import Ayarlar
import fonksiyonlar
from pygame.sprite import Group
from gemi import Gemi
from buton import Buton
from istatistik import İstatistik
from hedef import Hedef

def çalıştır_oyun():
    # Oyun için başlangıç yapma ve ekran objesini oluşturma.
    pygame.init()

    ayarlar = Ayarlar()
    ekran = pygame.display.set_mode(
        (ayarlar.ekran_genişliği, ayarlar.ekran_uzunluğu))

    pygame.display.set_caption("14-2 Target Practice")

    # Buton ile ilgili bir obje oluşturalım
    oyuna_başla = Buton(ayarlar, ekran, "Oyna")

    # Hedef objemizi oluşturalım.
    hedef = Hedef(ayarlar, ekran, "HEDEF")

    # Oyun ile ilgileri bilgileri depolaması için istatistik objesi oluşturalım
    istatistik = İstatistik(ayarlar)

    # Gemi objesi oluşturalım.
    gemi = Gemi(ayarlar, ekran)

    # Mermileri depolayacağımız bir grup oluşturalım
    mermiler = Group()

    while True:
        fonksiyonlar.eventleri_kontrol(ayarlar, ekran, istatistik, oyuna_başla,
                                       gemi, mermiler)
        if istatistik.oyun_aktifliği:
            
            gemi.güncelle()
            fonksiyonlar.mermileri_güncelle(istatistik, gemi, mermiler, ekran)
            fonksiyonlar.hedef_güncelle(ayarlar, hedef, mermiler, istatistik, gemi)

        fonksiyonlar.ekranı_güncelle(ayarlar, ekran, gemi, mermiler, oyuna_başla,
                    istatistik, hedef)

çalıştır_oyun()
        

        
