# EK ÖRNEK 1: Çok Basit Hata Yakalama
print("=== BASİT HATA YAKALAMA ===")

try:
    sayi = int(input("Bir sayı girin: "))
    print(f"Girdiğiniz sayı: {sayi}")
except:
    print("Bir hata oluştu!")

print("Program bitti.")


# EK ÖRNEK 2: Sözlük Anahtar Hatası
print("=== SÖZLÜK HATASI ===")

ogrenci = {"ad": "Ali", "not": 85}

try:
    anahtar = input("Hangi bilgiyi görmek istersiniz? (ad/not/soyad): ")
    print(f"{anahtar}: {ogrenci[anahtar]}")
except KeyError:
    print("HATA: Böyle bir anahtar yok!")