
class Ayarlar():
    """Bu sınıf yazdığın program için tüm ayarları içerir"""

    def __init__(self):
        """Oyun ayarları için initialize """
        # screen settings
        self.ekran_genişliği = 1000
        self.ekran_yüksekliği = 600
        self.bg_renk = (230, 230, 230)

        # Cisim ayarları
        self.cisim_hız_faktörü = 1.5
