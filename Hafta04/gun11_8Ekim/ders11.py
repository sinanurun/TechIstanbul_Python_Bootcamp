# Method Overriding ve super() Kullanımı
# Örnek 4: Method Overriding - Ödeme Sistemi
class Odeme:
    """Ödeme işlemlerinin temel sınıfı"""
    
    def __init__(self, tutar, tarih):
        self.tutar = tutar
        self.tarih = tarih
        self.odeme_durumu = "Bekliyor"
    
    def odeme_yap(self):
        """Ödeme yapma işlemi - Temel metot"""
        self.odeme_durumu = "Başarılı"
        print(f"{self.tutar} TL ödeme işlemi başlatıldı.")
    
    def iade_et(self):
        """Ödeme iadesi - Temel metot"""
        self.odeme_durumu = "İade Edildi"
        print(f"{self.tutar} TL iade edildi.")
    
    def bilgileri_goster(self):
        """Ödeme bilgilerini gösterir"""
        print(f"\n--- Ödeme Bilgileri ---")
        print(f"Tutar: {self.tutar} TL")
        print(f"Tarih: {self.tarih}")
        print(f"Durum: {self.odeme_durumu}")

class KrediKarti(Odeme):
    """Kredi kartı ile ödeme sınıfı"""
    
    def __init__(self, tutar, tarih, kart_no, son_kullanma):
        super().__init__(tutar, tarih)
        self.kart_no = kart_no[-4:]  # Son 4 haneyi sakla
        self.son_kullanma = son_kullanma
        self.odeme_tipi = "Kredi Kartı"
    
    def odeme_yap(self):
        """Kredi kartı ile ödeme yapar - Method overriding"""
        print(f"Kredi kartı ile {self.tutar} TL ödeme yapılıyor...")
        print(f"Kart: **** **** **** {self.kart_no}")
        print(f"Son kullanma: {self.son_kullanma}")
        
        # Ödeme işlemi simülasyonu
        self.odeme_durumu = "Başarılı"
        print("✅ Ödeme başarıyla tamamlandı!")
    
    def bilgileri_goster(self):
        """Kredi kartı ödeme bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()  # Üst sınıfın metodunu çağır
        print(f"Ödeme Tipi: {self.odeme_tipi}")
        print(f"Kart No: **** **** **** {self.kart_no}")

class BankaHavalesi(Odeme):
    """Banka havalesi ile ödeme sınıfı"""
    
    def __init__(self, tutar, tarih, banka_adi, iban):
        super().__init__(tutar, tarih)
        self.banka_adi = banka_adi
        self.iban = iban[-4:]  # Son 4 haneyi sakla
        self.odeme_tipi = "Banka Havalesi"
    
    def odeme_yap(self):
        """Banka havalesi ile ödeme yapar - Method overriding"""
        print(f"Banka havalesi ile {self.tutar} TL ödeme yapılıyor...")
        print(f"Banka: {self.banka_adi}")
        print(f"IBAN: **** **** **** {self.iban}")
        
        # Havale işlemi simülasyonu
        self.odeme_durumu = "İşlemde"
        print("⏳ Havale işlemi bankaya iletildi...")
        
        # 2 saniye sonra başarılı olacak
        self.odeme_durumu = "Başarılı"
        print("✅ Havale işlemi tamamlandı!")
    
    def bilgileri_goster(self):
        """Banka havalesi bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Ödeme Tipi: {self.odeme_tipi}")
        print(f"Banka: {self.banka_adi}")
        print(f"IBAN: **** **** **** {self.iban}")

class Nakit(Odeme):
    """Nakit ödeme sınıfı"""
    
    def __init__(self, tutar, tarih, para_birimi="TL"):
        super().__init__(tutar, tarih)
        self.para_birimi = para_birimi
        self.odeme_tipi = "Nakit"
    
    def odeme_yap(self):
        """Nakit ödeme yapar - Method overriding"""
        print(f"Nakit {self.tutar} {self.para_birimi} ödeme yapılıyor...")
        
        # Nakit ödeme simülasyonu
        self.odeme_durumu = "Tamamlandı"
        print("💰 Nakit ödeme alındı!")
    
    def para_ustu_hesapla(self, verilen_para):
        """Para üstü hesaplar - Ek metot"""
        para_ustu = verilen_para - self.tutar
        if para_ustu >= 0:
            print(f"Para üstü: {para_ustu} {self.para_birimi}")
            return para_ustu
        else:
            print(f"Eksik para! {abs(para_ustu)} {self.para_birimi} daha gerekiyor.")
            return para_ustu
    
    def bilgileri_goster(self):
        """Nakit ödeme bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Ödeme Tipi: {self.odeme_tipi}")
        print(f"Para Birimi: {self.para_birimi}")

# Method overriding kullanımı
print("\n=== METHOD OVERRIDING: ÖDEME SİSTEMİ ===")

# Farklı ödeme yöntemleri
odeme1 = KrediKarti(150.50, "2024-01-15", "1234567812345678", "12/25")
odeme2 = BankaHavalesi(275.00, "2024-01-15", "Ziraat Bankası", "TR123456789012345678901234")
odeme3 = Nakit(89.99, "2024-01-15", "TL")

# Ödemeleri liste içinde topla
odemeler = [odeme1, odeme2, odeme3]

# Çok biçimlilik: Aynı metot farklı davranışlar
print("--- Tüm Ödemeler ---")
for odeme in odemeler:
    odeme.odeme_yap()  # Her ödeme kendi odeme_yap metodunu kullanır
    odeme.bilgileri_goster()
    print("=" * 40)

# Nakit ödeme için ek metot kullanımı
print("--- Nakit Ödeme Detayı ---")
odeme3.para_ustu_hesapla(100)