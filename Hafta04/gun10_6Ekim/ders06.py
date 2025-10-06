# Metotlar (Methods)
# Sınıf içinde tanımlanan fonksiyonlardır.
# self parametresi zorunludur (otomatik aktarılır).

# self Anahtar Kelimesi
# Her metot ilk parametre olarak self alır.
# Python, nesne.metot() çağrısında selfi otomatik ekler.
# self yerine başka isim de kullanılabilir ama best practice değildir.

class Araba:
    def __init__(self, marka, model): #constructor method
        self.marka = marka #self o an oluşturulan nesneyi temsil eder
        self.model = model
    def bilgi_goster(self):
        return f"{self.marka} {self.model}"

araba1 = Araba("Toyota","Coralla")
print(araba1)
print(araba1.marka, araba1.model)
print(araba1.bilgi_goster)


class Ogrenci():
    bolum = "Maliye"
    bina = "Kuzey"
    def __init__(self, ad, soyad, tcno):
        self.ad = ad
        self.soyad = soyad
        self.tcno = tcno

    def tamad(self):
        self.tam_isim = self.ad + self.soyad
        return self.tam_isim
    def __str__(self):
        return self.ad + self.soyad

ogr1 = Ogrenci("Sevgi","Can","12541254")
print(ogr1)
ogr1.tamad()
print(ogr1.tam_isim)
ogr2 = Ogrenci("Berk","Veli","87878784")
print(ogr2)
ogr2.tamad()
print(ogr2.tam_isim)