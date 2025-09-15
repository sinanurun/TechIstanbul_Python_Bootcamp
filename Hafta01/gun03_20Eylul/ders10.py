carpim = 1
adet = 0
while True:
    sayi = int(input("bir sayı giriniz"))
    if sayi == 0:
        continue
    carpim = carpim*sayi
    adet = adet + 1
    if adet == 10 :
        print("10 adet 0'dan farklı sayı girişi tamamlandı")
        print("Çarpımları sonucu",carpim)
        break