fiyatlar = {"elma": 8, "muz":12, "armut": 9}

toplam = 0

for fiyat in fiyatlar.values():
    toplam += fiyat

print("toplam tutar", toplam)


#oguz

urunler = []
print("=== Pazar Listesi ===")
print("Çıkmak için 'bitir' yazın")
toplam = 0
while True:
    ad = input("Ürün adı: ")
    if ad == "bitir":
        break
    
    fiyat = float(input("Fiyat (TL): "))
    
    urun = {
        "ad": ad,
        "fiyat": fiyat,
    }
    urunler.append(urun)
    print(f"'{ad}' sisteme eklendi.\n")
    toplam +=fiyat
    
print("\n--- Tüm Ürünler ---")
for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']} TL,]")

print(f"Toplam harcamanız :{toplam} TL")


#onur

items = {}

print("enter your items and prices")
print("to exit press Q")
while True:
    name = input('Enter item name: ')
    if name.upper() == 'Q':
        break
    else:
        price = float(input('Enter item price: '))
    items[name] = price
print(items)
total_price = sum(items.values())