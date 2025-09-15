carpim = 1
adet = 0
while True:
    sayi = int(input("bir sayı giriniz"))
    if sayi == 0:
        print("girilen sayı işleme tabi değil")
        continue
    carpim *= sayi
    adet += 1
    if adet == 10:
        print("Sayı girme işlemi tamamlanmıştır")
        break
print(carpim)