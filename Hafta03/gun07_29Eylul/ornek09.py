# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 6
# Matematik Oyunu

import random
import time

def toplama_sorusu():
    """Toplama sorusu oluşturur"""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return f"{a} + {b} = ?", a + b

def cikarma_sorusu():
    """Çıkarma sorusu oluşturur"""
    a = random.randint(1, 100)
    b = random.randint(1, a)  # Negatif sonuç olmaması için
    return f"{a} - {b} = ?", a - b

def carpma_sorusu():
    """Çarpma sorusu oluşturur"""
    a = random.randint(1, 20)
    b = random.randint(1, 10)
    return f"{a} × {b} = ?", a * b

def bolme_sorusu():
    """Bölme sorusu oluşturur"""
    b = random.randint(1, 10)
    a = b * random.randint(1, 10)  # Tam bölünsün
    return f"{a} ÷ {b} = ?", a // b

def matematik_oyunu():
    """Matematik oyununu başlatır"""
    print("🎯 MATEMATİK OYUNU")
    print("="*30)
    
    soru_turleri = [toplama_sorusu, cikarma_sorusu, carpma_sorusu, bolme_sorusu]
    puan = 0
    soru_sayisi = 5
    
    print(f"Toplam {soru_sayisi} soru sorulacak. Hazır mısınız?\n")
    time.sleep(1)
    
    for i in range(soru_sayisi):
        # Rastgele soru seç
        soru_fonksiyonu = random.choice(soru_turleri)
        soru_metni, dogru_cevap = soru_fonksiyonu()
        
        # Zamanlayıcı başlat
        baslama_zamani = time.time()
        
        try:
            kullanici_cevap = int(input(f"Soru {i+1}: {soru_metni} "))
            
            # Süre hesapla
            sure = time.time() - baslama_zamani
            
            if kullanici_cevap == dogru_cevap:
                # Süreye göre puan ver (ne kadar hızlıysa o kadar çok puan)
                if sure < 3:
                    puan += 10
                    print(f"✅ Mükemmel! +10 puan ({sure:.1f} saniye)")
                elif sure < 6:
                    puan += 7
                    print(f"✅ Çok iyi! +7 puan ({sure:.1f} saniye)")
                else:
                    puan += 5
                    print(f"✅ Doğru! +5 puan ({sure:.1f} saniye)")
            else:
                print(f"❌ Yanlış! Doğru cevap: {dogru_cevap}")
                
        except ValueError:
            print("❌ Geçersiz cevap! Lütfen sayı girin.")
    
    return puan

def sonuc_goruntule(puan, maksimum_puan=50):
    """Oyun sonucunu görüntüler"""
    print("\n" + "="*30)
    print("🎮 OYUN SONUCU")
    print("="*30)
    
    print(f"Toplam puan: {puan}/{maksimum_puan}")
    
    if puan == maksimum_puan:
        print("🏆 MÜKEMMEL! Tüm soruları doğru ve hızlı cevapladınız!")
    elif puan >= 35:
        print("🥇 HARİKA! Matematik becerileriniz çok iyi!")
    elif puan >= 25:
        print("🥈 İYİ! Daha fazla pratik yapabilirsiniz.")
    elif puan >= 15:
        print("🥈 ORTA! Biraz daha çalışmanız gerekiyor.")
    else:
        print("💪 PES ETMEYİN! Daha çok pratik yapın.")

# Ana program
try:
    while True:
        print("\n1: Oyunu Başlat")
        print("2: Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            puan = matematik_oyunu()
            sonuc_goruntule(puan)
        elif secim == '2':
            print("Oyun sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim!")
            
except KeyboardInterrupt:
    print("\n\nOyun kullanıcı tarafından durduruldu.")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Matematik oyunu kapatıldı.")