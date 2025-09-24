"""
ç içe veri yapılarını (liste + sözlük) kullanarak:

Kitap eklemek
Tüm kitapları listelemek
Belirli bir yazarın kitaplarını filtrelemek
Basit bir menü sistemi kurmak

"""
#part1: veri yapısı
kitaplar = [
    {
        "baslik": "Python İle Programlama",
        "yazar": "Zeynep Yılmaz",
        "yil": 2021,
        "tur": "Bilgisayar"
    },
    {
        "baslik": "Dünyanın Dili",
        "yazar": "Ali Demir",
        "yil": 2019,
        "tur": "Edebiyat"
    },
    {
        "baslik": "Veri Bilimine Giriş",
        "yazar": "Zeynep Yılmaz",
        "yil": 2022,
        "tur": "Bilim"
    }
]

#part2: 
#menü ve işlevler
# kullanıcıdan seçim al, işlemi yap
# 1. kitap ekle
# 2. tüm kitapları listele
# 3. yazara göre filtrele
# 4. çıkış  

kitaplar = []  # Başlangıçta boş liste

print("📚 KÜTÜPHANE YÖNETİM SİSTEMİ")
print("Bu küçük sistemde kitap ekleyebilir ve listeleyebilirsiniz.\n")

while True:
    print("\n=== MENÜ ===")
    print("1. Kitap Ekle")
    print("2. Tüm Kitapları Listele")
    print("3. Yazardan Kitap Bul")
    print("4. Çıkış")
    
    secim = input("Seçiminiz (1-4): ")
    
    if secim == "1":
        print("\n--- Yeni Kitap Ekle ---")
        baslik = input("Kitap başlığı: ")
        yazar = input("Yazar adı: ")
        yil = int(input("Yıl: "))
        tur = input("Tür: ")
        
        kitap = {
            "baslik": baslik,
            "yazar": yazar,
            "yil": yil,
            "tur": tur
        }
        kitaplar.append(kitap)
        print(f"'{baslik}' kitabı kütüphaneye eklendi.")
    
    elif secim == "2":
        print("\n--- TÜM KİTAPLAR ---")
        if len(kitaplar) == 0:
            print("Kütüphanede henüz kitap yok.")
        else:
            for kitap in kitaplar:
                print(f"📘 {kitap['baslik']} | Yazar: {kitap['yazar']} | Yıl: {kitap['yil']} | Tür: {kitap['tur']}")
    
    elif secim == "3":
        print("\n--- YAZARA GÖRE ARAMA ---")
        aranan_yazar = input("Aranan yazar adı: ")
        bulunanlar = []
        
        for kitap in kitaplar:
            if kitap["yazar"].lower() == aranan_yazar.lower():
                bulunanlar.append(kitap)
        
        if len(bulunanlar) == 0:
            print(f"{aranan_yazar} adına ait kitap bulunamadı.")
        else:
            print(f"{aranan_yazar} için bulunan kitaplar:")
            for kitap in bulunanlar:
                print(f"➡️  {kitap['baslik']} ({kitap['yil']})")
    
    elif secim == "4":
        print("👋 Kütüphane sisteminden çıkılıyor. Hoşça kal!")
        break
    
    else:
        print("❌ Geçersiz seçim. Lütfen 1-4 arasında bir sayı girin.")

