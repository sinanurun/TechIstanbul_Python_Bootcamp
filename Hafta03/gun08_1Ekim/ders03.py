# MODÜLLER - ÖRNEK 3
# Datetime Modülü - Zaman Hesaplamaları

import datetime

print("=== ZAMAN HESAPLAMALARI ===")

try:
    # Şu anki zamanı al
    simdi = datetime.datetime.now()
    print(f"Şu anki tarih ve saat: {simdi}")
    print(f"Tarih: {simdi.date()}")
    print(f"Saat: {simdi.time()}")
    print(f"Yıl: {simdi.year}")
    print(f"Ay: {simdi.month}")
    print(f"Gün: {simdi.day}")
    print(f"Saat: {simdi.hour}")
    print(f"Dakika: {simdi.minute}")
    
    # Doğum günü hesaplama
    dogum_yili = int(input("\nDoğum yılınızı girin: "))
    dogum_ayi = int(input("Doğum ayınızı girin: "))
    dogum_gunu = int(input("Doğum gününüzü girin: "))
    
    dogum_tarihi = datetime.date(dogum_yili, dogum_ayi, dogum_gunu)
    bugun = datetime.date.today()
    
    # Yaş hesaplama
    yas = bugun.year - dogum_tarihi.year
    
    # Doğum günü henüz gelmediyse 1 yaş eksik say
    if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
        yas -= 1
    
    print(f"Yaşınız: {yas}")
    
    # Doğum gününe kalan gün sayısı
    bu_yil_dogum_gunu = datetime.date(bugun.year, dogum_ayi, dogum_gunu)
    
    if bu_yil_dogum_gunu < bugun:
        gelecek_yil_dogum_gunu = datetime.date(bugun.year + 1, dogum_ayi, dogum_gunu)
        kalan_gun = (gelecek_yil_dogum_gunu - bugun).days
    else:
        kalan_gun = (bu_yil_dogum_gunu - bugun).days
    
    print(f"Doğum gününüze kalan gün sayısı: {kalan_gun}")
    
    # Haftanın günü hesaplama
    haftanin_gunleri = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    dogum_gunu_adi = haftanin_gunleri[dogum_tarihi.weekday()]
    print(f"Doğduğunuz gün: {dogum_gunu_adi}")

except ValueError as e:
    print(f"HATA: Geçersiz tarih! {e}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Zaman hesaplamaları tamamlandı.")