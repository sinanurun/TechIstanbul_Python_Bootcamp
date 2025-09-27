# HATA YÖNETİMİ - ÖRNEK 10
# Liste İşlemleri ve Hata Yönetimi
# Bu program, bir sayı listesi üzerinde çeşitli işlemler yapar.
# Hataları yakalar ve kullanıcıya bilgi verir.
print("=== SAYI LİSTESİ İŞLEMLERİ ===")

# Sayı listesi oluştur
sayilar = [10, 20, 30, 40, 50]
print(f"Listemiz: {sayilar}")

try:
    # Kullanıcıdan işlem seç
    print("\n1: Tüm listeyi göster")
    print("2: Belirli indeksteki sayıyı göster")
    print("3: Listenin ortalamasını hesapla")
    
    secim = int(input("Seçiminiz (1-3): "))
    
    if secim == 1:
        print("Tüm liste:", sayilar)
        
    elif secim == 2:
        indeks = int(input("İndeks girin (0-4): "))
        print(f"{indeks}. indeksteki sayı: {sayilar[indeks]}")
        
    elif secim == 3:
        # Ortalama hesapla
        toplam = 0
        for sayi in sayilar:
            toplam += sayi
        ortalama = toplam / len(sayilar)
        print(f"Listenin ortalaması: {ortalama}")
        
    else:
        print("Geçersiz seçim!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except IndexError:
    print("HATA: Geçersiz indeks! 0-4 arası girin.")
except ZeroDivisionError:
    print("HATA: Liste boş, ortalama hesaplanamaz!")

print("İşlemler tamamlandı.")