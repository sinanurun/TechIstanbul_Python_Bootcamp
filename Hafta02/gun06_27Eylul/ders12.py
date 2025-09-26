# Çarpım tablosu oluşturma
#list comprehension ile 1'den 3'e kadar olan sayıların çarpım tablosu
carpim_tablosu = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Çarpım Tablosu:")
for satir in carpim_tablosu:
    print(satir)