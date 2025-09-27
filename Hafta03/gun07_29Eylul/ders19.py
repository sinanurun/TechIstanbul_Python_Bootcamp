# HATA YÖNETİMİ - ÖRNEK 19
# Küme İşlemleri ve Matematiksel Hatalar

print("=== SAYI KÜMELERİ İŞLEMLERİ ===")

tek_sayilar = {1, 3, 5, 7, 9}
cift_sayilar = {2, 4, 6, 8, 10}
asal_sayilar = {2, 3, 5, 7}

print(f"Tek sayılar: {tek_sayilar}")
print(f"Çift sayılar: {cift_sayilar}")
print(f"Asal sayılar: {asal_sayilar}")

try:
    # Kullanıcıdan işlem seç
    print("\n1: Birleşim")
    print("2: Kesişim")
    print("3: Fark")
    print("4: Küme ekle")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Birleşim işlemi
        birlesim = tek_sayilar.union(cift_sayilar)
        print(f"Tek ve çift sayıların birleşimi: {birlesim}")
        
    elif secim == 2:
        # Kesişim işlemi
        kesisim = tek_sayilar.intersection(asal_sayilar)
        print(f"Tek ve asal sayıların kesişimi: {kesisim}")
        
    elif secim == 3:
        # Fark işlemi
        fark = asal_sayilar.difference(tek_sayilar)
        print(f"Asal sayılardan tek sayıların farkı: {fark}")
        
    elif secim == 4:
        # Küme ekle
        yeni_sayi = int(input("Kümelere eklemek için bir sayı girin: "))
        
        # Sayı tipine göre uygun kümeye ekle
        if yeni_sayi % 2 == 0:
            cift_sayilar.add(yeni_sayi)
            print(f"{yeni_sayi} çift sayılar kümesine eklendi.")
        else:
            tek_sayilar.add(yeni_sayi)
            print(f"{yeni_sayi} tek sayılar kümesine eklendi.")
            
        # Asal sayı kontrolü (basit)
        if yeni_sayi > 1 and all(yeni_sayi % i != 0 for i in range(2, int(yeni_sayi**0.5) + 1)):
            asal_sayilar.add(yeni_sayi)
            print(f"{yeni_sayi} asal sayılar kümesine eklendi.")
            
        print(f"\nGüncel kümeler:")
        print(f"Tek sayılar: {tek_sayilar}")
        print(f"Çift sayılar: {cift_sayilar}")
        print(f"Asal sayılar: {asal_sayilar}")
        
    else:
        print("Geçersiz seçim!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Küme işlemleri tamamlandı.")