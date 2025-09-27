# MODÜLLER - ÖRNEK 2
# Random Modülü - Şans Oyunları

import random

print("=== ŞANS OYUNLARI ===")

try:
    print("1: Zar Atma")
    print("2: Sayı Tahmin Oyunu")
    print("3: Şanslı Numara Çekilişi")
    print("4: Kelime Karıştırıcı")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Zar atma
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        print(f"Zar 1: {zar1}, Zar 2: {zar2}")
        print(f"Toplam: {zar1 + zar2}")
        
    elif secim == 2:
        # Sayı tahmin oyunu
        gizli_sayi = random.randint(1, 100)
        hak = 5
        
        print("1-100 arası bir sayı tuttum. Tahmin et!")
        
        for deneme in range(1, hak + 1):
            tahmin = int(input(f"{deneme}. tahmininiz: "))
            
            if tahmin == gizli_sayi:
                print(f"Tebrikler! {deneme}. denemede bildiniz.")
                break
            elif tahmin < gizli_sayi:
                print("Daha büyük bir sayı deneyin.")
            else:
                print("Daha küçük bir sayı deneyin.")
        else:
            print(f"Maalesef bilemediniz. Sayı: {gizli_sayi}")
            
    elif secim == 3:
        # Şanslı numara çekilişi
        katilimcilar = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif"]
        print(f"Katılımcılar: {katilimcilar}")
        
        sansli_kisi = random.choice(katilimcilar)
        sansli_numara = random.randint(1000, 9999)
        
        print(f"🎉 Şanslı kişi: {sansli_kisi}")
        print(f"🎯 Şanslı numara: {sansli_numara}")
        
    elif secim == 4:
        # Kelime karıştırıcı
        kelime = input("Bir kelime girin: ").strip()
        
        if len(kelime) < 2:
            print("Kelime en az 2 harfli olmalıdır!")
        else:
            # Kelimeyi listeye çevir ve karıştır
            harfler = list(kelime)
            random.shuffle(harfler)
            karisik_kelime = ''.join(harfler)
            
            print(f"Orijinal: {kelime}")
            print(f"Karışık: {karisik_kelime}")
            
    else:
        print("Geçersiz seçim!")

except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Oyunlar bitti.")