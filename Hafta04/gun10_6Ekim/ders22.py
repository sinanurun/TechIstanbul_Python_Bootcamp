class Calisan():
    sirket = "Techİstanbul"
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.fEposta()

    def fEposta(self):
        return self.ad + self.soyad + "@sirket.com"

    @classmethod
    def fSirketDegis(cls):
        cls.sirket = input("Yeni Çalışacaklar İçin Şirket Bilgisi Giriniz : ")
        return cls.sirket

    def __str__(self):
        return f"{self.ad}, {self.soyad}, {self.maas}, {self.eposta}"


print(Calisan.sirket)
# print(Calisan.fSirketDegis())
calisan1 = Calisan("Berk","Can",100000)
print(calisan1.eposta)
print(calisan1.sirket)
calisan1.sirket = "Adu"
print(calisan1.sirket, Calisan.sirket)
Calisan.fSirketDegis()
calisan2 = Calisan("Berkay","Canan",505050)
print(calisan1.sirket, Calisan.sirket,calisan2.sirket)
calisan1.maas *= 1.5
print(calisan1.maas)
print(calisan1)