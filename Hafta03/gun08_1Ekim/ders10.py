# MODÜLLER - ÖRNEK 10
# Çoklu Modül Kullanımı - Hava Durumu Simülasyonu
# Math, Random, Datetime Modülleri kullanılarak basit bir hava durumu simülasyonu yapılacak
# Rastgele şehirler için hava durumu, sıcaklık, nem ve rüzgar hızı üretilecek
#  Ayrıca bazı matematiksel analizler yapılacak ve sonuçlar gösterilecek
# İstatistiksel bilgiler de sunulacak
# Hata yönetimi eklenecek


import random
import datetime
import math

print("=== HAVA DURUMU SİMÜLASYONU ===")

try:
    # Hava durumu verileri
    sehirler = ["İstanbul", "Ankara", "İzmir", "Antalya", "Trabzon"]
    hava_durumlari = ["Güneşli", "Bulutlu", "Yağmurlu", "Karlı", "Rüzgarlı"]
    
    # Hava sıcaklıkları (mevsime göre)
    mevsimler = {
        "İlkbahar": (10, 20),
        "Yaz": (20, 35), 
        "Sonbahar": (5, 15),
        "Kış": (-5, 10)
    }
    
    # Mevsimi belirle (basitçe aya göre)
    simdiki_ay = datetime.datetime.now().month
    if 3 <= simdiki_ay <= 5:
        mevsim = "İlkbahar"
    elif 6 <= simdiki_ay <= 8:
        mevsim = "Yaz"
    elif 9 <= simdiki_ay <= 11:
        mevsim = "Sonbahar"
    else:
        mevsim = "Kış"
    
    print(f"Mevsim: {mevsim}")
    print("=" * 40)
    
    # Her şehir için hava durumu tahmini
    for sehir in sehirler:
        # Rastgele hava durumu seç
        hava = random.choice(hava_durumlari)
        
        # Mevsime göre sıcaklık belirle
        min_sicaklik, max_sicaklik = mevsimler[mevsim]
        sicaklik = random.randint(min_sicaklik, max_sicaklik)
        
        # Hava durumuna göre sıcaklık ayarı
        if hava == "Güneşli":
            sicaklik += random.randint(2, 5)
        elif hava == "Karlı":
            sicaklik -= random.randint(3, 8)
        elif hava == "Yağmurlu":
            sicaklik -= random.randint(1, 3)
        
        # Nem oranı (hava durumuna göre)
        if hava == "Yağmurlu":
            nem = random.randint(70, 95)
        elif hava == "Karlı":
            nem = random.randint(60, 80)
        else:
            nem = random.randint(30, 70)
        
        # Hissedilen sıcaklık (nem ve rüzgar etkisi)
        if hava == "Rüzgarlı":
            ruzgar_hizi = random.randint(15, 40)
            hissedilen = sicaklik - (ruzgar_hizi * 0.1)  # Rüzgar soğuk hissettirir
        else:
            ruzgar_hizi = random.randint(0, 15)
            # Nem yüksekse daha sıcak hissedilir
            hissedilen = sicaklik + (nem * 0.01)
        
        # Sonuçları göster
        print(f"🌆 {sehir}:")
        print(f"   🌡️  Sıcaklık: {sicaklik}°C")
        print(f"   💧 Nem: {nem}%")
        print(f"   💨 Rüzgar: {ruzgar_hizi} km/sa")
        print(f"   🌤️  Hava: {hava}")
        print(f"   🤔 Hissedilen: {hissedilen:.1f}°C")
        print()
    
    # Matematiksel analiz
    print("İstatistiksel Bilgiler:")
    print(f"Toplam şehir sayısı: {len(sehirler)}")
    print(f"Olası hava durumu sayısı: {len(hava_durumlari)}")
    print(f"π değeri: {math.pi:.5f}")
    print(f"e sayısı: {math.e:.5f}")

except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Hava durumu simülasyonu tamamlandı.")