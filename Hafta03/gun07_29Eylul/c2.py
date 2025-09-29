# Kullanıcıdan yaş ve isim al. Geçerli girdi değilse uyarı ver, ama program çökmesin.

print("=== KULLANICI KAYIT SİSTEMİ ===")

while True:
    try:
        isim = input("İsminiz: ")
        if len(isim) < 2:
            raise ValueError("İsim en az 2 harf olmalı.")
        
        yas = int(input("Yaşınız: "))
        if yas < 0 or yas > 150:
            raise ValueError("Yaş 0-150 arasında olmalı.")
        
    except ValueError as e:
        print("❌ Hata:", e)
    
    else:
        print(f"✅ Hoş geldin, {isim}! ({yas} yaşında)")
        break  # doğruysa döngüden çık
    
    finally:
        print("---")