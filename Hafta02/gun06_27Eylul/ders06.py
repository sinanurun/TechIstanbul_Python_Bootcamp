def toplama(a,b):
    return a+b

def yasHesapla(dYili):
    yas = 2025 - dYili
    return yas
sonuc = toplama(5,6)



#ortalama hesaplama fonksiyonu
def ortalama_hesapla(vize, final):
    ortalama = (vize * 0.4) + (final * 0.6)
    return ortalama

# Kullanım
ogr_ortalama = ortalama_hesapla(70, 85)
print(f"Öğrenci ortalaması: {ogr_ortalama:.2f}")


#üs alma fonksiyonu
def us_al(taban, us):
    return taban ** us

# Kullanım
print("2^3 =", us_al(2, 3))
print("5^2 =", us_al(5, 2))

#daire alanı hesaplama fonksiyonu
def daire_alani(yaricap):
    pi = 3.14
    alan = pi * (yaricap ** 2)
    return alan

# Kullanım
r = 5
print(f"Yarıçapı {r} olan dairenin alanı: {daire_alani(r):.2f}")