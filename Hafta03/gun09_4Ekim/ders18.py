#CSV (Comma Separated Values) formatı daha düzenli, Excel’de de açabiliriz

import csv
import os


# bulunduğun klasörü garantiye almak için
current_dir = os.path.dirname(os.path.abspath(__file__))


dosya = os.path.join(current_dir, "kitaplar.csv")


# Başlıkları dosyaya yaz (ilk kez oluşturuluyorsa)
if not os.path.exists(dosya):
    with open(dosya, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Kitap Adı", "Yazar", "Yıl"])

def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yil = input("Yıl: ")
    with open(dosya, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([kitap_adi, yazar, yil])
    print("✅ Kitap eklendi.\n")

def kitaplari_listele():
    with open(dosya, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    if len(reader) <= 1:
        print("Henüz hiç kitap yok.\n")
        return
    print("📚 Kayıtlı Kitaplar:")
    for i, row in enumerate(reader[1:], 1):  # başlığı atla
        print(f"{i}. {row[0]} - {row[1]} ({row[2]})")
    print()

def kitap_ara():
    aranan = input("Aranacak kitap adı veya yazar: ")
    bulundu = False
    with open(dosya, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # başlığı atla
        for i, row in enumerate(reader, 1):
            if aranan.lower() in row[0].lower() or aranan.lower() in row[1].lower():
                print(f"{i}. {row[0]} - {row[1]} ({row[2]})")
                bulundu = True
    if not bulundu:
        print("❌ Sonuç bulunamadı.\n")

def kitap_sil():
    kitap_no = int(input("Silmek istediğiniz kitap numarası: "))
    with open(dosya, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    if 0 < kitap_no <= len(reader) - 1:
        silinen = reader.pop(kitap_no)  # başlık satırı index 0
        with open(dosya, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(reader)
        print(f"🗑️ Silindi: {silinen[0]} - {silinen[1]} ({silinen[2]})\n")
    else:
        print("❌ Geçersiz numara.\n")

def menu():
    while True:
        print("📘 Kitap Kayıt Sistemi (CSV)")
        print("1. Kitap ekle")
        print("2. Kitapları listele")
        print("3. Kitap ara")
        print("4. Kitap sil")
        print("5. Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_ara()
        elif secim == "4":
            kitap_sil()
        elif secim == "5":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("❌ Hatalı seçim, tekrar deneyin.\n")

if __name__ == "__main__":
    menu()
