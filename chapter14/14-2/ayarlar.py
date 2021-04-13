class Ayarlar():
    """ Oyun ile ilgili tüm ayarları içerir."""

    def __init__(self):
        """ oyun ayarları için initialize yapalım"""
        # Ekran ayarları
        self.ekran_genişliği = 1000
        self.ekran_uzunluğu = 600
        self.ap_renk = (230, 230, 230)

        # Gemi ayarları
        self.gemi_hızı = 1.5
        self.oyun_hakkı = 3

        # Mermi ayarları
        self.mermi_hızı = 1
        self.mermi_genişliği = 15
        self.mermi_yüksekliği = 3
        self.mermi_rengi = 60, 60, 60
        self.izinverilen_mermi = 6

        # Hedef yönü 1 aşağı yönü -1 yukarı yönü temsil eder
        self.hedef_yön = 1

        # Hedef ayarlar
        self.hedef_hızı = 0.5

        
