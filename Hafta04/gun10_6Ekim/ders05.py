# __init__ Metodu – Kurucu (Constructor)
# Nesne oluşturulurken otomatik çağrılır.
# Başlangıç durumunu (özellikleri) tanımlar.

class Araba:
    def __init__(self, marka, model): #constructor method
        self.marka = marka #self o an oluşturulan nesneyi temsil eder
        self.model = model

araba1 = Araba("Toyota","Coralla")
print(araba1)
print(araba1.marka, araba1.model)


class Ogrenci():
    bolum = "Maliye"
    bina = "Kuzey"
    def __init__(self):
        self.ad = ""
        self.soyad = ""
        self.tcno = ""

ogr1 = Ogrenci()
print(ogr1.bolum)
ogr1.ad = "Sevgi"
print(ogr1.ad)
ogr2 = Ogrenci()
print(ogr2.ad)