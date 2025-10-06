#özellike yani Attributes 
"""
Örnek (instance) özellikleri: self ile tanımlanır, her nesneye özeldir.
Sınıf (class) özellikleri: Sınıf seviyesinde, tüm nesneleri kapsar.
"""

class Araba:
    tekerlek_sayisi = 4  # sınıf özelliği

class Ogrenci():
    kurs = "Python 80 Saat Bootcamp"
    fakulte = ""


print(Ogrenci().kurs)
ogr1 = Ogrenci()
ogr1.fakulte = "Siyasal Bilgiler Fakultesi"
print(ogr1.kurs, ogr1.fakulte)
ogr1.ad = "Berk"
ogr2 = Ogrenci()
ogr2.kurs = "Hobi Amaçlı Kurs"
print(ogr2.kurs)
print(Ogrenci().kurs)