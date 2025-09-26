# Fonksiyon ile liste işleme
# Belirli bir eşik değerinden büyük olan sayıların karesini alan fonksiyon
# List comprehension kullanarak fonksiyon tanımlama ve return ile değer döndürme
def filtrele_ve_islem(sayilar, esik_deger):
    # Belirli eşik değerinden büyük sayıların karesini al
    return [x**2 for x in sayilar if x > esik_deger]

# Kullanım
sayilar = [1, 5, 10, 15, 20]
sonuc = filtrele_ve_islem(sayilar, 10)
print("10'dan büyük sayıların karesi:", sonuc)