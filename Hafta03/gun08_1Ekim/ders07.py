# MODÜLLER - ÖRNEK 7
# Random ve Math Birleşimi - Matematik Testi

import random
import math

print("=== MATEMATİK BECERİ TESTİ ===")

try:
    puan = 0
    soru_sayisi = 5
    
    print(f"Toplam {soru_sayisi} soru sorulacak. Hazır mısınız?\n")
    
    for soru_no in range(1, soru_sayisi + 1):
        # Rastgele işlem seç
        islem_tipi = random.choice(["+", "-", "*", "/", "üs", "karekök"])
        
        if islem_tipi in ["+", "-", "*"]:
            sayi1 = random.randint(1, 20)
            sayi2 = random.randint(1, 20)
            
            if islem_tipi == "+":
                dogru_cevap = sayi1 + sayi2
                soru = f"{sayi1} + {sayi2} = ?"
            elif islem_tipi == "-":
                dogru_cevap = sayi1 - sayi2
                soru = f"{sayi1} - {sayi2} = ?"
            else:  # *
                dogru_cevap = sayi1 * sayi2
                soru = f"{sayi1} × {sayi2} = ?"
                
        elif islem_tipi == "/":
            sayi2 = random.randint(1, 10)
            sayi1 = sayi2 * random.randint(1, 10)  # Bölüm tam sayı olsun
            dogru_cevap = sayi1 // sayi2
            soru = f"{sayi1} ÷ {sayi2} = ?"
            
        elif islem_tipi == "üs":
            taban = random.randint(2, 5)
            us = random.randint(2, 4)
            dogru_cevap = math.pow(taban, us)
            soru = f"{taban} üssü {us} = ?"
            
        else:  # karekök
            sayi = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
            dogru_cevap = math.sqrt(sayi)
            soru = f"√{sayi} = ?"
        
        # Soruyu sor
        print(f"Soru {soru_no}: {soru}")
        kullanici_cevap = float(input("Cevabınız: "))
        
        # Cevabı kontrol et
        if abs(kullanici_cevap - dogru_cevap) < 0.001:  # Küçük farkları tolere et
            print("✅ Doğru!\n")
            puan += 1
        else:
            print(f"❌ Yanlış! Doğru cevap: {dogru_cevap}\n")
    
    # Sonuçları göster
    print("=" * 30)
    print("TEST SONUÇLARI")
    print("=" * 30)
    print(f"Toplam soru: {soru_sayisi}")
    print(f"Doğru cevap: {puan}")
    print(f"Başarı yüzdesi: {(puan/soru_sayisi)*100:.1f}%")
    
    if puan == soru_sayisi:
        print("🎉 Mükemmel! Tüm soruları doğru bildiniz!")
    elif puan >= soru_sayisi * 0.7:
        print("👍 Çok iyi! Matematik becerileriniz güçlü.")
    elif puan >= soru_sayisi * 0.5:
        print("👌 İyi! Daha fazla pratik yapabilirsiniz.")
    else:
        print("💪 Daha çok çalışmanız gerekiyor. Pes etmeyin!")

except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Matematik testi bitti.")