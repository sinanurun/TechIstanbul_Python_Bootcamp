class Calisan:

    katsayi = 5

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
    def tamad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

personel1 = Calisan("ali","demir",2500)

personel2 = Calisan ("kerim","bakir",1950)

print(Calisan.tamad(personel1))
print(Calisan.katsayi)

# Aşağıdaki kısım dersin ilk bölümünde anlatılan kısım


# print(personel1)
# print(personel1.ad,personel1.soyad,personel1.eposta)
# print(personel1.tamad())
#
# print(personel2)
# print(personel2.ad,personel2.soyad)
# print(personel2.eposta)



# class Calisan:
#     def __init__(self,ad,soyad,maas):
#         pass
#
# personel1 = Calisan("ali","demir",2500)
# personel1.ad = "ali"
# personel1.soyad = "demir"
# personel1.maas = 2500
#
# personel2 = Calisan()
# personel2.ad = "kerim"
# personel2.soyad = "bakir"
# personel2.maas = 1950
#
#
# print(personel1)
# print(personel1.ad,personel1.soyad)
#
# print(personel2)
# print(personel2.ad,personel2.soyad)