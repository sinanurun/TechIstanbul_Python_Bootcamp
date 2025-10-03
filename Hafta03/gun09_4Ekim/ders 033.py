import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "ornek.txt"

# Dosyaya yazma
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write("Merhaba Dünya!\n")
    dosya.write("Python öğreniyorum.\n")

# Dosyadan okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    # Tüm içeriği oku
    tum_icerik = dosya.read()
    print("Tüm içerik:")
    print(tum_icerik)

# Satır satır okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    print("\nSatır satır okuma:")
    for satir in dosya:
        print(satir.strip())  # strip() ile boşlukları temizle

# Tüm satırları liste olarak okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()
    print(f"\nToplam {len(satirlar)} satır:")
    for i, satir in enumerate(satirlar, 1):
        print(f"{i}. {satir.strip()}")