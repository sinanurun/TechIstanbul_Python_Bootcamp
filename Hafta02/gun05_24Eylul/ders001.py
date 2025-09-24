#list comprehension kullanımı
# Liste Comprehension, Python'da liste oluşturmanın kısa, okunabilir ve etkili bir yoludur. 
# Tek satırda for döngüsü ve isteğe bağlı olarak koşul ifadeleri kullanarak liste oluşturmamızı sağlar.

"""
[expression for item in iterable if condition]
"""

#örnek 1: 1-10 arasındaki sayıların karelerini listele
# list comprehension kullanım amacı: daha kısa ve okunabilir kod yazmak
# geleneksel yöntem ile yapımı
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
# list comprehension ile yapımı
sayilar = [1,2,3,4,5,6,7,8,9,10]
kareler = [x**2 for x in sayilar]
print(kareler)


#örnek 2: 1-20 arasındaki çift sayıları listele
# geleneksel yöntem ile yapımı
even_numbers = []
for i in range(1,21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
# list comprehension ile yapımı
ciftler = [x for x in range(1,21) if x % 2 == 0]
print(ciftler)

#örnek 3: bir cümledeki kelimelerin uzunluklarını listele
# geleneksel yöntem ile yapımı
sentence = "Python programlama dili çok eğlencelidir"
words = sentence.split()
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)
# list comprehension ile yapımı
kelimeler = sentence.split()
uzunluklar = [len(kelime) for kelime in kelimeler]
print(uzunluklar)

# Bir listedeki tüm kelimeleri büyük harfe çevirelim
kelimeler = ["python", "programlama", "liste", "comprehension"]
buyuk_harfler = [kelime.upper() for kelime in kelimeler]
print(buyuk_harfler)  # ['PYTHON', 'PROGRAMLAMA', 'LİSTE', 'COMPREHENSION']

# İki listeyi çarpraz şekilde birleştirelim
liste1 = ['a', 'b', 'c']
liste2 = [1, 2, 3]
birlesim = [(harf, sayi) for harf in liste1 for sayi in liste2]
print(birlesim)  # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

# Bir string'deki sesli harfleri bulalım
metin = "Python Programlama Dili"
sesliler = [harf for harf in metin if harf.lower() in 'aeıioöuü']
print(sesliler)  # ['o', 'o', 'a', 'a', 'a', 'i', 'i']

# Çarpım tablosu (1'den 3'e kadar)
carpim_tablosu = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
print(carpim_tablosu)
# ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', '3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9']


# Sayıları "Çift" veya "Tek" olarak etiketleyelim
sayilar = [1, 2, 3, 4, 5, 6]
etiketler = ["Çift" if x % 2 == 0 else "Tek" for x in sayilar]
print(etiketler)  # ['Tek', 'Çift', 'Tek', 'Çift', 'Tek', 'Çift']

# 3x3'lük bir matris oluşturalım
matris = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matris)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

"""
Liste Comprehension Avantajları:
Okunabilirlik: Kod daha kısa ve anlaşılır

Performans: Genellikle normal döngülerden daha hızlı

Pythonic: Python programlama stilinde tercih edilen bir yöntem

Dikkat Edilmesi Gerekenler:
Çok karmaşık logic'ler için normal döngüler daha okunabilir olabilir

Çok uzun liste comprehension'lar okunmayı zorlaştırabilir

Liste Comprehension, Python'da veri işleme ve liste manipülasyonunda sıkça kullanılan güçlü bir araçtır! 

"""