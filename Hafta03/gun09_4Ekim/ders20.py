#json kütüphane örneği hata ayıklamalı hali

import json
import os


# bulunduğun klasörü garantiye almak için
current_dir = os.path.dirname(os.path.abspath(__file__))


DOSYA = os.path.join(current_dir, "kitaplar.json")


# JSON dosyası yoksa boş liste ile oluştur
if not os.path.exists(DOSYA):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def kitaplari_oku():
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

def kitaplari_yaz(kitaplar):
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(kitaplar, f, ensure_ascii=False, indent=4)

def kitap_ekle():
    try:
        ad = input("Kitap adı: ")
        yazar = input("Yazar: ")
        yil = input("Yıl: ")
        kitaplar = kitaplari_oku()
        kitaplar.append({"ad": ad, "yazar": yazar, "yil": yil})
        kitaplari_yaz(kitaplar)
        print(f"✅ '{ad}' adlı kitap eklendi.\n")
    except Exception as e:
        print("❌ Kitap eklenirken hata:", e)

def kitaplari_listele():
    kitaplar = kitaplari_oku()
    if not kitaplar:
        print("📂 Henüz kayıtlı kitap yok.")
        return []
    print("\n--- Kayıtlı Kitaplar ---")
    for i, kitap in enumerate(kitaplar, 1):
        print(f"{i}. {kitap['ad']} - {kitap['yazar']} ({kitap['yil']})")
    print()
    return kitaplar

def kitap_guncelle():
    try:
        kitaplar = kitaplari_listele()
        if not kitaplar:
            return

        secim = int(input("Güncellemek istediğiniz kitabın numarası: "))
        if 0 < secim <= len(kitaplar):
            kitap = kitaplar[secim - 1]
            print(f"🔄 Seçilen kitap: {kitap['ad']} - {kitap['yazar']} ({kitap['yil']})")

            yeni_ad = input(f"Yeni kitap adı (Enter ile geç): ") or kitap["ad"]
            yeni_yazar = input(f"Yeni yazar (Enter ile geç): ") or kitap["yazar"]
            yeni_yil = input(f"Yeni yıl (Enter ile geç): ") or kitap["yil"]

            kitaplar[secim - 1] = {"ad": yeni_ad, "yazar": yeni_yazar, "yil": yeni_yil}
            kitaplari_yaz(kitaplar)
            print("✅ Kitap güncellendi.\n")
        else:
            print("❌ Geçersiz numara.\n")
    except Exception as e:
        print("❌ Güncelleme sırasında hata:", e)

def menu():
    while True:
        print("📘 Kitap Kayıt Sistemi (JSON)")
        print("1. Kitap ekle")
        print("2. Kitapları listele")
        print("3. Kitap güncelle")
        print("4. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_guncelle()
        elif secim == "4":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("❌ Hatalı seçim, tekrar deneyin.\n")

if __name__ == "__main__":
    menu()
