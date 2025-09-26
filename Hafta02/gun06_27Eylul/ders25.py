# Sözlük Anahtar-Değer Değiştirme
# Bir sözlük içindeki anahtar ve değerleri yer değiştiren fonksiyon
# Fonksiyon, yeni oluşturulan sözlüğü return ile döndürecek
def anahtar_deger_degistir(sozluk):
    return {deger: anahtar for anahtar, deger in sozluk.items()}

# Kullanım
renkler = {"kırmızı": "#FF0000", "yeşil": "#00FF00", "mavi": "#0000FF"}
ters_renkler = anahtar_deger_degistir(renkler)
print("Ters çevrilmiş:", ters_renkler)