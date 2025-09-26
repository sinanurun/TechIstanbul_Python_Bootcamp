# Çoklu parametre alan ve işlem yapan fonksiyon
# İstediğimiz kadar sayı alıp toplayan fonksiyon
def topla_cok(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

# Kullanım
print("Toplam:", topla_cok(1, 2, 3))
print("Toplam:", topla_cok(10, 20, 30, 40, 50))


# İstediğimiz kadar sayı alıp ortalamasını hesaplayan fonksiyon
def ortalama(*args):
    print(args, type(args))
    print(*args)
    toplam = 0
    for i in args:
        toplam += i
    sonuc = toplam / len(args)
    return sonuc

sortalama = ortalama(1,2,3,4,6,5)
print(sortalama)

# İstediğimiz kadar sayı alıp ortalamasını hesaplayan fonksiyon - kısayol
def ortalama_hesapla(*notlar):
    if len(notlar) == 0:
        return 0
    return sum(notlar) / len(notlar)

# Kullanım
print("Ortalama:", ortalama_hesapla(70, 80, 90, 100))
print("Ortalama:", ortalama_hesapla(50, 60, 70))