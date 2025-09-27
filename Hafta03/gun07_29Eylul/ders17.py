# HATA YÖNETİMİ - ÖRNEK 17
# Liste Metotları ve Hata Yönetimi

print("=== AKILLI ALIŞVERİŞ LİSTESİ ===")

alisveris_listesi = ["elma", "ekmek", "süt"]
print(f"Mevcut liste: {alisveris_listesi}")

while True:
    try:
        print("\n1: Ürün ekle")
        print("2: Ürün çıkar")
        print("3: Listeyi göster")
        print("4: Ürün ara")
        print("5: Çıkış")
        
        secim = int(input("Seçiminiz: "))
        
        if secim == 1:
            # Ürün ekle
            yeni_urun = input("Eklemek istediğiniz ürün: ").strip().lower()
            
            if not yeni_urun:
                raise ValueError("Ürün adı boş olamaz!")
            
            if yeni_urun in alisveris_listesi:
                print("Bu ürün zaten listede var!")
            else:
                alisveris_listesi.append(yeni_urun)
                print(f"'{yeni_urun}' listeye eklendi.")
                
        elif secim == 2:
            # Ürün çıkar
            if not alisveris_listesi:
                print("Liste zaten boş!")
                continue
                
            cikarilacak = input("Çıkarmak istediğiniz ürün: ").strip().lower()
            
            if cikarilacak in alisveris_listesi:
                alisveris_listesi.remove(cikarilacak)
                print(f"'{cikarilacak}' listeden çıkarıldı.")
            else:
                raise ValueError("Bu ürün listede bulunamadı!")
                
        elif secim == 3:
            # Listeyi göster
            if alisveris_listesi:
                print("\nAlışveriş Listesi:")
                for i, urun in enumerate(alisveris_listesi, 1):
                    print(f"{i}. {urun}")
            else:
                print("Liste boş!")
                
        elif secim == 4:
            # Ürün ara
            aranan = input("Aramak istediğiniz ürün: ").strip().lower()
            
            if aranan in alisveris_listesi:
                indeks = alisveris_listesi.index(aranan)
                print(f"'{aranan}' listede bulundu! ({indeks + 1}. sırada)")
            else:
                print("Ürün listede bulunamadı.")
                
        elif secim == 5:
            print("Çıkış yapılıyor...")
            break
            
        else:
            print("Geçersiz seçim! 1-5 arası girin.")
            
    except ValueError as e:
        print(f"HATA: {e}")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

print(f"Son liste: {alisveris_listesi}")