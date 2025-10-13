"""
Özel Metotlar (Magic/Dunder Methods)
Python'da çift alt çizgi ile başlayıp biten özel metotlardır.
"""

# Örnek 5: Temel Özel Metotlar - Vektör Sınıfı
class Vektor:
    """2D vektör sınıfı - Özel metot örneği"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # def __str__(self):
    #     """Kullanıcı dostu string gösterimi"""
    #     return f"Vektor str({self.x}, {self.y})"
    
    # def __repr__(self):
    #     """Geliştirici dostu string gösterimi"""
    #     return f"Vektor repr({self.x}, {self.y})"
    
        # __str__ ve __repr__ metotları

    # Aritmetik operatörler
    def __add__(self, other):
        """+ operatörü için: v1 + v2"""
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """- operatörü için: v1 - v2"""
        return Vektor(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """* operatörü için: v1 * sayı"""
        if isinstance(scalar, (int, float)):
            return Vektor(self.x * scalar, self.y * scalar)
        raise TypeError("Skaler ile çarpılmalı!")
    
    def __truediv__(self, scalar):
        """/ operatörü için: v1 / sayı"""
        if isinstance(scalar, (int, float)):
            return Vektor(self.x / scalar, self.y / scalar)
        raise TypeError("Skaler ile bölünmeli!")
    
    # Karşılaştırma operatörleri
    def __eq__(self, other):
        """== operatörü için: v1 == v2"""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """< operatörü için: v1 < v2 (büyüklük karşılaştırması)"""
        return self.buyukluk() < other.buyukluk()
    
    def __len__(self):
        """len() fonksiyonu için"""
        return 2  # 2D vektör
    
    # Yardımcı metotlar
    def buyukluk(self):
        """Vektörün büyüklüğünü hesaplar"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def nokta_carpim(self, other):
        """İki vektörün nokta çarpımı"""
        return self.x * other.x + self.y * other.y

# Özel metot kullanımı
print("=== ÖZEL METOTLAR: VEKTÖR SINIFI ===")

# Vektörler oluşturma
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

# __str__ ve __repr__ kullanımı
print(f"v1: {v1}")  # __str__ çağrılır
print(f"v2: {v2}")

# Aritmetik operatörler
print(f"\n--- Aritmetik İşlemler ---")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 / 2 = {v1 / 2}")

# Karşılaştırma operatörleri
print(f"\n--- Karşılaştırma İşlemleri ---")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 < v2: {v1 < v2}")

# Diğer özel metotlar
print(f"\n--- Diğer İşlemler ---")
print(f"len(v1): {len(v1)}")
print(f"v1 büyüklük: {v1.buyukluk():.2f}")
print(f"v2 büyüklük: {v2.buyukluk():.2f}")
print(f"Nokta çarpım: {v1.nokta_carpim(v2)}")