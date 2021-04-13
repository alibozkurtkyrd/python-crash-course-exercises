class Ayarlar():
    """ Oyun ile ilgili tüm ayarları içerir."""

    def __init__(self):
        """ oyun ayarları için initialize yapalım"""
        # Ekran ayarları
        self.ekran_genişliği = 1000
        self.ekran_uzunluğu = 700
        self.ap_renk = (230, 230, 230)

        # Gemi ayarları
        self.oyun_hakkı = 6

        # Mermi ayarları
        self.mermi_genişliği = 15
        self.mermi_yüksekliği = 3
        self.mermi_rengi = 60, 60, 60
        self.izinverilen_mermi = 6

        # oyun hızlanma ivmesi
        self.hızlanma_ivmesi = 1.1

        self.başlangıç_ayarları()

    def başlangıç_ayarları(self):
        """oyun boyunca değişen başlangıç ayarlarını yazalım."""
        self.gemi_hızı = 2
        self.mermi_hızı = 1
        self.hedef_hızı = 0.5
        
        # Hedef yönü 1 aşağı yönü -1 yukarı yönü temsil eder
        self.hedef_yön = 1
        
    def hız_arttır(self):
        """Oyun hızını arttıralım."""
        
        #self.gemi_hızı *= self.hızlanma_ivmesi  Geminin hızlanmasına gerek yok
        self.mermi_hızı *= self.hızlanma_ivmesi
        self.hedef_hızı *= self.hızlanma_ivmesi

        
        
