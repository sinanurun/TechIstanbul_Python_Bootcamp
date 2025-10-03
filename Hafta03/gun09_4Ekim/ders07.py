print("=== ALIŞVERİŞ LİSTESİ ===")
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya = bulundugum_dizin + "/" + "liste.txt"
with open(dosya, "w") as f:
    while True:
        urun = input("Ürün (bitir için 'bitir'): ")
        if urun == "bitir":
            break
        f.write(urun + "\n")  # her ürünü yeni satıra yaz

print("Liste 'liste.txt' dosyasına kaydedildi.")