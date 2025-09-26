#matematik işlemleri fonksiyonu
def matematik_islemleri(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"
    
    return {
        "toplam": toplam,
        "fark": fark,
        "carpim": carpim,
        "bolum": bolum
    }

# Kullanım
sonuclar = matematik_islemleri(20, 5)
for islem, sonuc in sonuclar.items():
    print(f"{islem}: {sonuc}")