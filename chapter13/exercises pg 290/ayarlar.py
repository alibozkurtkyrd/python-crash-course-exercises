class Ayarlar():
    """Catch isimli oyunumuz için tüm ayarları içerir."""

    def __init__(self):
        """Oyun ayarları için başlangıç."""
        # Ekran ayarları
        self.ekran_genişliği = 1100
        self.ekran_yüksekliği = 600
        self.ap_renk = (252, 252, 252) # ap = arka plan

        # Hol ayarları
        self.hol_hızı = 3

        # Top ayarları
        self.top_hızı = 0.4
        self.top_limit = 3
