def selamla():
    isim = input("adınızı giriniz")
    print(f"selamlar {isim}, kursumuza hoşgeldiniz")
    return isim

a = selamla()
print(a, type(a)) # string

# return ile değer döndüren fonksiyon
def carp(sayi1, sayi2):
    return sayi1 * sayi2

# Sonucu değişkene kaydetme
sonuc = carp(4, 5)
print("Çarpım sonucu:", sonuc)


# Tek parametre alan ve işlem yapan fonksiyon
# Kare alma fonksiyonu return ile   değer döndürüyor
def kare_al(sayi):
    return sayi ** 2

# Kullanım
print("5'in karesi:", kare_al(5))
print("8'in karesi:", kare_al(8))


def yas_hesapla(dogum_yili):
    from datetime import datetime
    su_an = datetime.now().year
    return su_an - dogum_yili

# Kullanım
print("2000 doğumlu kişi:", yas_hesapla(2000), "yaşında")