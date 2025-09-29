# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 4
# Şifre Güçlülük Kontrolü

def sifre_kontrol(sifre):
    """Şifrenin güçlülüğünü kontrol eder"""
    
    # Kontrol kriterleri
    kriterler = {
        'uzunluk': len(sifre) >= 8,
        'kucuk_harf': any(c.islower() for c in sifre),
        'buyuk_harf': any(c.isupper() for c in sifre),
        'rakam': any(c.isdigit() for c in sifre),
        'ozel_karakter': any(not c.isalnum() for c in sifre)
    }
    
    # Puan hesapla
    puan = sum(kriterler.values())
    
    # Güç seviyesini belirle
    if puan == 5:
        seviye = "Çok Güçlü 🔒"
    elif puan == 4:
        seviye = "Güçlü ✅"
    elif puan == 3:
        seviye = "Orta ⚠️"
    else:
        seviye = "Zayıf ❌"
    
    return {
        'puan': puan,
        'seviye': seviye,
        'kriterler': kriterler
    }

def sifre_raporu(sifre, sonuc):
    """Şifre raporunu görüntüler"""
    print("\n" + "="*40)
    print("🔐 ŞİFRE GÜVENLİK RAPORU")
    print("="*40)
    
    print(f"Şifre: {'*' * len(sifre)}")
    print(f"Güç Seviyesi: {sonuc['seviye']}")
    print(f"Puan: {sonuc['puan']}/5")
    
    print("\nKriterler:")
    kriter_adlari = {
        'uzunluk': "En az 8 karakter",
        'kucuk_harf': "Küçük harf içeriyor",
        'buyuk_harf': "Büyük harf içeriyor", 
        'rakam': "Rakam içeriyor",
        'ozel_karakter': "Özel karakter içeriyor"
    }
    
    for kriter, gecerli in sonuc['kriterler'].items():
        durum = "✅" if gecerli else "❌"
        print(f"  {durum} {kriter_adlari[kriter]}")

def guclu_sifre_olustur():
    """Rastgele güçlü şifre önerileri oluşturur"""
    import random
    import string
    
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    rakamlar = string.digits
    ozel_karakterler = "!@#$%^&*"
    
    # Her kategoriden en az bir karakter al
    sifre = [
        random.choice(kucuk_harfler),
        random.choice(buyuk_harfler),
        random.choice(rakamlar),
        random.choice(ozel_karakterler)
    ]
    
    # Kalan karakterleri rastgele seç
    tum_karakterler = kucuk_harfler + buyuk_harfler + rakamlar + ozel_karakterler
    sifre.extend(random.choice(tum_karakterler) for _ in range(4))
    
    # Karakterleri karıştır
    random.shuffle(sifre)
    
    return ''.join(sifre)

# Ana program
try:
    while True:
        print("\n1: Şifre Kontrol Et")
        print("2: Güçlü Şifre Öner")
        print("3: Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            sifre = input("Kontrol edilecek şifreyi girin: ")
            sonuc = sifre_kontrol(sifre)
            sifre_raporu(sifre, sonuc)
            
        elif secim == '2':
            print("\n💡 Güçlü Şifre Önerileri:")
            for i in range(3):
                sifre = guclu_sifre_olustur()
                sonuc = sifre_kontrol(sifre)
                print(f"  {i+1}. {sifre} - {sonuc['seviye']}")
                
        elif secim == '3':
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim!")
            
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Şifre kontrol programı kapatıldı.")