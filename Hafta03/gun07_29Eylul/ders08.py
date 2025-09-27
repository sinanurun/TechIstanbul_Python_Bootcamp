# HATA YÖNETİMİ - ÖRNEK 8
# finally Bloğu

print("=== KAYNAK YÖNETİMİ ===")

baglanti_acik = False

try:
    # Bağlantıyı aç (simülasyon)
    print("Bağlantı açılıyor...")
    baglanti_acik = True
    
    # Kullanıcıdan veri al
    isim = input("Adınızı girin: ")
    
    # Hata oluştur
    yas = int(input("Yaşınızı girin: "))
    
    print(f"Hoş geldiniz {isim}! Yaşınız: {yas}")
    
except ValueError:
    print("HATA: Geçerli bir yaş girin!")
    
finally:
    # Bağlantıyı kapat (her durumda)
    if baglanti_acik:
        print("Bağlantı kapatıldı.")
    print("finally bloğu çalıştı.")

print("Program sonlandı.")