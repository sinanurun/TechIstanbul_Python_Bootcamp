# DOSYA İŞLEMLERİ - ÖRNEK 2
# Kişisel Not Defteri Uygulaması

import datetime

def not_ekle():
    """Yeni not ekler"""
    try:
        baslik = input("Not başlığı: ")
        icerik = input("Not içeriği: ")
        
        # Tarih ve saat bilgisi
        simdi = datetime.datetime.now()
        tarih = simdi.strftime("%d/%m/%Y %H:%M")
        
        with open("not_defteri.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"[{tarih}] {baslik}\n")
            dosya.write(f"{icerik}\n")
            dosya.write("-" * 50 + "\n")
        
        print("✅ Not başarıyla eklendi!")
        
    except Exception as e:
        print(f"❌ Hata: {e}")

def notlari_listele():
    """Tüm notları listeler"""
    try:
        with open("not_defteri.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            
        if not icerik.strip():
            print("📝 Henüz hiç notunuz yok!")
            return
            
        print("\n📓 NOT DEFTERİ")
        print("=" * 60)
        print(icerik)
        
    except FileNotFoundError:
        print("❌ Not defteri bulunamadı! Önce not ekleyin.")
    except Exception as e:
        print(f"❌ Hata: {e}")

def not_ara():
    """Notlarda arama yapar"""
    try:
        arama_kelimesi = input("Aranacak kelime: ").lower()
        
        with open("not_defteri.txt", "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()
        
        bulunan_notlar = []
        mevcut_not = []
        not_bulundu = False
        
        for satir in satirlar:
            if satir.startswith("[") and "]" in satir:
                # Yeni not başlığı
                if mevcut_not and not_bulundu:
                    bulunan_notlar.extend(mevcut_not)
                mevcut_not = [satir]
                not_bulundu = arama_kelimesi in satir.lower()
            elif satir.strip() == "-" * 50:
                # Not sonu
                if not_bulundu:
                    bulunan_notlar.extend(mevcut_not)
                    bulunan_notlar.append(satir)
                mevcut_not = []
                not_bulundu = False
            elif mevcut_not:
                mevcut_not.append(satir)
                if arama_kelimesi in satir.lower():
                    not_bulundu = True
        
        if bulunan_notlar:
            print(f"\n🔍 '{arama_kelimesi}' için {len(bulunan_notlar)//3} not bulundu:")
            print("=" * 60)
            for satir in bulunan_notlar:
                print(satir, end="")
        else:
            print(f"❌ '{arama_kelimesi}' ile ilgili not bulunamadı!")
            
    except FileNotFoundError:
        print("❌ Not defteri bulunamadı!")
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana program
print("📓 KİŞİSEL NOT DEFTERİ")
print("=" * 30)

while True:
    print("\n1. Not Ekle")
    print("2. Notları Listele")
    print("3. Not Ara")
    print("4. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        not_ekle()
    elif secim == "2":
        notlari_listele()
    elif secim == "3":
        not_ara()
    elif secim == "4":
        print("👋 Not defteri kapatılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print("Not defteri uygulaması sonlandırıldı!")