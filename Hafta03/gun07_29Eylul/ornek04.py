# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 1
# Akıllı Alışveriş Listesi

def alisveris_listesi_olustur():
    """Akıllı alışveriş listesi oluşturur"""
    liste = []
    print("🛒 Alışveriş Listesi Oluşturucu")
    print("Çıkmak için 'q' yazın")
    
    while True:
        try:
            urun = input("Ürün adı: ").strip()
            
            if urun.lower() == 'q':
                break
                
            if not urun:
                raise ValueError("Ürün adı boş olamaz!")
            
            fiyat = float(input("Ürün fiyatı: ₺"))
            if fiyat <= 0:
                raise ValueError("Fiyat pozitif olmalıdır!")
            
            miktar = int(input("Miktar: "))
            if miktar <= 0:
                raise ValueError("Miktar pozitif olmalıdır!")
            
            # Ürünü listeye ekle
            urun_bilgisi = {
                "ad": urun,
                "fiyat": fiyat,
                "miktar": miktar,
                "toplam": fiyat * miktar
            }
            
            liste.append(urun_bilgisi)
            print(f"✅ '{urun}' eklendi!")
            
        except ValueError as e:
            print(f"❌ Hata: {e}")
    
    return liste

def liste_goruntule(liste):
    """Alışveriş listesini görüntüler"""
    if not liste:
        print("📝 Liste boş!")
        return
    
    print("\n" + "="*40)
    print("🛒 ALIŞVERİŞ LİSTEM")
    print("="*40)
    
    toplam_tutar = 0
    for i, urun in enumerate(liste, 1):
        print(f"{i}. {urun['ad']:15} {urun['miktar']:3} x ₺{urun['fiyat']:6.2f} = ₺{urun['toplam']:7.2f}")
        toplam_tutar += urun['toplam']
    
    print("="*40)
    print(f"💰 TOPLAM TUTAR: ₺{toplam_tutar:.2f}")

# Ana program
try:
    alisveris_listem = alisveris_listesi_olustur()
    liste_goruntule(alisveris_listem)
    
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Alışveriş listesi tamamlandı!")