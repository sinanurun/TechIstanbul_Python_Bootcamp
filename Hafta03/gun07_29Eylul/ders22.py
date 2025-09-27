# HATA YÖNETİMİ - ÖRNEK 22
# Kapsamlı Veri Yapıları Uygulaması

print("=== OKUL YÖNETİM SİSTEMİ ===")

# Okul veritabanı (iç içe veri yapıları)
okul = {
    "siniflar": {
        "9A": ["Ali", "Ayşe", "Mehmet"],
        "10B": ["Zeynep", "Can", "Elif"],
        "11C": ["Burak", "Deniz", "Cem"]
    },
    "ogretmenler": {
        "Matematik": "Ahmet Hoca",
        "Fizik": "Mehmet Hoca", 
        "Kimya": "Zeynep Hoca"
    },
    "ders_programı": [
        {"ders": "Matematik", "saat": "09:00", "sinif": "9A"},
        {"ders": "Fizik", "saat": "10:30", "sinif": "10B"},
        {"ders": "Kimya", "saat": "13:00", "sinif": "11C"}
    ]
}

try:
    print("1: Sınıf listesi görüntüle")
    print("2: Öğretmen bilgisi sorgula")
    print("3: Ders programını görüntüle")
    print("4: Öğrenci ekle")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Sınıf listelerini göster
        print("\n=== SINIF LİSTELERİ ===")
        for sinif, ogrenciler in okul["siniflar"].items():
            print(f"{sinif}: {ogrenciler}")
            
    elif secim == 2:
        # Öğretmen bilgisi sorgula
        ders_adi = input("Hangi dersin öğretmenini sorgulamak istersiniz? ").strip()
        
        if ders_adi in okul["ogretmenler"]:
            ogretmen = okul["ogretmenler"][ders_adi]
            print(f"{ders_adi} dersinin öğretmeni: {ogretmen}")
        else:
            raise KeyError("Bu ders bulunamadı!")
            
    elif secim == 3:
        # Ders programını göster
        print("\n=== DERS PROGRAMI ===")
        for ders in okul["ders_programı"]:
            print(f"{ders['saat']} - {ders['ders']} - {ders['sinif']}")
            
    elif secim == 4:
        # Yeni öğrenci ekle
        sinif_adi = input("Hangi sınıfa öğrenci eklemek istersiniz? ").strip()
        yeni_ogrenci = input("Öğrenci adı: ").strip()
        
        if sinif_adi in okul["siniflar"]:
            if yeni_ogrenci in okul["siniflar"][sinif_adi]:
                print("Bu öğrenci zaten bu sınıfta!")
            else:
                okul["siniflar"][sinif_adi].append(yeni_ogrenci)
                print(f"'{yeni_ogrenci}' {sinif_adi} sınıfına eklendi.")
                print(f"Güncel liste: {okul['siniflar'][sinif_adi]}")
        else:
            raise KeyError("Bu sınıf bulunamadı!")
            
    else:
        print("Geçersiz seçim!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except KeyError as e:
    print(f"HATA: {e}")
    if secim == 2:
        print("Mevcut dersler:", list(okul["ogretmenler"].keys()))
    elif secim == 4:
        print("Mevcut sınıflar:", list(okul["siniflar"].keys()))
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Okul yönetim sistemi kapatılıyor...")