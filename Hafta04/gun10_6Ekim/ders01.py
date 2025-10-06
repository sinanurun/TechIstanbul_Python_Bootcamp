#Nesne Yönelimli Programlama (OOP), gerçek dünyadaki varlıkları ve ilişkileri modellememizi sağlayan bir programlama paradigmasıdır.
"""
Yapısal programlamadan farkı: Kodun tekrar kullanılabilirliği, modülerliği ve bakım kolaylığı.
Gerçek dünya benzetimi: Nesneler → Özellikler (attributes) + Davranışlar (methods).
Python’da her şey nesnedir: int, str, list gibi tipler bile birer sınıftır.
"""


# OOP ÖNCESİ - Fonksiyonel Yaklaşım
def ogrenci_olustur(ad, yas, not_ortalamasi):
    return {"ad": ad, "yas": yas, "not_ortalamasi": not_ortalamasi}

def ogrenci_bilgileri(ogrenci):
    return f"{ogrenci['ad']}, {ogrenci['yas']} yaşında, Not: {ogrenci['not_ortalamasi']}"

# Kullanım
ogrenci1 = ogrenci_olustur("Ali", 20, 85.5)
print(ogrenci_bilgileri(ogrenci1))

# # OOP SONRASI - Nesne Yönelimli Yaklaşım
# class Ogrenci:
#     def __init__(self, ad, yas, not_ortalamasi):
#         self.ad = ad
#         self.yas = yas
#         self.not_ortalamasi = not_ortalamasi
    
#     def bilgileri_goster(self):
#         return f"{self.ad}, {self.yas} yaşında, Not: {self.not_ortalamasi}"

# # Kullanım
# ogrenci1 = Ogrenci("Ali", 20, 85.5)
# print(ogrenci1.bilgileri_goster())