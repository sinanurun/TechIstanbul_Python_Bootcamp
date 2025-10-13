# Örnek 7: Kütüphane Yönetim Sistemi - Kalıtım ve Çok Biçimlilik
class Kitap:
    """Kitap sınıfı - Tüm kitapların temel sınıfı"""
    
    def __init__(self, isbn, baslik, yazar, yayin_yili):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self.odunc_alindi = False
    
    def odunc_al(self):
        """Kitabı ödünç alır"""
        if not self.odunc_alindi:
            self.odunc_alindi = True
            print(f"'{self.baslik}' ödünç alındı.")
            return True
        else:
            print(f"'{self.baslik}' zaten ödünç alınmış.")
            return False
    
    def iade_et(self):
        """Kitabı iade eder"""
        if self.odunc_alindi:
            self.odunc_alindi = False
            print(f"'{self.baslik}' iade edildi.")
            return True
        else:
            print(f"'{self.baslik}' zaten kütüphanede.")
            return False
    
    def bilgileri_goster(self):
        """Kitap bilgilerini gösterir"""
        durum = "Ödünç Alındı" if self.odunc_alindi else "Kütüphanede"
        print(f"\n--- {self.baslik} ---")
        print(f"ISBN: {self.isbn}")
        print(f"Yazar: {self.yazar}")
        print(f"Yayın Yılı: {self.yayin_yili}")
        print(f"Durum: {durum}")

class Roman(Kitap):
    """Roman sınıfı - Kitap sınıfından türetilmiş"""
    
    def __init__(self, isbn, baslik, yazar, yayin_yili, tur, sayfa_sayisi):
        super().__init__(isbn, baslik, yazar, yayin_yili)
        self.tur = tur  # Aşk, Macera, Polisiye vb.
        self.sayfa_sayisi = sayfa_sayisi
        self.kitap_turu = "Roman"
    
    def bilgileri_goster(self):
        """Roman bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Tür: {self.tur}")
        print(f"Sayfa Sayısı: {self.sayfa_sayisi}")
        print(f"Kitap Türü: {self.kitap_turu}")

class DersKitabi(Kitap):
    """Ders kitabı sınıfı - Kitap sınıfından türetilmiş"""
    
    def __init__(self, isbn, baslik, yazar, yayin_yili, ders, sinif):
        super().__init__(isbn, baslik, yazar, yayin_yili)
        self.ders = ders  # Matematik, Fizik vb.
        self.sinif = sinif  # 9, 10, 11, 12
        self.kitap_turu = "Ders Kitabı"
    
    def bilgileri_goster(self):
        """Ders kitabı bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Ders: {self.ders}")
        print(f"Sınıf: {self.sinif}")
        print(f"Kitap Türü: {self.kitap_turu}")

class Ansiklopedi(Kitap):
    """Ansiklopedi sınıfı - Kitap sınıfından türetilmiş"""
    
    def __init__(self, isbn, baslik, yazar, yayin_yili, cilt, konu):
        super().__init__(isbn, baslik, yazar, yayin_yili)
        self.cilt = cilt
        self.konu = konu  # Bilim, Tarih, Sanat vb.
        self.kitap_turu = "Ansiklopedi"
    
    def bilgileri_goster(self):
        """Ansiklopedi bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Cilt: {self.cilt}")
        print(f"Konu: {self.konu}")
        print(f"Kitap Türü: {self.kitap_turu}")

class Kutuphane:
    """Kütüphane yönetim sınıfı"""
    
    def __init__(self, isim):
        self.isim = isim
        self.kitaplar = []
    
    def kitap_ekle(self, kitap):
        """Kütüphaneye kitap ekler"""
        self.kitaplar.append(kitap)
        print(f"'{kitap.baslik}' kütüphaneye eklendi.")
    
    def kitap_ara(self, anahtar_kelime):
        """Kitaplarda arama yapar"""
        bulunanlar = []
        for kitap in self.kitaplar:
            if (anahtar_kelime.lower() in kitap.baslik.lower() or 
                anahtar_kelime.lower() in kitap.yazar.lower()):
                bulunanlar.append(kitap)
        return bulunanlar
    
    def odunc_al(self, baslik):
        """Kitap ödünç alır"""
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == baslik.lower():
                return kitap.odunc_al()
        print(f"'{baslik}' kütüphanede bulunamadı.")
        return False
    
    def iade_et(self, baslik):
        """Kitap iade eder"""
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == baslik.lower():
                return kitap.iade_et()
        print(f"'{baslik}' kütüphanede bulunamadı.")
        return False
    
    def kutuphane_durumu(self):
        """Kütüphane durumunu gösterir"""
        toplam = len(self.kitaplar)
        odunc_alinan = sum(1 for kitap in self.kitaplar if kitap.odunc_alindi)
        kutuphanede = toplam - odunc_alinan
        
        print(f"\n=== {self.isim} Kütüphanesi Durumu ===")
        print(f"Toplam Kitap: {toplam}")
        print(f"Ödünç Alınan: {odunc_alinan}")
        print(f"Kütüphanede: {kutuphanede}")
    
    def tum_kitaplari_goster(self):
        """Tüm kitapları gösterir"""
        print(f"\n=== {self.isim} Kütüphanesi - Tüm Kitaplar ===")
        for i, kitap in enumerate(self.kitaplar, 1):
            print(f"{i}. {kitap.baslik} - {kitap.yazar}")

# Kütüphane sistemi kullanımı
print("=== KÜTÜPHANE YÖNETİM SİSTEMİ ===")

# Kütüphane oluşturma
kutuphane = Kutuphane("Merkez Kütüphane")

# Farklı türde kitaplar ekleme
kutuphane.kitap_ekle(Roman("978-975-08-4521-1", "Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Psikolojik", 671))
kutuphane.kitap_ekle(DersKitabi("978-975-08-1234-5", "Matematik 10", "Ahmet Yılmaz", 2023, "Matematik", 10))
kutuphane.kitap_ekle(Ansiklopedi("978-975-08-7890-1", "Bilim Ansiklopedisi", "Mehmet Kaya", 2022, 1, "Bilim"))
kutuphane.kitap_ekle(Roman("978-975-08-4522-8", "Savaş ve Barış", "Lev Tolstoy", 1869, "Tarihi", 1225))

# Kütüphane durumu
kutuphane.kutuphane_durumu()

# Kitap ödünç alma
print("\n--- Ödünç Alma İşlemleri ---")
kutuphane.odunc_al("Suç ve Ceza")
kutuphane.odunc_al("Matematik 10")

# Arama işlemi
print("\n--- Arama İşlemleri ---")
bulunan_kitaplar = kutuphane.kitap_ara("savaş")
print("'savaş' kelimesi için bulunan kitaplar:")
for kitap in bulunan_kitaplar:
    print(f"  - {kitap.baslik}")

# Kitap bilgilerini göster
print("\n--- Kitap Detayları ---")
for kitap in kutuphane.kitaplar:
    kitap.bilgileri_goster()

# Güncel kütüphane durumu
kutuphane.kutuphane_durumu()

# Kitap iade
print("\n--- İade İşlemleri ---")
kutuphane.iade_et("Suç ve Ceza")

# Son durum
kutuphane.kutuphane_durumu()