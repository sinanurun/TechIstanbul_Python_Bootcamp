#List Comprehension + Fonksiyon: Filtreleme
# Bir liste içindeki çift sayıları filtreleyen fonksiyon
# Fonksiyon, çift sayılardan oluşan yeni bir liste return ile döndürece

def cift_sayilari_filtrele(sayilar):
    return [x for x in sayilar if x % 2 == 0]

# Kullanım
sayilar = list(range(1, 16))
ciftler = cift_sayilari_filtrele(sayilar)
print("1-15 arası çift sayılar:", ciftler)