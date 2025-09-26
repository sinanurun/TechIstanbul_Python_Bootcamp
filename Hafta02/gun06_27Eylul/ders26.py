# Sözlük Filtreleme
# Bir sözlük içindeki belirli bir değerin üzerindeki öğeleri filtreleyen fonksiyon
# Fonksiyon, filtrelenmiş yeni bir sözlük return ile döndürecek
#örneğin notları 50'nin üzerindeki dersleri filtreleme
def filtrele_sozluk(sozluk, esik_deger):
    return {k: v for k, v in sozluk.items() if v > esik_deger}

# Kullanım
notlar = {"Matematik": 85, "Fizik": 45, "Kimya": 90, "Biyoloji": 30}
gecti = filtrele_sozluk(notlar, 50)
print("Geçilen dersler:", gecti)