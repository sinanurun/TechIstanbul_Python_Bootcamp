# HATA YÖNETİMİ - ÖRNEK 6
# Hata Türüne Özel Mesajlar

"""
Bu program, farklı hata türleri için özelleştirilmiş mesajlar gösterir.
Her hata türü için ayrı except blokları kullanır.
"""

print("=== DETAYLI HATA MESAJLARI ===")

def hesapla():
    try:
        # Kullanıcıdan çeşitli veriler alıyoruz
        sayi = int(input("Bir tam sayı girin: "))
        bolen = int(input("Bölecek sayıyı girin: "))
        
        # Liste oluşturuyoruz
        liste = [1, 2, 3, 4, 5]
        
        # Çeşitli işlemler yapıyoruz
        bolum = sayi / bolen
        liste_elemani = liste[sayi]  # Burada IndexError olabilir
        
        print(f"Bölüm: {bolum}")
        print(f"Liste elemanı: {liste_elemani}")
        
    except ValueError:
        # Sayı dönüşüm hatası
        print("HATA: Lütfen geçerli bir tam sayı girin!")
        print("Örnek: 5, 10, 25 gibi...")
        
    except ZeroDivisionError:
        # Sıfıra bölme hatası
        print("HATA: Bir sayıyı sıfıra bölemezsiniz!")
        print("Lütfen sıfırdan farklı bir sayı girin.")
        
    except IndexError:
        # Liste indeks hatası
        print("HATA: Geçersiz liste indeksi!")
        print(f"Lütfen 0 ile {len(liste)-1} arasında bir sayı girin.")
        
    except Exception as genel_hata:
        # Diğer tüm hatalar için
        print(f"Beklenmeyen bir hata oluştu: {genel_hata}")

# Fonksiyonu çağırıyoruz
hesapla()
print("İşlem tamamlandı.")