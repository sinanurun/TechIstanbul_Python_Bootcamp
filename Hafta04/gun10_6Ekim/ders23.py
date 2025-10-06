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

    # def arttirMaas(self,oran):
    #     # self.maas = self.maas*1.05
    #     self.maas = self.maas * float(oran)
    def arttirMaas(self):
        # self.maas = self.maas*1.05
        # self.maas = self.maas * self.zam_orani
        self.maas *= Calisan.zam_orani

print(Calisan.per_say)
personel1 = Calisan("Veysel","Can",75000)
print(Calisan.per_say)
personel2 = Calisan("Berkay","Canan",75500)
print(Calisan.per_say)
# personel1.arttirMaas(1.1)
# print(personel1.maas)
personel1.arttirMaas()
print(personel1.maas)