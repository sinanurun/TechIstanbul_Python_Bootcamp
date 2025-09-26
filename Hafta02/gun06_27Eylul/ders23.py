#Sözlük + List Comprehension: Değer Güncelleme
# Bir sözlük içindeki ürünlerin fiyatlarını belirli bir oranda artıran fonksiyon
# Fonksiyon, güncellenmiş fiyatları içeren yeni bir sözlük return ile döndürecek
def fiyatlari_artir(urunler, oran):
    return {urun: fiyat*(1+oran/100) for urun, fiyat in urunler.items()}

# Kullanım
urun_fiyatlari = {"elma": 5, "muz": 8, "portakal": 6}
yeni_fiyatlar = fiyatlari_artir(urun_fiyatlari, 10)  # %10 zam
print("Yeni fiyatlar:", yeni_fiyatlar)