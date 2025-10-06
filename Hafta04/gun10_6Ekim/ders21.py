# 1. Basit Kişi Sınıfı
class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
    
    def tanit(self):
        return f"Ben {self.ad}, {self.yas} yaşındayım"

# 2. Hesap Makinesi
class HesapMakinesi:
    def __init__(self):
        self.sonuc = 0
    
    def topla(self, sayi):
        self.sonuc += sayi
    
    def cikar(self, sayi):
        self.sonuc -= sayi
    
    def carp(self, sayi):
        self.sonuc *= sayi
    
    def bol(self, sayi):
        if sayi != 0:
            self.sonuc /= sayi

# 3. Hayvan Sınıfı
class Hayvan:
    def __init__(self, isim, tur):
        self.isim = isim
        self.tur = tur
    
    def ses_cikar(self):
        return "Ses çıkarıyor..."

# 4. Köpek Sınıfı (Hayvan'dan türetilmiş)
class Kopek(Hayvan):
    def __init__(self, isim, cins):
        super().__init__(isim, "Köpek")
        self.cins = cins
    
    def ses_cikar(self):
        return "Hav hav!"

# 5. Kedi Sınıfı
class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav!"

# 6. Daire Sınıfı
class Daire:
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    def alan(self):
        return 3.14159 * self.yaricap ** 2
    
    def cevre(self):
        return 2 * 3.14159 * self.yaricap

# 7. Öğrenci Not Sistemi
class Ogrenci:
    def __init__(self, ad):
        self.ad = ad
        self.notlar = []
    
    def not_ekle(self, not_degeri):
        self.notlar.append(not_degeri)
    
    def ortalama(self):
        return sum(self.notlar) / len(self.notlar) if self.notlar else 0

# 8. Araba Sınıfı
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.hiz = 0
    
    def hizlan(self):
        self.hiz += 10
    
    def yavasla(self):
        self.hiz = max(0, self.hiz - 10)

# 9. Telefon Rehberi
class Rehber:
    def __init__(self):
        self.kisiler = {}
    
    def kisi_ekle(self, isim, telefon):
        self.kisiler[isim] = telefon
    
    def kisi_ara(self, isim):
        return self.kisiler.get(isim, "Bulunamadı")

# 10. Market Sepeti
class Sepet:
    def __init__(self):
        self.urunler = {}
    
    def urun_ekle(self, urun, fiyat):
        self.urunler[urun] = fiyat
    
    def toplam(self):
        return sum(self.urunler.values())

# 11. Zaman Sınıfı
class Zaman:
    def __init__(self, saat, dakika):
        self.saat = saat
        self.dakika = dakika
    
    def goster(self):
        return f"{self.saat:02d}:{self.dakika:02d}"

# 12. Kitap Sınıfı
class Kitap:
    def __init__(self, baslik, yazar, sayfa):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa = sayfa
        self.okundu = False
    
    def oku(self):
        self.okundu = True


