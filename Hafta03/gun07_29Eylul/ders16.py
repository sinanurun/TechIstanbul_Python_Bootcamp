# HATA YÖNETİMİ - ÖRNEK 16
# Demet ve Liste Dönüşümü

print("=== DEMET ve LİSTE İŞLEMLERİ ===")

# Sabit veriler için demet kullanıyoruz
AYLAR = ("Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", 
         "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık")

print(f"Yılın ayları: {AYLAR}")

try:
    ay_no = int(input("Kaçıncı ayı görmek istersiniz? (1-12): "))
    
    # Demetten elemana erişim (indeks 0'dan başlar)
    if 1 <= ay_no <= 12:
        secilen_ay = AYLAR[ay_no - 1]
        print(f"{ay_no}. ay: {secilen_ay}")
        
        # Aydaki harf sayısını göster
        harf_sayisi = len(secilen_ay)
        print(f"Bu ay {harf_sayisi} harflidir.")
    else:
        raise IndexError("Geçersiz ay numarası!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except IndexError as e:
    print(f"HATA: {e}")

# Demeti listeye dönüştürme örneği
print("\n=== DEMETTEN LİSTEYE DÖNÜŞÜM ===")
ay_listesi = list(AYLAR)
print(f"Liste versiyonu: {ay_listesi}")

print("Ay işlemleri tamamlandı.")