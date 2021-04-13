
import pygame

from ayarlar import Ayarlar

from posizyon import Posizyon

import oyun_fonksiyonları as of

def run_game():
    """oyun için başlangıç ve ekran objesi yapma"""
    pygame.init()
    ab_ayarlar = Ayarlar()
    ekran = pygame.display.set_mode(
        (ab_ayarlar.ekran_genişliği, ab_ayarlar.ekran_yüksekliği))
    pygame.display.set_caption("12-3 Rocket Denemesi")

    # cisim yapma
    
    posizyon = Posizyon(ab_ayarlar, ekran)
       

    # oyun için döngüyü başlatma

    while True:

        of.check_events(posizyon)
        posizyon.güncelle()
        of.ekran_güncelle(ab_ayarlar, ekran, posizyon)
        
run_game()
