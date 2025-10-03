# DOSYA İŞLEMLERİ - ÖRNEK 1
# Basit Metin Dosyası İşlemleri

def dosya_olustur_ve_yaz():
    """Yeni dosya oluşturur ve içerik yazar"""
    try:
        with open("notlar.txt", "w", encoding="utf-8") as dosya:
            dosya.write("Python Dosya İşlemleri\n")
            dosya.write("=====================\n")
            dosya.write("1. with deyimi kullan\n")
            dosya.write("2. encoding belirt\n")
            dosya.write("3. Hata yönetimi yap\n")
        print("✅ Dosya başarıyla oluşturuldu ve yazıldı!")
    except Exception as e:
        print(f"❌ Hata: {e}")

def dosya_oku_ve_goster():
    """Dosyayı okur ve içeriği gösterir"""
    try:
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            print("\n📖 DOSYA İÇERİĞİ:")
            print("=" * 30)
            for i, satir in enumerate(dosya, 1):
                print(f"{i:2}. {satir.rstrip()}")
    except FileNotFoundError:
        print("❌ Dosya bulunamadı! Önce dosya oluşturun.")
    except Exception as e:
        print(f"❌ Hata: {e}")

def dosyaya_ekle():
    """Dosyanın sonuna yeni içerik ekler"""
    try:
        yeni_icerik = input("Eklemek istediğiniz metni girin: ")
        with open("notlar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(yeni_icerik + "\n")
        print("✅ İçerik başarıyla eklendi!")
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana program
print("📝 METİN DOSYASI İŞLEMLERİ")
print("=" * 30)

while True:
    print("\n1. Dosya Oluştur ve Yaz")
    print("2. Dosyayı Oku ve Göster")
    print("3. Dosyaya Ekle")
    print("4. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        dosya_olustur_ve_yaz()
    elif secim == "2":
        dosya_oku_ve_goster()
    elif secim == "3":
        dosyaya_ekle()
    elif secim == "4":
        print("👋 Program sonlandırılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print("Program tamamlandı!")