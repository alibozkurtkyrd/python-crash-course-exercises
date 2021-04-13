class İstatistik():
    """catch oyunu ile ilgili istatistikleri barındırır"""

    def __init__(self, ayarlar):
        """istatistik için başlangıç."""
        self.ayarlar = ayarlar
        self.sıfırla()

        # catch oyununu aktif konumda çalıştıralım
        self.oyun_aktifliği = True

    def sıfırla(self):
        """oyun anındaki istatistsel değişim ile ilgili başlangıç yapar."""
        self.top_hakkı = self.ayarlar.top_limit
