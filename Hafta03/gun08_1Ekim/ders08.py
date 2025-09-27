# MODÜLLER - ÖRNEK 8
# Datetime ve Time Birleşimi - Randevu Sistemi

import datetime
import time

print("=== RANDEVU SİSTEMİ ===")

try:
    randevular = []
    
    while True:
        print("\n1: Randevu Ekle")
        print("2: Randevuları Listele")
        print("3: Yaklaşan Randevular")
        print("4: Çıkış")
        
        secim = int(input("Seçiminiz: "))
        
        if secim == 1:
            # Yeni randevu ekle
            randevu_adi = input("Randevu adı: ")
            tarih_str = input("Tarih (GG/AA/YYYY): ")
            saat_str = input("Saat (SS:DD): ")
            
            # Tarih ve saati birleştir
            tarih_saat_str = f"{tarih_str} {saat_str}"
            randevu_tarihi = datetime.datetime.strptime(tarih_saat_str, "%d/%m/%Y %H:%M")
            
            # Geçmiş tarih kontrolü
            if randevu_tarihi < datetime.datetime.now():
                print("HATA: Geçmiş bir tarihe randevu ekleyemezsiniz!")
                continue
            
            randevu = {
                "adi": randevu_adi,
                "tarih": randevu_tarihi,
                "eklenme_zamani": datetime.datetime.now()
            }
            
            randevular.append(randevu)
            print(f"✅ '{randevu_adi}' randevusu eklendi.")
            
        elif secim == 2:
            # Randevuları listele
            if not randevular:
                print("Henüz randevu bulunmuyor.")
                continue
            
            print("\nTüm Randevular:")
            for i, randevu in enumerate(randevular, 1):
                kalan_zaman = randevu["tarih"] - datetime.datetime.now()
                kalan_gun = kalan_zaman.days
                kalan_saat = kalan_zaman.seconds // 3600
                
                print(f"{i}. {randevu['adi']}")
                print(f"   Tarih: {randevu['tarih'].strftime('%d/%m/%Y %H:%M')}")
                print(f"   Kalan: {kalan_gun} gün, {kalan_saat} saat")
                print()
                
        elif secim == 3:
            # Yaklaşan randevular
            simdi = datetime.datetime.now()
            yakin_randevular = []
            
            for randevu in randevular:
                if randevu["tarih"] > simdi:
                    yakin_randevular.append(randevu)
            
            if not yakin_randevular:
                print("Yaklaşan randevu bulunmuyor.")
                continue
            
            # Tarihe göre sırala
            yakin_randevular.sort(key=lambda x: x["tarih"])
            
            print("\nYaklaşan Randevular:")
            for i, randevu in enumerate(yakin_randevular[:3], 1):  # İlk 3'ü göster
                kalan_zaman = randevu["tarih"] - simdi
                kalan_dakika = kalan_zaman.total_seconds() / 60
                
                print(f"{i}. {randevu['adi']}")
                print(f"   {randevu['tarih'].strftime('%d/%m/%Y %H:%M')}")
                print(f"   {kalan_dakika:.0f} dakika kaldı")
                print()
                
        elif secim == 4:
            print("Randevu sisteminden çıkılıyor...")
            break
            
        else:
            print("Geçersiz seçim!")
            
        # 1 saniye bekle
        time.sleep(1)
        
except ValueError as e:
    print(f"HATA: Geçersiz tarih/saat formatı! {e}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Randevu sistemi kapatıldı.")