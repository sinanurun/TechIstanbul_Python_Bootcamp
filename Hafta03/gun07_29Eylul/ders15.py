# HATA YÖNETİMİ - ÖRNEK 15
# Küme İşlemleri ve Hata Yönetimi

print("=== KÜME İŞLEMLERİ ===")

sayilar = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Mevcut küme: {sayilar}")

try:
    # Kullanıcıdan sayı al
    girilen_sayi = int(input("Kümeye eklemek veya çıkarmak için bir sayı girin: "))
    
    if girilen_sayi in sayilar:
        # Sayı varsa çıkar
        sayilar.remove(girilen_sayi)
        print(f"{girilen_sayi} kümeden çıkarıldı.")
    else:
        # Sayı yoksa ekle
        sayilar.add(girilen_sayi)
        print(f"{girilen_sayi} kümeye eklendi.")
    
    print(f"Güncel küme: {sayilar}")
    
    # Küme boyutunu göster
    print(f"Kümede {len(sayilar)} eleman var.")
    
except ValueError:
    print("HATA: Lütfen geçerli bir tam sayı girin!")
except KeyError:
    print("HATA: Çıkarılmak istenen sayı kümede bulunamadı!")

print("Küme işlemleri tamamlandı.")