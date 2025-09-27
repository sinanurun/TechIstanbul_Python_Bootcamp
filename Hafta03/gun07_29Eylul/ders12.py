# HATA YÖNETİMİ - ÖRNEK 12
# Basit ATM Simülasyonu

print("=== ATM SİMÜLASYONU ===")

bakiye = 1000  # Başlangıç bakiyesi

while True:
    try:
        print(f"\nMevcut bakiyeniz: {bakiye}₺")
        print("1: Para Çek")
        print("2: Para Yatır")
        print("3: Çıkış")
        
        secim = int(input("Seçiminiz (1-3): "))
        
        if secim == 1:
            cekilecek_tutar = int(input("Çekilecek tutar: "))
            
            if cekilecek_tutar <= 0:
                print("HATA: Tutar pozitif olmalıdır!")
            elif cekilecek_tutar > bakiye:
                print("HATA: Yetersiz bakiye!")
            else:
                bakiye -= cekilecek_tutar
                print(f"Çekilen tutar: {cekilecek_tutar}₺")
                print(f"Yeni bakiye: {bakiye}₺")
                
        elif secim == 2:
            yatirilacak_tutar = int(input("Yatırılacak tutar: "))
            
            if yatirilacak_tutar <= 0:
                print("HATA: Tutar pozitif olmalıdır!")
            else:
                bakiye += yatirilacak_tutar
                print(f"Yatırılan tutar: {yatirilacak_tutar}₺")
                print(f"Yeni bakiye: {bakiye}₺")
                
        elif secim == 3:
            print("Çıkış yapılıyor...")
            break
            
        else:
            print("HATA: Geçersiz seçim! 1-3 arası girin.")
            
    except ValueError:
        print("HATA: Lütfen geçerli bir sayı girin!")

print("ATM işlemleri sonlandı. İyi günler!")