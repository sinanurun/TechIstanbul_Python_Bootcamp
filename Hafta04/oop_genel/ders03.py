class Calisan:

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

    @classmethod
    def zam_orani_degis(cls,yeni_oran):
        cls.zam_oranı = yeni_oran

    @classmethod
    def ypersonel(cls,pbilgisi):
        ad, soyad, maas = pbilgisi.split("-")
        return cls(ad,soyad,maas)

    @staticmethod
    def tel_no(telefon):
        return telefon.split(" ")


personel1 = Calisan("ali","demir",2500)
personel2 = Calisan("kerim","bakir",1950)

mpersonel1 = "veli-can-4000"
mpersonel2 = "mert-haydar-3200"

ypersonel1 = Calisan.ypersonel(mpersonel1)
print(ypersonel1.eposta)

gtelefon = "0123 456 78 90"
print(Calisan.tel_no(gtelefon))



# Calisan.zam_orani_degis(1.5)

# Calisan.zam_oranı = 1.2
# personel1.zam_oranı = 1.1
# print(personel1.maas)
# personel1.arttir()
# print(personel1.maas)
# personel2.zam_oranı = 1.15
# print(personel2.maas)
# personel2.arttir()
# print(personel2.maas)

