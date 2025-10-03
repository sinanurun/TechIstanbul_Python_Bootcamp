"""
JSON bize şu avantajı sağlar:

Daha düzenli saklama (listeler, sözlükler).

Daha kolay veri manipülasyonu.

İleride başka uygulamalarla kolay entegrasyon.
"""

import json
import os


# bulunduğun klasörü garantiye almak için
current_dir = os.path.dirname(os.path.abspath(__file__))


dosya = os.path.join(current_dir, "kitaplar.json")



# Eğer dosya yoksa boş liste ile oluştur
if not os.path.exists(dosya):
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def kitaplari_oku():
    with open(dosya, "r", encoding="utf-8") as f:
        return json.load(f)

def kitaplari_yaz(kitaplar):
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)

def kitap_ekle():
    kitap_adi = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yil = input("Yıl: ")
    kitaplar = kitaplari_oku()
    kitaplar.append({"kitap": kitap_adi, "yazar": yazar, "yil": yil})
    kitaplari_yaz(kitaplar)
    print("✅ Kitap eklendi.\n")

def kitaplari_listele():
    kitaplar = kitaplari_oku()
    if not kitaplar:
        print("Henüz hiç kitap yok.\n")
        return
    print("📚 Kayıtlı Kitaplar:")
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i}. {kitap['kitap']} - {kitap['yazar']} ({kitap['yil']})")
    print()

def kitap_ara():
    aranan = input("Aranacak kitap adı veya yazar: ")
    kitaplar = kitaplari_oku()
    bulundu = False
    for i, kitap in enumerate(kitaplar, 1):
        if (aranan.lower() in kitap["kitap"].lower() or
            aranan.lower() in kitap["yazar"].lower()):
            print(f"{i}. {kitap['kitap']} - {kitap['yazar']} ({kitap['yil']})")
            bulundu = True
    if not bulundu:
        print("❌ Sonuç bulunamadı.\n")

def kitap_sil():
    kitaplari_listele()
    kitap_no = int(input("Silmek istediğiniz kitap numarası: "))
    kitaplar = kitaplari_oku()
    if 0 < kitap_no <= len(kitaplar):
        silinen = kitaplar.pop(kitap_no - 1)
        kitaplari_yaz(kitaplar)
        print(f"🗑️ Silindi: {silinen['kitap']} - {silinen['yazar']} ({silinen['yil']})\n")
    else:
        print("❌ Geçersiz numara.\n")

def kitap_guncelle():
    kitaplari_listele()
    kitap_no = int(input("Güncellemek istediğiniz kitap numarası: "))
    kitaplar = kitaplari_oku()
    if 0 < kitap_no <= len(kitaplar):
        kitap = kitaplar[kitap_no - 1]
        print(f"🔄 Güncellenecek kitap: {kitap['kitap']} - {kitap['yazar']} ({kitap['yil']})")

        yeni_adi = input(f"Yeni kitap adı (Enter ile geç): ") or kitap["kitap"]
        yeni_yazar = input(f"Yeni yazar (Enter ile geç): ") or kitap["yazar"]
        yeni_yil = input(f"Yeni yıl (Enter ile geç): ") or kitap["yil"]

        kitaplar[kitap_no - 1] = {
            "kitap": yeni_adi,
            "yazar": yeni_yazar,
            "yil": yeni_yil
        }
        kitaplari_yaz(kitaplar)
        print("✅ Kitap güncellendi.\n")
    else:
        print("❌ Geçersiz numara.\n")

def menu():
    while True:
        print("📘 Kitap Kayıt Sistemi (JSON)")
        print("1. Kitap ekle")
        print("2. Kitapları listele")
        print("3. Kitap ara")
        print("4. Kitap sil")
        print("5. Kitap güncelle")
        print("6. Çıkış")
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
            kitap_guncelle()
        elif secim == "6":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("❌ Hatalı seçim, tekrar deneyin.\n")

if __name__ == "__main__":
    menu()
