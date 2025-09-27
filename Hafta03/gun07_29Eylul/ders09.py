# HATA YÖNETİMİ - ÖRNEK 9
# raise ile Kendi Hatamızı Oluşturma

print("=== YAŞ KONTROLÜ ===")

try:
    # Kullanıcıdan yaş al
    yas = int(input("Yaşınızı girin: "))
    
    # Yaş kontrolü yap
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")
    elif yas < 18:
        raise Exception("18 yaşından küçükler bu işlemi yapamaz!")
    elif yas > 120:
        raise Exception("Geçerli bir yaş girin!")
    
    print("İşleme devam ediliyor...")
    
except ValueError as ve:
    print(f"Sayı hatası: {ve}")
except Exception as e:
    print(f"Hata: {e}")

print("Kontrol tamamlandı.")