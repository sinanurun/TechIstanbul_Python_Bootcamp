class Calisan():
    zam_orani = 1.1
    per_say = 0
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad + self.soyad + "@sirket.com"
        Calisan.per_say += 1

    def tamad(self):
        return "ad? : {}, soyad? : {}".format(self.ad, self.soyad)

    @classmethod
    def zam_orani_degis(cls,oran):
        cls.zam_orani = oran
    def arttirMaas(self):
        # self.maas = self.maas*1.05
        # self.maas = self.maas * self.zam_orani
        self.maas *= Calisan.zam_orani

    @staticmethod
    def tel_no_cevir(telefon):
        return telefon.split(" ")

    def ftel_numarasi(self):
        self.tel_numarasi= Calisan.tel_no_cevir(input("telefon giriniz"))

    @classmethod
    def yPersonel(cls,pbilgisi):
        ad, soyad, maas = pbilgisi.split("-")
        return cls(ad, soyad, maas)


personel3 = Calisan.yPersonel("vahide-can-854") # Calisan("vahide","can",854)


print(Calisan.tel_no_cevir("555 55 55 77"))

print(Calisan.per_say)
personel1 = Calisan("Veysel","Can",75000)
personel1.ftel_numarasi()
print(personel1.tel_numarasi)
print(Calisan.per_say)
personel2 = Calisan("Berkay","Canan",75500)
print(Calisan.per_say)
# personel1.arttirMaas(1.1)
# print(personel1.maas)
personel1.arttirMaas()
print(personel1.maas)