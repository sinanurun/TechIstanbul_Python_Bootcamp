# HATA YÖNETİMİ - ÖRNEK 13
# Liste Elemanı Güvenli Erişim 
# Bu program, bir meyve listesi üzerinde kullanıcıdan indeks alır.
# Hatalı indeks girişlerinde anlamlı mesajlar verir.

print("=== LİSTE ELEMANI GÜVENLİ ERİŞİM ===")

meyveler = ["elma", "armut", "çilek", "muz", "portakal"]
print(f"Mevcut meyveler: {meyveler}")

while True:
    try:
        indeks = int(input("\nKaçıncı meyveyi görmek istersiniz? (0-4, çıkmak için -1): "))
        
        if indeks == -1:
            print("Çıkış yapılıyor...")
            break
        
        # Listeden elemana erişim
        secilen_meyve = meyveler[indeks]
        print(f"{indeks}. indeksteki meyve: {secilen_meyve}")
        
        # Meyve uzunluğunu göster
        uzunluk = len(secilen_meyve)
        print(f"Bu meyve {uzunluk} harflidir.")
        
    except ValueError:
        print("HATA: Lütfen geçerli bir sayı girin!")
    except IndexError:
        print(f"HATA: Geçersiz indeks! Sadece 0-{len(meyveler)-1} arası girebilirsiniz.")

print("Program sonlandı.")