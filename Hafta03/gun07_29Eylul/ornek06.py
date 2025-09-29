# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 3
# Kelime İstatistikleri Hesaplayıcı

def kelime_istatistikleri(metin):
    """Metnin kelime istatistiklerini hesaplar"""
    if not metin.strip():
        raise ValueError("Metin boş olamaz!")
    
    # Kelimeleri ayır ve temizle
    kelimeler = [kelime.strip('.,!?;:"').lower() for kelime in metin.split()]
    
    # İstatistikleri hesapla
    istatistikler = {
        'toplam_kelime': len(kelimeler),
        'benzersiz_kelime': len(set(kelimeler)),
        'kelime_frekanslari': {},
        'en_uzun_kelime': '',
        'en_kisa_kelime': kelimeler[0] if kelimeler else ''
    }
    
    # Kelime frekanslarını hesapla
    for kelime in kelimeler:
        istatistikler['kelime_frekanslari'][kelime] = istatistikler['kelime_frekanslari'].get(kelime, 0) + 1
    
    # En uzun ve en kısa kelimeyi bul
    if kelimeler:
        istatistikler['en_uzun_kelime'] = max(kelimeler, key=len)
        istatistikler['en_kisa_kelime'] = min(kelimeler, key=len)
    
    return istatistikler

def istatistikleri_goruntule(istatistikler):
    """İstatistikleri görüntüler"""
    print("\n" + "="*40)
    print("📊 KELİME İSTATİSTİKLERİ")
    print("="*40)
    
    print(f"Toplam kelime sayısı: {istatistikler['toplam_kelime']}")
    print(f"Benzersiz kelime sayısı: {istatistikler['benzersiz_kelime']}")
    print(f"En uzun kelime: '{istatistikler['en_uzun_kelime']}' ({len(istatistikler['en_uzun_kelime'])} harf)")
    print(f"En kısa kelime: '{istatistikler['en_kisa_kelime']}' ({len(istatistikler['en_kisa_kelime'])} harf)")
    
    print("\nEn sık kullanılan kelimeler:")
    sirali_kelimeler = sorted(istatistikler['kelime_frekanslari'].items(), 
                            key=lambda x: x[1], reverse=True)[:5]
    
    for kelime, frekans in sirali_kelimeler:
        print(f"  '{kelime}': {frekans} kez")

# Ana program
try:
    print("📝 Kelime İstatistikleri Hesaplayıcı")
    print("="*40)
    
    metin = input("Lütfen bir metin girin:\n")
    
    istatistikler = kelime_istatistikleri(metin)
    istatistikleri_goruntule(istatistikler)
    
except ValueError as e:
    print(f"❌ Hata: {e}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("\nProgram tamamlandı!")