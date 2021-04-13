import pygame
from ayarlar import Ayarlar
from gemi import Gemi
import oyun_fonksiyonları as of
from pygame.sprite import Group


def çalıştır_oyun():
    # Oyun için başlangıç yapalım ve ekran objesini oluşturalım.
    pygame.init()
    ui_ayarlar = Ayarlar()
    ekran = pygame.display.set_mode(
        (ui_ayarlar.ekran_genişliği, ui_ayarlar.ekran_uzunluğu))
    pygame.display.set_caption("Uzaylı İstilası")

    # Gemi objesi oluşturalım
    gemi = Gemi(ui_ayarlar, ekran)

    # Mermileri depolayacağımız bir grup oluşturalım
    mermiler = Group()

    while True:

        of.eventleri_kontrol(ui_ayarlar, ekran, gemi, mermiler)
        gemi.güncelle()
        of.mermileri_güncelle(mermiler, gemi)
        of.ekranı_güncelle(ui_ayarlar, ekran, gemi, mermiler)

çalıştır_oyun()
