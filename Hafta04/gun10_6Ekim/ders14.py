# ÖRNEK 2: self ve Özellik Kullanımı
class Dikdortgen:
    """Dikdörtgen sınıfı"""
    
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    def alan(self):
        """Dikdörtgenin alanını hesaplar"""
        return self.uzunluk * self.genislik
    
    def cevre(self):
        """Dikdörtgenin çevresini hesaplar"""
        return 2 * (self.uzunluk + self.genislik)
    
    def buyut(self, oran):
        """Dikdörtgeni büyütür"""
        self.uzunluk *= oran
        self.genislik *= oran
        return f"Yeni boyutlar: {self.uzunluk} x {self.genislik}"

# Kullanım
dikdortgen1 = Dikdortgen(5, 3)
print(f"Alan: {dikdortgen1.alan()}")
print(f"Çevre: {dikdortgen1.cevre()}")

dikdortgen1.buyut(2)
print(f"Büyütülmüş Alan: {dikdortgen1.alan()}")