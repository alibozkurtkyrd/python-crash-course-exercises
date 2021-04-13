import sys
import pygame
from top import Top


def down_tuşlarını_kontrol(event, hol):
    """Down tuşlarını kontrol eder"""
    if event.key == pygame.K_RIGHT:
        hol.sağ_hareket = True

    elif event.key == pygame.K_LEFT:
        hol.sol_hareket = True

    elif event.key == pygame.K_q:
        sys.exit()

def up_tuşlarını_kontrol(event, hol):
    """up tuşarını kontrol eder."""

    if event.key == pygame.K_RIGHT:
        hol.sağ_hareket = False

    elif event.key == pygame.K_LEFT:
        hol.sol_hareket = False

def eventleri_kontrol(ayarlar, hol):
    """Yukarıdaki up ve down fonksiyonlarını kontrol eder."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            down_tuşlarını_kontrol(event, hol)

        elif event.type == pygame.KEYUP:
            up_tuşlarını_kontrol(event, hol)

def ekran_güncelle(ayarlar, ekran, hol, toplar):
    """ Ekrandaki görüntüleri günceller ve yeni bir ekrana flip yapar."""
    # Her bir döngü boyunca ekranı yeniden çizme
    ekran.fill(ayarlar.ap_renk)

    hol.blitme()
    
    toplar.draw(ekran)
    # En son çizilen işlemi ekranda görünür yapar.
    pygame.display.flip()

def top_oluştur(ayarlar, ekran, toplar):
    """Top objesi oluşturur."""
    top = Top(ayarlar, ekran)
    toplar.add(top)

def topları_güncelle(ayarlar, ekran, holler, toplar):
    """"topların pozisyonunu günceller."""
    toplar.update()

    çarpışma_sonrası(ayarlar, ekran, holler, toplar)

    # Ekran sınırı altına inen topları silelim ve yeni bir top objsei oluşturalım
    ekran_ölçü = ekran.get_rect()
    for top in toplar.copy():
        if top.rect.top > ekran_ölçü.bottom:
            toplar.remove(top)
            
def çarpışma_sonrası(ayarlar, ekran, holler, toplar):
    """ Hol ile top çarpışması ile ilgili."""
    # Çarpışma sonrası top objesini siler
    çarpışma = pygame.sprite.groupcollide(holler, toplar, False, True)

    if len(toplar) == 0:
        # Yeni top objesi oluştur
        top_oluştur(ayarlar, ekran, toplar)
        
    
