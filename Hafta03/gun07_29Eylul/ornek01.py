# FONKSİYONLAR & VERİ YAPILARI - ÖRNEK 1
# Akıllı Alışveriş Listesi Yöneticisi

def akilli_alisveris_listesi():
    """Akıllı alışveriş listesi yönetimi"""
    
    alisveris_listesi = []
    kategoriler = {
        "meyve": ["elma", "armut", "muz", "portakal"],
        "sebze": ["domates", "salatalık", "biber", "patates"],
        "süt": ["süt", "yoğurt", "peynir", "tereyağı"]
    }
    
    def urun_ekle():
        """Listeye yeni ürün ekler"""
        try:
            print("\nMevcut kategoriler:", list(kategoriler.keys()))
            kategori = input("Kategori: ").strip().lower()
            urun = input("Ürün adı: ").strip().lower()
            
            if not kategori or not urun:
                raise ValueError("Kategori ve ürün adı boş olamaz!")
            
            if kategori not in kategoriler:
                kategoriler[kategori] = []
            
            if urun in alisveris_listesi:
                print("⚠️  Bu ürün zaten listede var!")
                return
            
            alisveris_listesi.append(urun)
            kategoriler[kategori].append(urun)
            print(f"✅ '{urun}' {kategori} kategorisine eklendi!")
            
        except ValueError as e:
            print(f"❌ Hata: {e}")
    
    def liste_goruntule():
        """Listeyi kategorilere göre gösterir"""
        if not alisveris_listesi:
            print("📝 Liste boş!")
            return
        
        print("\n🛒 ALIŞVERİŞ LİSTESİ")
        print("=" * 30)
        
        for kategori, urunler in kategoriler.items():
            if urunler:
                print(f"\n📁 {kategori.upper()}:")
                for urun in urunler:
                    if urun in alisveris_listesi:
                        print(f"   ✅ {urun}")
    
    def urun_ara():
        """Ürün arama fonksiyonu"""
        try:
            aranan = input("Aranacak ürün: ").strip().lower()
            if not aranan:
                raise ValueError("Arama terimi boş olamaz!")
            
            bulunanlar = []
            for urun in alisveris_listesi:
                if aranan in urun:
                    bulunanlar.append(urun)
            
            if bulunanlar:
                print(f"🔍 Bulunan ürünler: {bulunanlar}")
            else:
                print("❌ Ürün bulunamadı!")
                
        except ValueError as e:
            print(f"Hata: {e}")
    
    # Ana program döngüsü
    while True:
        print("\n" + "="*40)
        print("🛒 AKILLI ALIŞVERİŞ LİSTESİ")
        print("="*40)
        print("1: Ürün Ekle")
        print("2: Listeyi Görüntüle")
        print("3: Ürün Ara")
        print("4: Çıkış")
        
        try:
            secim = int(input("Seçiminiz: "))
            
            if secim == 1:
                urun_ekle()
            elif secim == 2:
                liste_goruntule()
            elif secim == 3:
                urun_ara()
            elif secim == 4:
                print("👋 Program sonlandırılıyor...")
                break
            else:
                print("❌ Geçersiz seçim!")
                
        except ValueError:
            print("❌ Lütfen geçerli bir sayı girin!")

# Programı başlat
akilli_alisveris_listesi()