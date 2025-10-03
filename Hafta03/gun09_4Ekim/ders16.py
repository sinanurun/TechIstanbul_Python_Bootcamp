import os
aranan = "python"
bulunan_satirlar = []

# bulunduğun klasörü garantiye almak için
current_dir = os.path.dirname(os.path.abspath(__file__))
belge_yolu = os.path.join(current_dir, "belge.txt")
sonuc_yolu = os.path.join(current_dir, "sonuc.txt")


with open(belge_yolu, "r", encoding="utf-8") as f:
    for num, satir in enumerate(f, 1):
        if aranan.lower() in satir.lower():   # büyük/küçük harf duyarsız
            bulunan_satirlar.append(f"{num}. satır: {satir.strip()}")

with open(sonuc_yolu, "w", encoding="utf-8") as f:
    f.write(f"'{aranan}' için sonuçlar:\n")
    if bulunan_satirlar:
        f.write("\n".join(bulunan_satirlar))
    else:
        f.write("Hiç sonuç bulunamadı.")