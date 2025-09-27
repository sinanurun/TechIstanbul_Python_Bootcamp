# MODÜLLER - ÖRNEK 5
# Time Modülü - Zaman Gecikmeli İşlemler

import time

print("=== ZAMAN GECİKMELİ İŞLEMLER ===")

try:
    print("1: Geri Sayım Sayacı")
    print("2: İşlem Süresi Hesaplama")
    print("3: Animasyonlu Yazı")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Geri sayım sayacı
        saniye = int(input("Kaç saniyelik geri sayım? "))
        
        for i in range(saniye, 0, -1):
            print(f"⏰ {i} saniye kaldı...")
            time.sleep(1)  # 1 saniye bekle
        
        print("🎉 Zaman doldu!")
        
    elif secim == 2:
        # İşlem süresi hesaplama
        print("Bir işlemin ne kadar sürdüğünü hesaplayalım.")
        input("Başlamak için ENTER'a basın...")
        
        baslama_zamani = time.time()  # Şu anki zamanı al (saniye cinsinden)
        
        # Kullanıcıdan bir işlem yapmasını iste
        print("1'den 1000'e kadar olan sayıların toplamını hesaplıyorum...")
        toplam = 0
        for i in range(1, 1001):
            toplam += i
        
        bitis_zamani = time.time()
        gecen_sure = bitis_zamani - baslama_zamani
        
        print(f"Toplam: {toplam}")
        print(f"İşlem süresi: {gecen_sure:.3f} saniye")
        
    elif secim == 3:
        # Animasyonlu yazı
        metin = input("Animasyonlu yazmak istediğiniz metni girin: ")
        
        for harf in metin:
            print(harf, end='', flush=True)  # flush=True anında gösterim için
            time.sleep(0.1)  # Her harf arasında 0.1 saniye bekle
        
        print()  # Yeni satır
        
    else:
        print("Geçersiz seçim!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except KeyboardInterrupt:
    print("\nProgram kullanıcı tarafından durduruldu.")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Zaman işlemleri tamamlandı.")