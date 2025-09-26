# Liste Ters Çevirme
# Bir listeyi tersine çeviren fonksiyon
# Fonksiyon, ters çevrilmiş listeyi return ile döndürecek
def liste_ters_cevir(liste):
    return liste[::-1]

# Kullanım
orijinal = [1, 2, 3, 4, 5]
ters = liste_ters_cevir(orijinal)
print("Orijinal:", orijinal)
print("Ters:", ters)