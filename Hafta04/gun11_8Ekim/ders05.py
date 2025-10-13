# Örnek 2: Çok Seviyeli Kalıtım - Personel Yönetim Sistemi
class Personel:
    """Tüm personelin ortak özellikleri"""
    
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.gorev = "Personel"
    
    def tam_isim(self):
        return f"{self.ad} {self.soyad}"
    
    def maas_arttir(self, oran):
        """Personelin maaşını arttırır"""
        self.maas += self.maas * oran / 100
        print(f"{self.tam_isim()} maaşı %{oran} arttırıldı. Yeni maaş: {self.maas:.2f} TL")
    
    def bilgileri_goster(self):
        print(f"\n--- {self.gorev} ---")
        print(f"Ad Soyad: {self.tam_isim()}")
        print(f"Maaş: {self.maas:.2f} TL")

class Yonetici(Personel):
    """Yönetici personel sınıfı"""
    
    def __init__(self, ad, soyad, maas, departman, calisan_sayisi):
        super().__init__(ad, soyad, maas)
        self.departman = departman
        self.calisan_sayisi = calisan_sayisi
        self.gorev = "Yönetici"
    
    def departman_degistir(self, yeni_departman):
        """Yöneticinin departmanını değiştirir"""
        self.departman = yeni_departman
        print(f"{self.tam_isim()} {yeni_departman} departmanına atandı.")
    
    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Departman: {self.departman}")
        print(f"Çalışan Sayısı: {self.calisan_sayisi}")

class Mudur(Yonetici):
    """Müdür sınıfı - Yonetici sınıfından türetilmiş"""
    
    def __init__(self, ad, soyad, maas, departman, calisan_sayisi, sorumlu_bolge):
        super().__init__(ad, soyad, maas, departman, calisan_sayisi)
        self.sorumlu_bolge = sorumlu_bolge
        self.gorev = "Müdür"
        self.bonus = maas * 0.2  # %20 bonus
    
    def bolge_degistir(self, yeni_bolge):
        """Müdürün sorumlu olduğu bölgeyi değiştirir"""
        self.sorumlu_bolge = yeni_bolge
        print(f"{self.tam_isim()} {yeni_bolge} bölgesinden sorumlu oldu.")
    
    def toplam_gelir(self):
        """Müdürün toplam gelirini hesaplar"""
        return self.maas + self.bonus
    
    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Sorumlu Bölge: {self.sorumlu_bolge}")
        print(f"Bonus: {self.bonus:.2f} TL")
        print(f"Toplam Gelir: {self.toplam_gelir():.2f} TL")

# Çok seviyeli kalıtım kullanımı
print("\n=== ÇOK SEVİYELİ KALITIM: PERSONEL SİSTEMİ ===")

# Farklı seviyelerde personel oluşturma
personel1 = Personel("Ali", "Yılmaz", 5000)
yonetici1 = Yonetici("Ayşe", "Kaya", 8000, "Satış", 5)
mudur1 = Mudur("Mehmet", "Demir", 12000, "Üretim", 25, "İstanbul")

# Bilgileri göster
personel1.bilgileri_goster()
yonetici1.bilgileri_goster()
mudur1.bilgileri_goster()

# Metotları kullanma
print("\n--- İşlemler ---")
personel1.maas_arttir(10)
yonetici1.departman_degistir("Pazarlama")
mudur1.bolge_degistir("Ankara")
mudur1.maas_arttir(15)

# Güncel bilgiler
mudur1.bilgileri_goster()