class Ayarlar():
    """ Uzaylı istlası oyunumuz için tüm ayarları içeren sınıftır."""

    def __init__(self):
        """ oyunun ayarları başlangıçı."""
        # Ekran ayarları
        self.ekran_genişliği = 1000
        self.ekran_uzunluğu = 600
        self.bg_renk = (230, 230, 230)

        # Gemi ayarları
        self.gemi_hızı = 1.5

        # Mermi ayarları
        self.mermi_hızı = 1
        self.mermi_genişliği = 15
        self.mermi_yüksekliği = 3
        self.mermi_rengi = 60, 60, 60
        self.izinverilen_mermi = 6

        
