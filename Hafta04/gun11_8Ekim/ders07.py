class calisan():

    zam_oranı = 1.05
    per_say = 0

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        calisan.per_say = calisan.per_say + 1
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

    def arttir(self):
        # self.maas = (self.maas*1.05)
        # self.maas = (self.maas * calisan.zam_oranı)
        self.maas = (self.maas * self.zam_oranı)

class gelistirici(calisan):
    def __init__(self,ad,soyad,maas,p_dili):
        # calisan.__init__(self,ad,soyad,maas)
        super().__init__(ad,soyad,maas)
        self.p_dili = p_dili
        self.zam_oranı = 1.2

class yonetici(calisan):
    def __init__(self,ad,soyad,maas,calisanlar = None):
        super().__init__(ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def eleman_ekle(self,eleman):
        self.calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.calisanlar.remove(eleman)

    def calisan_listele(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())

personel1 = calisan("ali","demir",2500)
personel2 = calisan("kerim","bakir",1950)

gel1 = gelistirici("mehmet","can",2250,"Python")
# print(gel1.tamad(), gel1.p_dili, gel1.maas)
gel1.arttir()
# print(gel1.maas)

yonet1 = yonetici("kamil","eren",6500,[gel1,personel1])
print(yonet1.tamad())
print(yonet1.calisan_listele())
yonet1.eleman_ekle(personel2)
print(yonet1.calisan_listele())
yonet1.eleman_cikar(gel1)
print(yonet1.calisan_listele())

print(isinstance(personel2,yonetici))

print(issubclass(calisan,yonetici))
print(issubclass(gelistirici,calisan))
