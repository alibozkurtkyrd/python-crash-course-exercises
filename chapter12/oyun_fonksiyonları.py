import sys

import pygame

def check_keydown_events(event, posizyon):
    """keypresses olaylarını kontrol eder"""

    if event.key == pygame.K_RIGHT:
        posizyon.moving_right = True

    elif event.key == pygame.K_LEFT:
        posizyon.moving_left = True

    elif event.key == pygame.K_UP:
        posizyon.moving_up = True

    elif event.key == pygame.K_DOWN:
        posizyon.moving_down = True 

def check_keyup_events(event, posizyon):
    """ key releases hareketlerini kontrol eder"""

    if event.key == pygame.K_RIGHT:
        posizyon.moving_right = False

    elif event.key == pygame.K_LEFT:
        posizyon.moving_left = False

    elif event.key == pygame.K_UP:
        posizyon.moving_up = False

    elif event.key == pygame.K_DOWN:
        posizyon.moving_down = False

def check_events(posizyon):
    """mouse ve keypresses olaylarını kontrol eder."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, posizyon)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, posizyon)

def ekran_güncelle(ab_ayarlar, ekran, posizyon):
    """ ekrandaki resmi güncelle.."""
    # her bir döngüde ekranı yeniden çizme
    ekran.fill(ab_ayarlar.bg_renk)
    posizyon.blitme()

    # ekranı görünür yapmak için son ekranı çizme
    pygame.display.flip()
    
