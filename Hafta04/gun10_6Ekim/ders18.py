# ÖRNEK 6: E-Ticaret Ürün Sistemi
class Urun:
    """E-ticaret ürün sınıfı"""
    
    def __init__(self, urun_adi, fiyat, stok, kategori):
        self.urun_adi = urun_adi
        self.fiyat = fiyat
        self.stok = stok
        self.kategori = kategori
        self.indirim_orani = 0
    
    def indirim_uygula(self, indirim_orani):
        """Ürüne indirim uygular"""
        if 0 <= indirim_orani <= 100:
            self.indirim_orani = indirim_orani
            return f"%{indirim_orani} indirim uygulandı"
        else:
            return "Geçersiz indirim oranı"
    
    def indirimli_fiyat(self):
        """İndirimli fiyatı hesaplar"""
        return self.fiyat * (1 - self.indirim_orani / 100)
    
    def stok_durumu(self):
        """Stok durumunu kontrol eder"""
        if self.stok == 0:
            return "Stokta yok"
        elif self.stok <= 5:
            return f"Son {self.stok} ürün!"
        else:
            return f"Stokta {self.stok} adet var"
    
    def satis_bilgileri(self):
        """Tüm satış bilgilerini gösterir"""
        bilgi = f"Ürün: {self.urun_adi}\n"
        bilgi += f"Kategori: {self.kategori}\n"
        bilgi += f"Normal Fiyat: {self.fiyat:.2f} TL\n"
        
        if self.indirim_orani > 0:
            bilgi += f"İndirim: %{self.indirim_orani}\n"
            bilgi += f"İndirimli Fiyat: {self.indirimli_fiyat():.2f} TL\n"
        
        bilgi += f"Stok: {self.stok_durumu()}"
        return bilgi

# Kullanım
urun1 = Urun("iPhone 14", 25000, 10, "Telefon")
urun2 = Urun("Samsung TV", 15000, 3, "Televizyon")

print(urun1.satis_bilgileri())
print("\n" + "="*40 + "\n")

urun1.indirim_uygula(15)
print(urun1.satis_bilgileri())