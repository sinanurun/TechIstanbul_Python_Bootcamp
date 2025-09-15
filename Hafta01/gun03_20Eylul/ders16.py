# #versiyon 1
# sayi = int(input("bir sayı giriniz"))
# ssayi = str(sayi)
# toplam = 0
# for rakam in ssayi:
#     kup= int(rakam)**len(ssayi)
#     toplam += kup
#     print(rakam, kup, toplam)
# if toplam == sayi:
#     print(sayi,"sayisi bir armstrong sayısıdır")
#versiyon 2
for i in range(100000):
    sayi = i
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup= int(rakam)**len(ssayi)
        toplam += kup
        # print(rakam, kup, toplam)
    if toplam == sayi:
        print(sayi,"sayisi bir armstrong sayısıdır")
