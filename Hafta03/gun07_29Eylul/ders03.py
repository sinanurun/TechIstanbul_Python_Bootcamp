# HATA YÖNETİMİ - ÖRNEK 3
# Liste İndeks Hatası

print("=== MEYVE LİSTESİ ===")

# Meyve listesi oluştur
meyveler = ["elma", "armut", "çilek", "muz", "portakal"]
print(f"Meyveler: {meyveler}")

try:
    # Kullanıcıdan indeks al
    indeks = int(input("Hangi meyveyi görmek istersiniz? (0-4): "))
    
    # Listeden meyveyi al
    secilen_meyve = meyveler[indeks]
    
    print(f"Seçilen meyve: {secilen_meyve}")
    
except ValueError:
    print("HATA: Lütfen bir sayı girin! (0, 1, 2, 3, 4)")
except IndexError:
    print(f"HATA: Geçersiz numara! Sadece 0-{len(meyveler)-1} arası girebilirsiniz.")

print("İşlem tamamlandı.")