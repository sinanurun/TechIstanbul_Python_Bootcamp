class Calisan():

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        Calisan.per_say = Calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * Calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

class Gelistirici(Calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        # Calisan.__init__(self,ad,soyad,maas)
        super().__init__(ad,soyad,maas)
        self.p_dili = p_dili
        self.zam_oranı = 1.2

class Yonetici(Calisan):
    def __init__(self,ad,soyad,maas,Calisanlar = None):
        super().__init__(ad,soyad,maas)
        if Calisanlar is None:
            self.Calisanlar = []
        else:
            self.Calisanlar = Calisanlar

    def eleman_ekle(self,eleman):
        self.Calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.Calisanlar.remove(eleman)

    def Calisan_listele(self):
        for eleman in self.Calisanlar:
            print(eleman.tamad())

personel1 = Calisan("ali","demir",2500)
personel2 = Calisan("kerim","bakir",1950)

gel1 = Gelistirici("mehmet","can",2250,"Python")
# print(gel1.tamad(), gel1.p_dili, gel1.maas)
gel1.arttir()
# print(gel1.maas)

yonet1 = Yonetici("kamil","eren",6500,[gel1,personel1])
print(yonet1.tamad())
print(yonet1.Calisan_listele())
yonet1.eleman_ekle(personel2)
print(yonet1.Calisan_listele())
yonet1.eleman_cikar(gel1)
print(yonet1.Calisan_listele())

print(isinstance(personel2,Yonetici))

print(issubclass(Calisan,Yonetici))
print(issubclass(Gelistirici,Calisan))
