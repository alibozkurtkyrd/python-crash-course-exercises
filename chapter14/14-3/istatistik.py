class İstatistik():
    """Oyunun istatistiksel bilgilerini muhafaza eder."""

    def __init__(self, ayarlar):
        """İstatistiğe initialize yapalım."""
        self.ayarlar = ayarlar
        self.istatistik_sıfırla()

        # Oyunu inaktif konumda başlatalım
        self.oyun_aktifliği = False

    def istatistik_sıfırla(self):
        """oyun sırasında değişken olan istatistik ile ilgili initialize yapalım."""
        self.oyun_hakkı = self.ayarlar.oyun_hakkı
