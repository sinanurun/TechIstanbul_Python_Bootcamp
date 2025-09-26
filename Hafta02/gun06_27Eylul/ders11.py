# Kısa, tek satırlık fonksiyonlar
kare_al = lambda x: x ** 2
topla = lambda a, b: a + b

# Kullanım
print("Kare:", kare_al(5))
print("Toplam:", topla(3, 7))


# lambda fonksiyonunu sıralama işlemlerinde kullanma
ogrenciler = [("Ali", 85), ("Ayşe", 90), ("Mehmet", 75)]

# Nota göre sırala
sirali = sorted(ogrenciler, key=lambda x: x[1], reverse=True)
print("Nota göre sıralı:", sirali)



# lambda ile filtreleme
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift sayılar:", cift_sayilar)

# lambda ile liste dönüştürme
kareler = list(map(lambda x: x ** 2, sayilar))
print("Kareler:", kareler)

# lambda ile karmaşık sıralama
ogrenciler = [("Ali", 20, 85), ("Ayşe", 19, 90), ("Mehmet", 21, 75)]

# Yaşa göre sırala
yas_sirali = sorted(ogrenciler, key=lambda x: x[1])
print("Yaşa göre sıralı:", yas_sirali)

# Nota göre sırala
not_sirali = sorted(ogrenciler, key=lambda x: x[2], reverse=True)
print("Nota göre sıralı:", not_sirali)