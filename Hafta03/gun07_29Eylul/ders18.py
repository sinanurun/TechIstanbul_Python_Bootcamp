# HATA YÖNETİMİ - ÖRNEK 18
# İç İçe Veri Yapıları ve Hata Yönetimi

print("=== SINIF BİLGİ SİSTEMİ ===")

sinif = [
    {"ad": "Ali", "notlar": [85, 90, 78], "devam": True},
    {"ad": "Ayşe", "notlar": [92, 88, 95], "devam": False},
    {"ad": "Mehmet", "notlar": [76, 82, 80], "devam": True}
]

print("Sınıftaki öğrenciler:")
for i, ogrenci in enumerate(sinif, 1):
    print(f"{i}. {ogrenci['ad']}")

try:
    ogrenci_no = int(input("\nHangi öğrencinin bilgilerini görmek istersiniz? (1-3): ")) - 1
    
    # Öğrenci seçimi
    if 0 <= ogrenci_no < len(sinif):
        secilen_ogrenci = sinif[ogrenci_no]
        
        print(f"\n{secilen_ogrenci['ad']} bilgileri:")
        print(f"Notlar: {secilen_ogrenci['notlar']}")
        print(f"Devam durumu: {'Evet' if secilen_ogrenci['devam'] else 'Hayır'}")
        
        # Not ortalaması hesapla
        notlar = secilen_ogrenci['notlar']
        if notlar:  # Liste boş mu kontrolü
            ortalama = sum(notlar) / len(notlar)
            print(f"Not ortalaması: {ortalama:.2f}")
        else:
            print("Not bilgisi bulunamadı.")
            
    else:
        raise IndexError("Geçersiz öğrenci numarası!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except IndexError as e:
    print(f"HATA: {e}")
except KeyError as e:
    print(f"HATA: Eksik veri - {e} anahtarı bulunamadı!")
except ZeroDivisionError:
    print("HATA: Not ortalaması hesaplanamıyor (not listesi boş)!")

print("Sorgulama tamamlandı.")