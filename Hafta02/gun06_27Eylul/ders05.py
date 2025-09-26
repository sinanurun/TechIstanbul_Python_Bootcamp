def selamla(ad):
    print(f"selamlar {ad}, kursumuza hoşgeldiniz")
    if len(ad)>5:
        return True
    else:
        return False
# isim = "idil"
# a = selamla(isim)
# print(a, type(a))


# Tek parametre alan ve işlem yapan fonksiyon
# Çift mi tek mi kontrolü yapan fonksiyon
def cift_mi(sayi):
    if sayi % 2 == 0:
        return True
    else:
        return False

# Kullanım
sayi = 10
if cift_mi(sayi):
    print(f"{sayi} çift sayıdır")
else:
    print(f"{sayi} tek sayıdır")