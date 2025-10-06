#class tanımlama : nesnelerin şablonudur, nesnelerin hangi özelliklere ve işlevlere sahip olabileceğini belirten bir şablondur
class Araba:
    pass

araba1 = Araba()
araba2 = Araba()

class Ogrenci():
    pass

ogrenci1 = Ogrenci()
ogrenci1.ad = "Sevgi"
print(ogrenci1)
print(type(ogrenci1))
print(ogrenci1.ad)
print(ogrenci1.soyad)

ogrenci2 = Ogrenci()
print(type(ogrenci2))
ogrenci2.ad = "Neslihan"
ogrenci2.soyad = "Besparmak"
print(ogrenci2.ad, ogrenci2.soyad)