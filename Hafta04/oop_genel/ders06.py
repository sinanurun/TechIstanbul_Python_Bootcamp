class Calisan():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property
    def eposta(self):
        self.email = self.ad + self.soyad + "@sirket.com"
        return self.email

    @property
    def tamad(self):
        return "{} {}".format(self.ad,self.soyad)

    @tamad.setter
    def tamad(self,gelenisim):
        ad, soyad = gelenisim.split(" ")
        self.ad = ad
        self.soyad = soyad

    @tamad.deleter
    def tamad(self):
        self.ad = None
        self.soyad = None
        print("kullanıcı bilgileri silindi")



personel1 = Calisan("ali","demir")

# personel1.ad = "can"

print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)

personel1.tamad = "can bakir"
print("değişince-----")
print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)

del personel1.tamad

print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)
