# Palindrom Kontrolü
# Bir kelimenin palindrom olup olmadığını kontrol eden fonksiyon
# Palindrom: Tersten okunuşu da aynı olan kelimeler (örn: "kek", "madam", "ara")
# Fonksiyon, kelimenin palindrom olup olmadığını belirten bir boolean değer döndürecek
# return ile değer döndürüyor
def palindrom_mi(kelime):
    temiz_kelime = kelime.lower().replace(" ", "")
    return temiz_kelime == temiz_kelime[::-1]

# Kullanım
kelimeler = ["kek", "python", "ara", "madam"]
for kelime in kelimeler:
    durum = "palindrom" if palindrom_mi(kelime) else "palindrom değil"
    print(f"'{kelime}' {durum}")