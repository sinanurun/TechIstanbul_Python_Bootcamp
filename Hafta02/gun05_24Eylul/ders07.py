#Kullanıcıdan ürün adı, fiyatı ve stok miktarını al, bir listeye sözlük olarak ekle.

urunler = []

print("=== ÜRÜN STOK TAKİP ===")
print("Çıkmak için 'bitir' yazın")

while True:
    ad = input("Ürün adı: ")
    if ad == "bitir":
        break
    
    fiyat = float(input("Fiyat (TL): "))
    stok = int(input("Stok adedi: "))
    
    urun = {
        "ad": ad,
        "fiyat": fiyat,
        "stok": stok
    }
    urunler.append(urun)
    print(f"'{ad}' sisteme eklendi.\n")

print("\n--- Tüm Ürünler ---")
for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']} TL, Stok: {urun['stok']}")