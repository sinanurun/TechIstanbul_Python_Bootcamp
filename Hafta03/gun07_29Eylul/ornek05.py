# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 2
# Öğrenci Not Takip Sistemi

def ogrenci_ekle(ogrenci_listesi):
    """Yeni öğrenci ekler"""
    try:
        ad = input("Öğrenci adı: ").strip()
        if not ad:
            raise ValueError("Öğrenci adı boş olamaz!")
        
        # Notları al
        notlar = []
        while True:
            try:
                not_str = input("Not girin (çıkmak için 'q'): ").strip()
                if not_str.lower() == 'q':
                    break
                
                not_deger = float(not_str)
                if not 0 <= not_deger <= 100:
                    raise ValueError("Not 0-100 arası olmalıdır!")
                
                notlar.append(not_deger)
                
            except ValueError as e:
                print(f"Geçersiz not: {e}")
        
        # Öğrenci bilgilerini oluştur
        ogrenci = {
            "ad": ad,
            "notlar": notlar,
            "ortalama": sum(notlar) / len(notlar) if notlar else 0
        }
        
        ogrenci_listesi.append(ogrenci)
        print(f"✅ '{ad}' eklendi!")
        
    except ValueError as e:
        print(f"❌ Hata: {e}")

def ogrenci_listele(ogrenci_listesi):
    """Öğrencileri listeler"""
    if not ogrenci_listesi:
        print("📝 Öğrenci listesi boş!")
        return
    
    print("\n" + "="*50)
    print("📚 ÖĞRENCİ LİSTESİ")
    print("="*50)
    
    for i, ogrenci in enumerate(ogrenci_listesi, 1):
        durum = "✅ Geçti" if ogrenci['ortalama'] >= 50 else "❌ Kaldı"
        print(f"{i}. {ogrenci['ad']:15} Notlar: {ogrenci['notlar']} Ortalama: {ogrenci['ortalama']:.1f} {durum}")

def en_basarili_ogrenci(ogrenci_listesi):
    """En başarılı öğrenciyi bulur"""
    if not ogrenci_listesi:
        print("Liste boş!")
        return
    
    en_basarili = max(ogrenci_listesi, key=lambda x: x['ortalama'])
    print(f"🎉 En başarılı öğrenci: {en_basarili['ad']} - Ortalama: {en_basarili['ortalama']:.1f}")

# Ana program
ogrenciler = []

while True:
    try:
        print("\n1: Öğrenci Ekle")
        print("2: Öğrenci Listele")
        print("3: En Başarılı Öğrenci")
        print("4: Çıkış")
        
        secim = int(input("Seçiminiz: "))
        
        if secim == 1:
            ogrenci_ekle(ogrenciler)
        elif secim == 2:
            ogrenci_listele(ogrenciler)
        elif secim == 3:
            en_basarili_ogrenci(ogrenciler)
        elif secim == 4:
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim!")
            
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

print("Öğrenci takip sistemi kapatıldı.")