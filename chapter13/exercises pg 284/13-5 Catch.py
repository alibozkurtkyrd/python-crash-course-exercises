

import pygame
from ayarlar import Ayarlar
from hol import Hol
import fonksiyonlar
from top import Top
from pygame.sprite import Group


def oyun_başlat():
    #Oyuna başlangıç ve ekran objesi oluşturma.
    
    pygame.init()
    ayarlar = Ayarlar()
    ekran = pygame.display.set_mode(
        (ayarlar.ekran_genişliği, ayarlar.ekran_yüksekliği))
    pygame.display.set_caption("Catch")
    
    # Hol objesi oluşturalım
    hol = Hol(ayarlar, ekran)

    # Groupcollide ifadesi parametre olarak iterable bir değer istediği için holler
    # şeklinde bir liste oluşturdum normalde holler = Group() da yapabliridim ancak güncelle
    # self.resim gibi türkçe değişkenleri update image gibi değerler dönüştürmem gerekirdi
    # geçici bir çözüm olmuş oldu
    holler = []
    holler.append(hol) 
    
    toplar = Group()

    # Top objesini oluşturalım
    fonksiyonlar.top_oluştur(ayarlar, ekran, toplar)
    
    # oyun için döngüyü başlatalım

    while True:
        
        fonksiyonlar.eventleri_kontrol(ayarlar, hol)
        hol.güncelle()
        fonksiyonlar.topları_güncelle(ayarlar, ekran, holler, toplar)
        fonksiyonlar.ekran_güncelle(ayarlar, ekran, hol, toplar)
        
oyun_başlat()
