# coding=utf-8
class Kitap():
    ad = ""
    yazar = ""
    sayfa_sayisi = 0
    basim_yili = 0
    yayin_evi = ""

kitap_listesi = []
for a in range(5):
    kitap = Kitap()
    kitap.ad = input("Kitap Adı Giriniz")
    kitap_listesi.append(kitap)

for k in kitap_listesi:
    print(k.ad)