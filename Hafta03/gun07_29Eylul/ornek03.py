# FONKSİYONLAR & VERİ YAPILARI - ÖRNEK 3
# Banka Hesap Yönetim Sistemi

def banka_hesap_sistemi():
    """Banka hesap yönetim sistemi"""
    
    hesaplar = {}
    hesap_nolari = set()
    
    def hesap_ac():
        """Yeni banka hesabı açar"""
        try:
            ad = input("Hesap sahibi adı: ").strip().title()
            if not ad:
                raise ValueError("Ad boş olamaz!")
            
            # Benzersiz hesap numarası oluştur
            while True:
                hesap_no = len(hesaplar) + 1000
                if hesap_no not in hesap_nolari:
                    break
            
            baslangic_bakiyesi = float(input("Başlangıç bakiyesi: "))
            if baslangic_bakiyesi < 0:
                raise ValueError("Bakiye negatif olamaz!")
            
            hesaplar[hesap_no] = {
                "ad": ad,
                "bakiye": baslangic_bakiyesi,
                "islem_gecmisi": []
            }
            hesap_nolari.add(hesap_no)
            
            print(f"✅ Hesap açıldı!")
            print(f"   👤 Hesap Sahibi: {ad}")
            print(f"   🔢 Hesap No: {hesap_no}")
            print(f"   💰 Bakiye: {baslangic_bakiyesi:.2f}₺")
            
        except ValueError as e:
            print(f"❌ Hata: {e}")
    
    def para_yatir():
        """Hesaba para yatırır"""
        try:
            if not hesaplar:
                print("❌ Henüz hesap yok!")
                return
            
            hesap_no = int(input("Hesap numarası: "))
            if hesap_no not in hesaplar:
                raise KeyError("Hesap bulunamadı!")
            
            miktar = float(input("Yatırılacak miktar: "))
            if miktar <= 0:
                raise ValueError("Miktar pozitif olmalı!")
            
            hesaplar[hesap_no]["bakiye"] += miktar
            hesaplar[hesap_no]["islem_gecmisi"].append(f"+{miktar:.2f}₺")
            
            print(f"✅ {miktar:.2f}₺ yatırıldı!")
            print(f"💰 Yeni bakiye: {hesaplar[hesap_no]['bakiye']:.2f}₺")
            
        except (ValueError, KeyError) as e:
            print(f"❌ Hata: {e}")
    
    def para_cek():
        """Hesaptan para çeker"""
        try:
            if not hesaplar:
                print("❌ Henüz hesap yok!")
                return
            
            hesap_no = int(input("Hesap numarası: "))
            if hesap_no not in hesaplar:
                raise KeyError("Hesap bulunamadı!")
            
            miktar = float(input("Çekilecek miktar: "))
            if miktar <= 0:
                raise ValueError("Miktar pozitif olmalı!")
            
            if miktar > hesaplar[hesap_no]["bakiye"]:
                raise ValueError("Yetersiz bakiye!")
            
            hesaplar[hesap_no]["bakiye"] -= miktar
            hesaplar[hesap_no]["islem_gecmisi"].append(f"-{miktar:.2f}₺")
            
            print(f"✅ {miktar:.2f}₺ çekildi!")
            print(f"💰 Yeni bakiye: {hesaplar[hesap_no]['bakiye']:.2f}₺")
            
        except (ValueError, KeyError) as e:
            print(f"❌ Hata: {e}")
    
    def hesap_raporu():
        """Hesap raporu gösterir"""
        try:
            if not hesaplar:
                print("❌ Henüz hesap yok!")
                return
            
            hesap_no = int(input("Hesap numarası: "))
            if hesap_no not in hesaplar:
                raise KeyError("Hesap bulunamadı!")
            
            hesap = hesaplar[hesap_no]
            print(f"\n📊 HESAP RAPORU - {hesap_no}")
            print("=" * 40)
            print(f"👤 Hesap Sahibi: {hesap['ad']}")
            print(f"💰 Güncel Bakiye: {hesap['bakiye']:.2f}₺")
            print(f"📋 İşlem Geçmişi:")
            
            for i, islem in enumerate(hesap['islem_gecmisi'], 1):
                print(f"   {i}. {islem}")
                
        except (ValueError, KeyError) as e:
            print(f"❌ Hata: {e}")
    
    # Ana program
    while True:
        print("\n" + "="*40)
        print("🏦 BANK HESAP YÖNETİM SİSTEMİ")
        print("="*40)
        print("1: Hesap Aç")    
        print("2: Para Yatır")
        print("3: Para Çek")
        print("4: Hesap Raporu")
        print("5: Çıkış")
        try:
            secim = int(input("Seçiminiz: "))
            
            if secim == 1:
                hesap_ac()
            elif secim == 2:
                para_yatir()
            elif secim == 3:
                para_cek()
            elif secim == 4:
                hesap_raporu()
            elif secim == 5:
                print("👋 Hoşça kalın!")
                break
            else:
                print("❌ Geçersiz seçim!")
                
        except ValueError as e:
            print(f"❌ Hata: {e}")
            print("❌ Lütfen geçerli bir sayı girin!")
            print("="*40)
        except Exception as e:  
            print(f"❌ Hata: {e}")
            print("❌ Beklenmedik bir hata oluştu!")
            print("="*40)
            print("❌ Lütfen geçerli bir sayı girin!")
            print("="*40)   

banka_hesap_sistemi()