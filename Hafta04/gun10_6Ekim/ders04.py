class Kitap():
    ad = ""
    yazar = ""
    sayfa_sayisi = 0
    basim_yili = 0
    yayin_evi = ""

kitap1 = Kitap()
kitap1.ad = "Hayvan Ciftligi"
kitap1.yazar = "George Orwell"
kitap1.sayfa_sayisi = 150
kitap1.basim_yili = 1984
kitap1.yayin_evi = "Abakus"
print(kitap1.ad)
degiskenler = vars(kitap1)
print(degiskenler)