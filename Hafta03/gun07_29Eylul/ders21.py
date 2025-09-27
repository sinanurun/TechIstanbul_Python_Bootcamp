# HATA YÖNETİMİ - ÖRNEK 21
# Liste ve Demet Performans Karşılaştırması

print("=== LİSTE vs DEMET PERFORMANSI ===")

# Sabit veriler için demet kullanıyoruz
RENKLER = ("kırmızı", "mavi", "yeşil", "sarı", "mor", "turuncu", "pembe")
print(f"Sabit renkler (demet): {RENKLER}")

# Değişebilir veriler için liste kullanıyoruz
favori_renkler = ["mavi", "yeşil", "mor"]
print(f"Favori renkler (liste): {favori_renkler}")

try:
    # Kullanıcıdan işlem seç
    print("\n1: Renk sorgula (demet)")
    print("2: Favori renk ekle (liste)")
    print("3: Favori renk çıkar (liste)")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Demetten renk sorgula
        renk_adi = input("Hangi rengi sorgulamak istersiniz? ").strip().lower()
        
        if renk_adi in RENKLER:
            indeks = RENKLER.index(renk_adi)
            print(f"'{renk_adi}' renk listemizde var! ({indeks}. sırada)")
        else:
            print("Bu renk listemizde yok.")
            
    elif secim == 2:
        # Listeye renk ekle
        yeni_renk = input("Eklemek istediğiniz rengi girin: ").strip().lower()
        
        if yeni_renk in RENKLER:
            if yeni_renk not in favori_renkler:
                favori_renkler.append(yeni_renk)
                print(f"'{yeni_renk}' favori renklerinize eklendi.")
            else:
                print("Bu renk zaten favorilerinizde var!")
        else:
            raise ValueError("Geçersiz renk! Sabit renkler listesinde yok.")
            
    elif secim == 3:
        # Listeden renk çıkar
        if not favori_renkler:
            print("Favori renk listeniz zaten boş!")
        else:
            cikarilacak = input("Çıkarmak istediğiniz rengi girin: ").strip().lower()
            
            if cikarilacak in favori_renkler:
                favori_renkler.remove(cikarilacak)
                print(f"'{cikarilacak}' favori renklerinizden çıkarıldı.")
            else:
                raise ValueError("Bu renk favori renklerinizde yok!")
                
    else:
        print("Geçersiz seçim!")
        
    # Güncel listeyi göster
    print(f"\nGüncel favori renkler: {favori_renkler}")
    
except ValueError as e:
    print(f"HATA: {e}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Renk işlemleri tamamlandı.")