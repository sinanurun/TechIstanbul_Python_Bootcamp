# Örnek 3: Çok Biçimlilik Örneği - Şekiller
"""
Çok Biçimlilik (Polymorphism)
Aynı metot adının farklı sınıflarda 
farklı şekillerde davranmasıdır.
"""

class Sekil:
    """Geometrik şekillerin temel sınıfı"""
    
    def __init__(self, isim):
        self.isim = isim
    
    def alan_hesapla(self):
        """Şeklin alanını hesaplar - Soyut metot"""
        raise NotImplementedError("Bu metot alt sınıflarda tanımlanmalıdır!")
    
    def cevre_hesapla(self):
        """Şeklin çevresini hesaplar - Soyut metot"""
        raise NotImplementedError("Bu metot alt sınıflarda tanımlanmalıdır!")
    
    def bilgileri_goster(self):
        """Şeklin bilgilerini gösterir"""
        print(f"\n--- {self.isim} ---")
        print(f"Alan: {self.alan_hesapla():.2f}")
        print(f"Çevre: {self.cevre_hesapla():.2f}")

class Dikdortgen(Sekil):
    """Dikdörtgen sınıfı"""
    
    def __init__(self, genislik, yukseklik):
        super().__init__("Dikdörtgen")
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    def alan_hesapla(self):
        """Dikdörtgenin alanını hesaplar"""
        return self.genislik * self.yukseklik
    
    def cevre_hesapla(self):
        """Dikdörtgenin çevresini hesaplar"""
        return 2 * (self.genislik + self.yukseklik)

class Daire(Sekil):
    """Daire sınıfı"""
    
    def __init__(self, yaricap):
        super().__init__("Daire")
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        """Dairenin alanını hesaplar"""
        return 3.14159 * self.yaricap ** 2
    
    def cevre_hesapla(self):
        """Dairenin çevresini hesaplar"""
        return 2 * 3.14159 * self.yaricap

class Ucgen(Sekil):
    """Üçgen sınıfı"""
    
    def __init__(self, taban, yukseklik, kenar1, kenar2):
        super().__init__("Üçgen")
        self.taban = taban
        self.yukseklik = yukseklik
        self.kenar1 = kenar1
        self.kenar2 = kenar2
    
    def alan_hesapla(self):
        """Üçgenin alanını hesaplar"""
        return (self.taban * self.yukseklik) / 2
    
    def cevre_hesapla(self):
        """Üçgenin çevresini hesaplar"""
        return self.taban + self.kenar1 + self.kenar2

# Çok biçimlilik kullanımı
print("=== ÇOK BİÇİMLİLİK: GEOMETRİK ŞEKİLLER ===")

# Farklı şekil nesneleri oluşturma
dikdortgen = Dikdortgen(5, 3)
daire = Daire(4)
ucgen = Ucgen(6, 4, 5, 5)

# Şekilleri liste içinde topla
sekiller = [dikdortgen, daire, ucgen]

# Çok biçimlilik: Aynı metot farklı davranışlar
print("--- Tüm Şekillerin Alan ve Çevreleri ---")
for sekil in sekiller:
    sekil.bilgileri_goster()

# Alanları karşılaştırma
print("\n--- Alan Karşılaştırması ---")
for sekil in sekiller:
    print(f"{sekil.isim} Alanı: {sekil.alan_hesapla():.2f}")

# Çevreleri karşılaştırma
print("\n--- Çevre Karşılaştırması ---")
for sekil in sekiller:
    print(f"{sekil.isim} Çevresi: {sekil.cevre_hesapla():.2f}")