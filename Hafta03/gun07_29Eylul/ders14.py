# HATA YÖNETİMİ - ÖRNEK 14
# Sözlük Anahtar Kontrolü

print("=== ÖĞRENCİ BİLGİ SİSTEMİ ===")

ogrenci = {
    "ad": "Ayşe",
    "yas": 20,
    "not": 85,
    "bolum": "Bilgisayar Mühendisliği"
}

print("Mevcut anahtarlar:", list(ogrenci.keys()))

try:
    # Kullanıcıdan anahtar iste
    anahtar = input("Hangi bilgiyi görmek istersiniz? ").strip().lower()
    
    # Anahtar var mı kontrol et
    if anahtar not in ogrenci:
        raise KeyError(f"'{anahtar}' anahtarı bulunamadı!")
    
    # Değeri göster
    deger = ogrenci[anahtar]
    print(f"{anahtar}: {deger}")
    
except KeyError as e:
    print(f"HATA: {e}")
    print("Mevcut anahtarlar:", list(ogrenci.keys()))
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Sorgulama tamamlandı.")