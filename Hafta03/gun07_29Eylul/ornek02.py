# FONKSİYONLAR & VERİ YAPILARI - ÖRNEK 2
# Öğrenci Not Takip Sistemi

def ogrenci_not_sistemi():
    """Öğrenci not takip sistemi"""
    
    ogrenciler = {}
    
    def ogrenci_ekle():
        """Yeni öğrenci ekler"""
        try:
            ad = input("Öğrenci adı: ").strip().title()
            if not ad:
                raise ValueError("Öğrenci adı boş olamaz!")
            
            if ad in ogrenciler:
                print("⚠️  Bu öğrenci zaten kayıtlı!")
                return
            
            ogrenciler[ad] = {
                "notlar": [],
                "devam": True,
                "kayit_tarihi": None
            }
            print(f"✅ '{ad}' öğrencisi eklendi!")
            
        except ValueError as e:
            print(f"❌ Hata: {e}")
    
    def not_ekle():
        """Öğrenciye not ekler"""
        try:
            if not ogrenciler:
                print("❌ Henüz öğrenci kaydı yok!")
                return
            
            print("Mevcut öğrenciler:", list(ogrenciler.keys()))
            ad = input("Öğrenci adı: ").strip().title()
            
            if ad not in ogrenciler:
                raise KeyError("Öğrenci bulunamadı!")
            
            not_degeri = float(input("Not (0-100): "))
            if not 0 <= not_degeri <= 100:
                raise ValueError("Not 0-100 arasında olmalı!")
            
            ogrenciler[ad]["notlar"].append(not_degeri)
            print(f"✅ '{ad}' öğrencisine {not_degeri} notu eklendi!")
            
        except (ValueError, KeyError) as e:
            print(f"❌ Hata: {e}")
    
    def istatistik_goruntule():
        """Öğrenci istatistiklerini gösterir"""
        if not ogrenciler:
            print("❌ Henüz öğrenci kaydı yok!")
            return
        
        print("\n📊 ÖĞRENCİ İSTATİSTİKLERİ")
        print("=" * 40)
        
        for ad, bilgiler in ogrenciler.items():
            notlar = bilgiler["notlar"]
            if notlar:
                ortalama = sum(notlar) / len(notlar)
                en_yuksek = max(notlar)
                en_dusuk = min(notlar)
                
                print(f"\n👤 {ad}:")
                print(f"   📈 Notlar: {notlar}")
                print(f"   ⭐ Ortalama: {ortalama:.1f}")
                print(f"   🔼 En yüksek: {en_yuksek}")
                print(f"   🔽 En düşük: {en_dusuk}")
            else:
                print(f"\n👤 {ad}: Henüz not girilmemiş")
    
    def en_basarili_ogrenci():
        """En başarılı öğrenciyi bulur"""
        if not ogrenciler:
            print("❌ Henüz öğrenci kaydı yok!")
            return
        
        basarili_ogrenci = None
        en_yuksek_ortalama = 0
        
        for ad, bilgiler in ogrenciler.items():
            notlar = bilgiler["notlar"]
            if notlar:
                ortalama = sum(notlar) / len(notlar)
                if ortalama > en_yuksek_ortalama:
                    en_yuksek_ortalama = ortalama
                    basarili_ogrenci = ad
        
        if basarili_ogrenci:
            print(f"🎉 En başarılı öğrenci: {basarili_ogrenci}")
            print(f"🏆 Ortalama: {en_yuksek_ortalama:.1f}")
        else:
            print("❌ Henüz not girilmemiş öğrenci yok!")
    
    # Ana program
    while True:
        print("\n" + "="*40)
        print("🎓 ÖĞRENCİ NOT TAKİP SİSTEMİ")
        print("="*40)
        print("1: Öğrenci Ekle")
        print("2: Not Ekle")
        print("3: İstatistikleri Görüntüle")
        print("4: En Başarılı Öğrenci")
        print("5: Çıkış")
        
        try:
            secim = int(input("Seçiminiz: "))
            
            if secim == 1:
                ogrenci_ekle()
            elif secim == 2:
                not_ekle()
            elif secim == 3:
                istatistik_goruntule()
            elif secim == 4:
                en_basarili_ogrenci()
            elif secim == 5:
                print("👋 Program sonlandırılıyor...")
                break
            else:
                print("❌ Geçersiz seçim!")
                
        except ValueError:
            print("❌ Lütfen geçerli bir sayı girin!")

# Programı başlat
ogrenci_not_sistemi()