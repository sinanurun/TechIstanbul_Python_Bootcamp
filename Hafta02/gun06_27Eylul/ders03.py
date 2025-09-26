def selamla(ad):
    print(f"selamlar {ad}, kursumuza hoşgeldiniz")

selamla('ahmett')

a = selamla("idil")
print(a, type(a)) # NoneType


# İki parametre alan ve işlem yapan fonksiyon
def topla(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {sonuc}")

topla(5, 3)
topla(10, 15)
