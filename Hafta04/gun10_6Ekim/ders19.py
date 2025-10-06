# ÖRNEK 7: Kütüphane Yönetim Sistemi
class Kitap:
    """Kitap sınıfı"""
    
    def __init__(self, isbn, baslik, yazar, sayfa_sayisi, yayin_yili):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.yayin_yili = yayin_yili
        self.odunc_alindi = False
    
    def odunc_al(self):
        """Kitabı ödünç alır"""
        if not self.odunc_alindi:
            self.odunc_alindi = True
            return f"'{self.baslik}' ödünç alındı"
        else:
            return f"'{self.baslik}' zaten ödünç alınmış"
    
    def iade_et(self):
        """Kitabı iade eder"""
        if self.odunc_alindi:
            self.odunc_alindi = False
            return f"'{self.baslik}' iade edildi"
        else:
            return f"'{self.baslik}' zaten kütüphanede"
    
    def kitap_bilgileri(self):
        """Kitap bilgilerini gösterir"""
        durum = "Ödünç Alındı" if self.odunc_alindi else "Kütüphanede"
        return f"ISBN: {self.isbn}\nBaşlık: {self.baslik}\nYazar: {self.yazar}\nSayfa: {self.sayfa_sayisi}\nYıl: {self.yayin_yili}\nDurum: {durum}"

class Kutuphane:
    """Kütüphane yönetim sınıfı"""
    
    def __init__(self, ad):
        self.ad = ad
        self.kitaplar = []  # Kitap nesnelerini tutan liste
    
    def kitap_ekle(self, kitap):
        """Kütüphaneye kitap ekler"""
        self.kitaplar.append(kitap)
        return f"'{kitap.baslik}' kütüphaneye eklendi"
    
    def kitap_ara(self, anahtar_kelime):
        """Kitap arama"""
        bulunan_kitaplar = []
        for kitap in self.kitaplar:
            if (anahtar_kelime.lower() in kitap.baslik.lower() or 
                anahtar_kelime.lower() in kitap.yazar.lower()):
                bulunan_kitaplar.append(kitap)
        return bulunan_kitaplar
    
    def mufred_kitaplar(self):
        """Mevcut kitapları listeler"""
        return [kitap for kitap in self.kitaplar if not kitap.odunc_alindi]
    
    def odunc_alinan_kitaplar(self):
        """Ödünç alınan kitapları listeler"""
        return [kitap for kitap in self.kitaplar if kitap.odunc_alindi]
    
    def kutuphane_durumu(self):
        """Kütüphane durum raporu"""
        toplam = len(self.kitaplar)
        odunc_alinan = len(self.odunc_alinan_kitaplar())
        mevcut = len(self.mufred_kitaplar())
        
        rapor = f"=== {self.ad} Kütüphanesi ===\n"
        rapor += f"Toplam Kitap: {toplam}\n"
        rapor += f"Mevcut: {mevcut}\n"
        rapor += f"Ödünç: {odunc_alinan}\n"
        return rapor

# Kullanım
kutuphane = Kutuphane("Merkez Kütüphane")

# Kitap oluştur ve ekle
kitap1 = Kitap("123456", "Python Programlama", "Ahmet Yılmaz", 350, 2023)
kitap2 = Kitap("789012", "Veri Bilimi", "Ayşe Kaya", 280, 2022)

kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)

print(kutuphane.kutuphane_durumu())

# Kitap ödünç al
print(kitap1.odunc_al())
print(kutuphane.kutuphane_durumu())

# Kitap ara
bulunanlar = kutuphane.kitap_ara("python")
for kitap in bulunanlar:
    print(kitap.kitap_bilgileri())