# DOSYA İŞLEMLERİ - ÖRNEK 4
# JSON ile Ayarlar Yöneticisi

import json
import os

# Varsayılan ayarlar
VARSAYILAN_AYARLAR = {
    "dil": "turkce",
    "tema": "koyu",
    "bildirimler": True,
    "otomatik_kaydet": False,
    "kaydetme_araligi": 5,
    "son_kullanici": None
}

def ayarlari_yukle():
    """Ayarları JSON dosyasından yükler"""
    try:
        if os.path.exists("ayarlar.json"):
            with open("ayarlar.json", "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        else:
            # Dosya yoksa varsayılan ayarları kaydet ve döndür
            ayarlari_kaydet(VARSAYILAN_AYARLAR)
            return VARSAYILAN_AYARLAR
    except Exception as e:
        print(f"❌ Ayarlar yüklenirken hata: {e}")
        return VARSAYILAN_AYARLAR

def ayarlari_kaydet(ayarlar):
    """Ayarları JSON dosyasına kaydeder"""
    try:
        with open("ayarlar.json", "w", encoding="utf-8") as dosya:
            json.dump(ayarlar, dosya, ensure_ascii=False, indent=4)
        print("✅ Ayarlar başarıyla kaydedildi!")
    except Exception as e:
        print(f"❌ Ayarlar kaydedilirken hata: {e}")

def ayarlari_goster(ayarlar):
    """Mevcut ayarları gösterir"""
    print("\n⚙️  MEVCUT AYARLAR")
    print("=" * 40)
    
    for anahtar, deger in ayarlar.items():
        if isinstance(deger, bool):
            durum = "✅ Açık" if deger else "❌ Kapalı"
            print(f"{anahtar:<20}: {durum}")
        else:
            print(f"{anahtar:<20}: {deger}")

def ayar_degistir(ayarlar):
    """Belirli bir ayarı değiştirir"""
    try:
        print("\nMevcut ayarlar:")
        for i, anahtar in enumerate(ayarlar.keys(), 1):
            print(f"{i}. {anahtar}")
        
        secim = input("\nDeğiştirmek istediğiniz ayarın adını girin: ")
        
        if secim not in ayarlar:
            print("❌ Geçersiz ayar adı!")
            return
        
        mevcut_deger = ayarlar[secim]
        print(f"Mevcut değer: {mevcut_deger} ({type(mevcut_deger).__name__})")
        
        if isinstance(mevcut_deger, bool):
            # Boolean değer için
            yeni_deger = not mevcut_deger
            print(f"Yeni değer: {yeni_deger}")
            
        elif isinstance(mevcut_deger, int):
            # Integer değer için
            yeni_deger = int(input("Yeni değer: "))
            
        elif isinstance(mevcut_deger, float):
            # Float değer için
            yeni_deger = float(input("Yeni değer: "))
            
        else:
            # String değer için
            yeni_deger = input("Yeni değer: ")
        
        ayarlar[secim] = yeni_deger
        ayarlari_kaydet(ayarlar)
        
    except ValueError:
        print("❌ Geçersiz değer tipi!")
    except Exception as e:
        print(f"❌ Hata: {e}")

def ayarlari_sifirla():
    """Ayarları varsayılana sıfırlar"""
    try:
        onay = input("Tüm ayarlar varsayılana sıfırlanacak. Emin misiniz? (e/h): ")
        if onay.lower() == 'e':
            ayarlari_kaydet(VARSAYILAN_AYARLAR)
            print("✅ Ayarlar varsayılana sıfırlandı!")
            return VARSAYILAN_AYARLAR
        else:
            print("İşlem iptal edildi.")
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana program
print("⚙️  AYARLAR YÖNETİCİSİ")
print("=" * 30)

# Ayarları yükle
ayarlar = ayarlari_yukle()

while True:
    print("\n1. Ayarları Göster")
    print("2. Ayar Değiştir")
    print("3. Ayarları Sıfırla")
    print("4. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        ayarlari_goster(ayarlar)
    elif secim == "2":
        ayar_degistir(ayarlar)
        # Ayarları yeniden yükle
        ayarlar = ayarlari_yukle()
    elif secim == "3":
        ayarlar = ayarlari_sifirla()
    elif secim == "4":
        print("👋 Ayarlar yöneticisi kapatılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print("Ayarlar yöneticisi sonlandırıldı!")