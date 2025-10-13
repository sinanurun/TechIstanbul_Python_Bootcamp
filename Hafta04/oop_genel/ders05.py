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

    def __repr__(self):
        return "Calisan('{}','{}','{}')".format(self.ad,self.soyad,self.maas)

    def __str__(self):
        return "{} , eposta : {}".format(self.tamad(),self.eposta)
    def __add__(self, other):
        return self.maas + other.maas

personel1 = Calisan("ali","demir",2500)
personel2 = Calisan("kerim","bakir",1950)

print(personel1 + personel2)

# print(5+9)
# print("ali"+"veli")

# print(int.__add__(5,9))
# print(str.__add__("ali","veli"))

# print(personel1)
# print(personel1.__repr__())
# print(repr(personel1))
# print(str(personel1))
# print(personel1.__str__())