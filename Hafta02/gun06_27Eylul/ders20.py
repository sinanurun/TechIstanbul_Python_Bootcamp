# En büyük sayıyı bulma
# Bir liste içindeki en büyük sayıyı bulan fonksiyon
# Fonksiyon, en büyük sayıyı return ile döndürecek
def en_buyuk_bul(sayilar):
    if not sayilar:
        return None
    return max(sayilar)

# Kullanım
liste = [15, 8, 23, 4, 42, 11]
print("En büyük sayı:", en_buyuk_bul(liste))
