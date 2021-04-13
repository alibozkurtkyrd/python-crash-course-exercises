import sys
import pygame
from mermi import Mermi
from hedef import Hedef
from time import sleep

def keydown_tuşları(event, ayarlar, ekran, gemi, mermiler):
    """Tuşa basma olaylarını kontrol eder."""
    if event.key == pygame.K_UP:
        gemi.yukarı = True

    elif event.key == pygame.K_DOWN:
        gemi.aşağı = True

    elif event.key == pygame.K_SPACE:
        mermiyi_ateşle(ayarlar, ekran, gemi, mermiler)

def keyup_tuşları(event, gemi):
    """ Tuşa BASMAMA olaylarını kontrol eder"""

    if event.key == pygame.K_UP:
        gemi.yukarı = False

    elif event.key == pygame.K_DOWN:
        gemi.aşağı = False

def eventleri_kontrol(ayarlar, ekran, istatistik, oyuna_başla,
                                       gemi, mermiler):
    """Tuşları ve mouse eventlerini kontrol eder."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keydown_tuşları(event, ayarlar, ekran, gemi, mermiler)

        elif event.type == pygame.KEYUP:
            keyup_tuşları(event, gemi)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            oyna_butonu_kontrol(istatistik, oyuna_başla, mouse_x, mouse_y)

def oyna_butonu_kontrol(istatistik, oyuna_başla, mouse_x, mouse_y):
    """Oyna butonuna her basışta oyun tekrar başlar"""

    if oyuna_başla.dörtgen.collidepoint(mouse_x, mouse_y):
        # Oyun istatistiğini sıfırlayalım
        istatistik.istatistik_sıfırla()
        istatistik.oyun_aktifliği = True

def ekranı_güncelle(ayarlar, ekran, gemi, mermiler, oyuna_başla,
                    istatistik, hedef):
    """Ekrandaki görüntüleri günceller ve yeni bir ekrana geçiş yapar."""
    # Her bir yeni döngüde ekranı tekrar oluşturur
    ekran.fill(ayarlar.ap_renk)

    # Tüm mermileri yeniden çizelim
    for mermi in mermiler.sprites():
        mermi.mermi_çiz()

    gemi.blitme()

    # Oyunun aktif olmadığı durum için Oyna butonunu ekrana çizelim
    if not istatistik.oyun_aktifliği:
        oyuna_başla.buton_çiz()

    # Hedef objemizi ekrana çizelim.
    hedef.şekil_çiz()
    
    # En son ki görseli ekrana baasalım
    pygame.display.flip()

def mermileri_güncelle(istatistik, gemi, mermiler, ekran):
   """ Mermilerin koordinatlarını günceller ve ihtiyaç dışı mermileri siler."""
   mermiler.update()
   
   # Ekran alanı dışına çıkan mermileri silme
   ekran_ölçü = ekran.get_rect()
   for mermi in mermiler.copy():
       if mermi.rect.right > ekran_ölçü.right:
           çarpışma(istatistik, gemi, mermiler)
           mermiler.remove(mermi)

def mermiyi_ateşle(ayarlar, ekran, gemi, mermiler):
    """ Eğer mermi limitini aşmıyor ise mermi ateşle."""
    # Yeni bir mermi objesi oluşturalım ve bunu mermiler grubuna ekleyelim
    if len(mermiler) < ayarlar.izinverilen_mermi:
        yeni_mermi = Mermi(ayarlar, ekran, gemi)
        mermiler.add(yeni_mermi)

def hedef_sınırları_kontrol(ayarlar, hedef):
    """Hedef objemizin ekran sınırlarındaki durumunu kontrol eder."""
    if hedef.sınır_kontrol():
        hedef_yön_değiştir(ayarlar)
            
def hedef_yön_değiştir(ayarlar):
    """Hedefimizin konumuna göre yönünü değiştirir."""
    ayarlar.hedef_yön *= -1

def hedef_güncelle(ayarlar, hedef, mermiler, istatistik, gemi):
    """ Hedef objemizin ekranını uç noktalarında
        olup olmadığını kontrol edelim ve buna göre
        güncelleme yapalım."""
    hedef_sınırları_kontrol(ayarlar, hedef)
    hedef.güncelle()

    # Mermi hedef çarpışmasını kontrol edelim.
    if pygame.sprite.spritecollideany(hedef, mermiler):
        mermiler.empty() # basit bir çözüm oldu aksi halde mermi hedefin arkasına geçiyor ve mermileri güncelle fonksiyonunu devreye geçiriyordu

def çarpışma(istatistik, gemi, mermiler):
    """ Mermi ile hedef çarpışmasını olayını kontrol eder."""
    if istatistik.oyun_hakkı > 0:
        #oyun_hakkını bir azaltalım.
        istatistik.oyun_hakkı -= 1

        # Mermiler listesini boşaltalım
        mermiler.empty()

        # Gemiyi başlangıç konumuna alalım
        gemi.merkez_gemi()

        # Pause
        sleep(0.5)
    else:
        istatistik.oyun_aktifliği = False
        

