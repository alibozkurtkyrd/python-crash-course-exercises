import sys

import pygame

from mermi import Mermi

def keydown_tuşları(event,ui_ayarlar, ekran, gemi, mermiler):
    """Tuşa basma olaylarını kontrol eder"""
    if event.key == pygame.K_UP:
        gemi.yukarı = True

    elif event.key == pygame.K_DOWN:
        gemi.aşağı = True

    elif event.key == pygame.K_SPACE:
        mermiyi_ateşle(ui_ayarlar, ekran, gemi, mermiler)        
                
def keyup_tuşları(event, gemi):
    """ Tuşa basmaMA olaylarını kontrol eder"""

    if event.key == pygame.K_UP:
        gemi.yukarı = False
        
    elif event.key == pygame.K_DOWN:
        gemi.aşağı = False


def eventleri_kontrol(ui_ayarlar, ekran, gemi, mermiler):
    """ Tuşlrı ve mouse eventlerini kontrol eder."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_tuşları(event, ui_ayarlar, ekran, gemi, mermiler)
        elif event.type == pygame.KEYUP:
            keyup_tuşları(event, gemi)

def ekranı_güncelle(ui_ayarlar, ekran, gemi, mermiler):
    """ekrandaki resimleri günceller ve yeni bir ekrana geçiş yapar."""
    # her bir yeni döngüde ekranı tekrar oluşturma
    ekran.fill(ui_ayarlar.bg_renk)

    # tüm mermileri yeniden çizelim
    for mermi in mermiler.sprites():
        mermi.mermi_çiz()

    gemi.blitme()

    # en son şekli ekrana basma
    pygame.display.flip()

def mermileri_güncelle(mermiler, gemi): #not gemi parametresini ben EKLEDİM game_functions.py(orjinalde) yok amaç ekran dışına çıkan mermiyi silmek
    """Mermilerin koordinatlarını güncelleme ve eski mermileri silme."""
    # Mermi koordinatını güncelleme
    #mermiler.güncelle() # It is failed said 'Group' object has no attribute 'güncelle'
    
    # Ekran görüntüsünden çıkan mermileri silme
    for mermi in mermiler.copy():
        mermi.güncelle() # NOT: line 55 teki kod çalışmadığı için buraya bunu yazdım
        if mermi.dörtgen.right > gemi.ekran_dörtgeni.right: # burası game_functions.py den FARKLI çünkü mermi sağa doğru giderken x değeri büyüyor orjianalde kücülüyordu
            mermiler.remove(mermi)
            
            
def mermiyi_ateşle(ui_ayarlar, ekran, gemi, mermiler):
    """ Eğer belirlediğimiz sınırı aşmıyorsa mermiyi ateşle"""
    # yeni bir mermi objsei oluşturalım ve bunu mermiler grubuna ekleyelim
    if len(mermiler) < ui_ayarlar.izinverilen_mermi:
        yeni_mermi = Mermi(ui_ayarlar, ekran, gemi)
        mermiler.add(yeni_mermi)
