"""
KALITIM TEMEL KAVRAMLARI:
- Üst sınıf (Parent class): Temel sınıf
- Alt sınıf (Child class): Üst sınıftan türeyen sınıf
- super(): Üst sınıfın metotlarına erişim
"""

class Ogrenci():
    def __init__(self,ad, soyad):
        self.ad = ad
        self.soyad = soyad

class BOgrenci(Ogrenci):
    def __init__(self,ad,soyad,bolum):
        # super().__init__(ad,soyad)
        Ogrenci.__init__(self,ad,soyad)
        self.bolum = bolum

class FOgrenci(BOgrenci):
    def __init__(self,ad,soyad,bolum,fakulte):
        BOgrenci.__init__(self,ad,soyad,bolum)
        self.fakulte = fakulte

gogrenci1 = Ogrenci("ali","veli")
print(gogrenci1.ad, gogrenci1.soyad)

bogrenci1 = BOgrenci("Neslihan","Can","Makine")
print(bogrenci1.ad, bogrenci1.soyad,bogrenci1.bolum)