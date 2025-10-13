# filter fonksiyonu bir listedeki verileri
# isdeğimiz koşula uygun şekilde filitrelemeye yarar

# bir dizi de bulunan sayılardan 3'e bölünenleri listeleyim

# def uce(liste):
#     yliste = [a for a in liste if a%3==0]
#     return yliste
# sayilar = [1,5,6,9,8,7,3,12,58]
# print(uce(sayilar))

#örneğimizi filter ile yapalım
# sayilar = [1,5,6,9,8,7,3,12,58]
# print(list(filter(lambda x: x%3 ,  sayilar)))
# print(list(filter(lambda x : x%2==0 ,sayilar)))

adlar = ["ali","veli","can","berk"]
print(list(filter(lambda x:"a" in x ,adlar)))