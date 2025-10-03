# DOSYA İŞLEMLERİ - ÖRNEK 3
# Öğrenci Kayıt Sistemi (CSV)

import csv
import os

def ogrenci_ekle():
    """Yeni öğrenci ekler"""
    try:
        ogrenci_no = input("Öğrenci No: ")
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        bolum = input("Bölüm: ")
        not_ort = float(input("Not Ortalaması: "))
        
        # CSV dosyasına ekle (dosya yoksa oluştur)
        dosya_var = os.path.exists("ogrenciler.csv")
        
        with open("ogrenciler.csv", "a", newline="", encoding="utf-8") as dosya:
            alanlar = ["ogrenci_no", "ad", "soyad", "bolum", "not_ort"]
            yazici = csv.DictWriter(dosya, fieldnames=alanlar)
            
            # Dosya yoksa başlık yaz
            if not dosya_var:
                yazici.writeheader()
            
            # Öğrenciyi yaz
            yazici.writerow({
                "ogrenci_no": ogrenci_no,
                "ad": ad,
                "soyad": soyad,
                "bolum": bolum,
                "not_ort": not_ort
            })
        
        print("✅ Öğrenci başarıyla eklendi!")
        
    except ValueError:
        print("❌ Hata: Not ortalaması sayı olmalıdır!")
    except Exception as e:
        print(f"❌ Hata: {e}")

def ogrenci_listele():
    """Tüm öğrencileri listeler"""
    try:
        with open("ogrenciler.csv", "r", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)
            ogrenciler = list(okuyucu)
        
        if not ogrenciler:
            print("📝 Henüz hiç öğrenci kaydı yok!")
            return
        
        print(f"\n🎓 ÖĞRENCİ LİSTESİ ({len(ogrenciler)} öğrenci)")
        print("=" * 80)
        print(f"{'No':<10} {'Ad':<15} {'Soyad':<15} {'Bölüm':<20} {'Not Ort':<10}")
        print("-" * 80)
        
        for ogrenci in ogrenciler:
            print(f"{ogrenci['ogrenci_no']:<10} {ogrenci['ad']:<15} {ogrenci['soyad']:<15} "
                  f"{ogrenci['bolum']:<20} {ogrenci['not_ort']:<10}")
                  
    except FileNotFoundError:
        print("❌ Öğrenci dosyası bulunamadı! Önce öğrenci ekleyin.")
    except Exception as e:
        print(f"❌ Hata: {e}")

def bolume_gore_listele():
    """Bölüme göre öğrencileri listeler"""
    try:
        bolum_adi = input("Bölüm adı: ")
        
        with open("ogrenciler.csv", "r", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)
            ogrenciler = [o for o in okuyucu if o['bolum'].lower() == bolum_adi.lower()]
        
        if not ogrenciler:
            print(f"❌ '{bolum_adi}' bölümünde öğrenci bulunamadı!")
            return
        
        print(f"\n🎓 {bolum_adi.upper()} BÖLÜMÜ ÖĞRENCİLERİ ({len(ogrenciler)} öğrenci)")
        print("=" * 60)
        
        for ogrenci in ogrenciler:
            print(f"{ogrenci['ad']} {ogrenci['soyad']} - {ogrenci['not_ort']}")
                  
    except FileNotFoundError:
        print("❌ Öğrenci dosyası bulunamadı!")
    except Exception as e:
        print(f"❌ Hata: {e}")

def istatistikler():
    """Öğrenci istatistiklerini gösterir"""
    try:
        with open("ogrenciler.csv", "r", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)
            ogrenciler = list(okuyucu)
        
        if not ogrenciler:
            print("❌ İstatistik hesaplanamıyor (öğrenci yok)!")
            return
        
        # İstatistikleri hesapla
        toplam_ogrenci = len(ogrenciler)
        not_ortalamalari = [float(o['not_ort']) for o in ogrenciler]
        ortalama_not = sum(not_ortalamalari) / toplam_ogrenci
        en_basarili = max(ogrenciler, key=lambda x: float(x['not_ort']))
        
        # Bölüm dağılımı
        bolumler = {}
        for ogrenci in ogrenciler:
            bolum = ogrenci['bolum']
            bolumler[bolum] = bolumler.get(bolum, 0) + 1
        
        print("\n📊 ÖĞRENCİ İSTATİSTİKLERİ")
        print("=" * 40)
        print(f"Toplam öğrenci: {toplam_ogrenci}")
        print(f"Genel not ortalaması: {ortalama_not:.2f}")
        print(f"En başarılı öğrenci: {en_basarili['ad']} {en_basarili['soyad']} - {en_basarili['not_ort']}")
        
        print("\nBölüm Dağılımı:")
        for bolum, sayi in bolumler.items():
            print(f"  {bolum}: {sayi} öğrenci")
                  
    except FileNotFoundError:
        print("❌ Öğrenci dosyası bulunamadı!")
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana program
print("🎓 ÖĞRENCİ KAYIT SİSTEMİ")
print("=" * 30)

while True:
    print("\n1. Öğrenci Ekle")
    print("2. Tüm Öğrencileri Listele")
    print("3. Bölüme Göre Listele")
    print("4. İstatistikler")
    print("5. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrenci_listele()
    elif secim == "3":
        bolume_gore_listele()
    elif secim == "4":
        istatistikler()
    elif secim == "5":
        print("👋 Sistem kapatılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print("Öğrenci kayıt sistemi sonlandırıldı!")