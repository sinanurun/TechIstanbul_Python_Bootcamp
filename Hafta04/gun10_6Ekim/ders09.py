# class methodlar kullanımına ikinci örnek 
# okul öğrenci örneği

class Ogrenci:
    okul_adi = "Techİstanbul - Ecodation"  # Class değişkeni
    ogrenci_sayisi = 0           # Class değişkeni

    def __init__(self, ad, soyad, not_ort):
        self.ad = ad
        self.soyad = soyad
        self.not_ort = not_ort
        Ogrenci.ogrenci_sayisi += 1  # Her öğrenci oluşturulduğunda artar

    # Instance method
    def bilgi_goster(self):
        print(f"{self.ad} {self.soyad} - Not Ortalaması: {self.not_ort}")

    # Class method
    @classmethod
    def okul_bilgisi(cls):
        print(f"Okul: {cls.okul_adi}, Toplam Öğrenci: {cls.ogrenci_sayisi}")

    # Static method
    @staticmethod
    def ortalama_hesapla(notlar):
        return sum(notlar) / len(notlar) if notlar else 0

# Öğrenci ekleme
ogr1 = Ogrenci("Sinan", "Urun", 90)
ogr2 = Ogrenci("Elif", "Kaya", 85)
ogr3 = Ogrenci("Ahmet", "Demir", 70)

# Bilgileri göster
ogr1.bilgi_goster()
ogr2.bilgi_goster()
ogr3.bilgi_goster()

# Okul bilgisi (class method)
Ogrenci.okul_bilgisi()
ogr1.okul_bilgisi()

# Ortalama hesaplama (static method)
notlar = [ogr1.not_ort, ogr2.not_ort, ogr3.not_ort]
genel_ort = Ogrenci.ortalama_hesapla(notlar)
print(f"Genel Ortalama: {genel_ort}")
