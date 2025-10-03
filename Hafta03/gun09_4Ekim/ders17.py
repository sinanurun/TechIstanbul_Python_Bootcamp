import os


# bulunduğun klasörü garantiye almak için
current_dir = os.path.dirname(os.path.abspath(__file__))


dosya = os.path.join(current_dir, "kitaplar.txt")

def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yil = input("Yıl: ")
    with open(dosya, "a", encoding="utf-8") as f:
        f.write(f"{kitap_adi};{yazar};{yil}\n")
    print("✅ Kitap eklendi.\n")

def kitaplari_listele():
    if not os.path.exists(dosya):
        print("Henüz hiç kitap eklenmedi.\n")
        return
    with open(dosya, "r", encoding="utf-8") as f:
        kitaplar = f.readlines()
    if not kitaplar:
        print("Henüz hiç kitap yok.\n")
    else:
        print("📚 Kayıtlı Kitaplar:")
        for i, satir in enumerate(kitaplar, 1):
            kitap_adi, yazar, yil = satir.strip().split(";")
            print(f"{i}. {kitap_adi} - {yazar} ({yil})")
        print()

def kitap_ara():
    aranan = input("Aranacak kitap adı veya yazar: ")
    bulundu = False
    with open(dosya, "r", encoding="utf-8") as f:
        for i, satir in enumerate(f, 1):
            kitap_adi, yazar, yil = satir.strip().split(";")
            if aranan.lower() in kitap_adi.lower() or aranan.lower() in yazar.lower():
                print(f"{i}. {kitap_adi} - {yazar} ({yil})")
                bulundu = True
    if not bulundu:
        print("❌ Sonuç bulunamadı.\n")

def kitap_sil():
    kitap_no = int(input("Silmek istediğiniz kitap numarası: "))
    with open(dosya, "r", encoding="utf-8") as f:
        kitaplar = f.readlines()
    if 0 < kitap_no <= len(kitaplar):
        silinen = kitaplar.pop(kitap_no - 1)
        with open(dosya, "w", encoding="utf-8") as f:
            f.writelines(kitaplar)
        kitap_adi, yazar, yil = silinen.strip().split(";")
        print(f"🗑️ Silindi: {kitap_adi} - {yazar} ({yil})\n")
    else:
        print("❌ Geçersiz numara.\n")

def menu():
    while True:
        print("📘 Kitap Kayıt Sistemi")
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
