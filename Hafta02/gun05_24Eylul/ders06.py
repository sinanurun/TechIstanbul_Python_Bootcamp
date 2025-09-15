ogrenciler = []

print("=== Öğrenci Not Takibi ===")
print("Çıkmak için 'çık' yazın")

while True:
    ad = input("Öğrenci adı: ")
    if ad == "çık":
        break
    notu = int(input(f"{ad} için not: "))
    
    ogrenci = {
        "ad": ad,
        "not": notu
    }
    ogrenciler.append(ogrenci)
    print(f"{ad} eklendi.")

print("\n--- Tüm Öğrenciler ---")
for ogr in ogrenciler:
    print(f"{ogr['ad']}: {ogr['not']}")