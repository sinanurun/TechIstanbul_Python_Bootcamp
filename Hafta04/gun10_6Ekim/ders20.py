# ÖRNEK 8: Geometrik Şekiller
class Nokta:
    """2D nokta sınıfı"""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def uzaklik(self, diger_nokta):
        """İki nokta arasındaki uzaklığı hesaplar"""
        return ((self.x - diger_nokta.x) ** 2 + (self.y - diger_nokta.y) ** 2) ** 0.5
    
    def __str__(self):
        """Noktanın string gösterimi"""
        return f"({self.x}, {self.y})"

class Cember:
    """Çember sınıfı"""
    
    def __init__(self, merkez, yaricap):
        self.merkez = merkez  # Nokta nesnesi
        self.yaricap = yaricap
    
    def alan(self):
        """Çemberin alanını hesaplar"""
        return 3.14159 * self.yaricap ** 2
    
    def cevre(self):
        """Çemberin çevresini hesaplar"""
        return 2 * 3.14159 * self.yaricap
    
    def nokta_icinde_mi(self, nokta):
        """Bir noktanın çember içinde olup olmadığını kontrol eder"""
        return self.merkez.uzaklik(nokta) <= self.yaricap

class Dikdortgen:
    """Dikdörtgen sınıfı"""
    
    def __init__(self, sol_ust, sag_alt):
        self.sol_ust = sol_ust  # Nokta nesnesi
        self.sag_alt = sag_alt  # Nokta nesnesi
    
    def genislik(self):
        """Dikdörtgenin genişliğini hesaplar"""
        return abs(self.sag_alt.x - self.sol_ust.x)
    
    def yukseklik(self):
        """Dikdörtgenin yüksekliğini hesaplar"""
        return abs(self.sag_alt.y - self.sol_ust.y)
    
    def alan(self):
        """Dikdörtgenin alanını hesaplar"""
        return self.genislik() * self.yukseklik()
    
    def cevre(self):
        """Dikdörtgenin çevresini hesaplar"""
        return 2 * (self.genislik() + self.yukseklik())
    
    def nokta_icinde_mi(self, nokta):
        """Bir noktanın dikdörtgen içinde olup olmadığını kontrol eder"""
        return (self.sol_ust.x <= nokta.x <= self.sag_alt.x and 
                self.sol_ust.y <= nokta.y <= self.sag_alt.y)

# Kullanım
# Noktalar oluştur
nokta1 = Nokta(0, 0)
nokta2 = Nokta(3, 4)
nokta3 = Nokta(2, 2)

print(f"Nokta1: {nokta1}")
print(f"Nokta2: {nokta2}")
print(f"Uzaklık: {nokta1.uzaklik(nokta2):.2f}")

# Çember oluştur
cember = Cember(nokta1, 5)
print(f"\nÇember Alanı: {cember.alan():.2f}")
print(f"Çember Çevresi: {cember.cevre():.2f}")
print(f"Nokta2 çember içinde mi: {cember.nokta_icinde_mi(nokta2)}")

# Dikdörtgen oluştur
dikdortgen = Dikdortgen(Nokta(1, 1), Nokta(4, 3))
print(f"\nDikdörtgen Alanı: {dikdortgen.alan()}")
print(f"Dikdörtgen Çevresi: {dikdortgen.cevre()}")
print(f"Nokta3 dikdörtgen içinde mi: {dikdortgen.nokta_icinde_mi(nokta3)}")