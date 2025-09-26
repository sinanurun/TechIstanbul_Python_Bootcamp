# kwargs: key-value (anahtar-değer) çiftleri olarak fonksiyona esnek sayıda argüman geçmeyi sağlar.
# Fonksiyon tanımında **kwargs kullanılır.
# Fonksiyon içinde kwargs bir sözlük (dictionary) olarak ele alınır.
# Anahtarlar string, değerler herhangi bir veri tipi olabilir.
def ogrenci_bilgisi(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

# Kullanım
ogrenci_bilgisi(ad="Ali", yas=20, bolum="Bilgisayar")
print("---")
ogrenci_bilgisi(ad="Ayşe", sehir="Ankara", not_ort=85.5)


# *args: fonksiyona esnek sayıda pozisyonel argüman geçmeyi sağlar.
# Fonksiyon tanımında *args kullanılır.
# Fonksiyon içinde args bir demet (tuple) olarak ele alınır.
# Argümanlar herhangi bir veri tipi olabilir.
# kwargs ve *args birlikte kullanılabilir, *args önce gelmelidir.
def ogrenciKarti(*args,**kwargs):
    print(kwargs)
    print(type(kwargs))
    for bilgiler in kwargs:
        print(bilgiler, kwargs[bilgiler])
ogrenciKarti("YOK Kartı",oadi="defne",ogrenciNo=251)

# Örnek: Ürün oluşturma fonksiyonu
# İstediğimiz kadar özellik (anahtar-değer çifti) alıp bir sözlük döndüren fonksiyon
def urun_olustur(**ozellikler):
    urun = {}
    for ozellik, deger in ozellikler.items():
        urun[ozellik] = deger
    return urun

# Kullanım
laptop = urun_olustur(marka="Dell", fiyat=5000, stok=10)
print("Oluşturulan ürün:", laptop)