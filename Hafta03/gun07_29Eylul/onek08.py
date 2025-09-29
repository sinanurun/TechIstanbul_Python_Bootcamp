# FONKSİYONLAR & KOLEKSİYONLAR - ÖRNEK 5
# Film Koleksiyon Yöneticisi

def film_ekle(film_koleksiyonu):
    """Yeni film ekler"""
    try:
        ad = input("Film adı: ").strip()
        if not ad:
            raise ValueError("Film adı boş olamaz!")
        
        yil = int(input("Yayın yılı: "))
        if yil < 1888 or yil > 2030:  # İlk film 1888'de çekildi
            raise ValueError("Geçersiz yıl!")
        
        tur = input("Tür (aksiyon, komedi, dram, vb.): ").strip().lower()
        puan = float(input("IMDb puanı (0-10): "))
        if not 0 <= puan <= 10:
            raise ValueError("Puan 0-10 arası olmalıdır!")
        
        film = {
            'ad': ad,
            'yil': yil,
            'tur': tur,
            'puan': puan,
            'izlendi': False
        }
        
        film_koleksiyonu.append(film)
        print(f"✅ '{ad}' koleksiyona eklendi!")
        
    except ValueError as e:
        print(f"❌ Hata: {e}")

def film_ara(film_koleksiyonu, anahtar_kelime):
    """Filmleri ara"""
    bulunan_filmler = []
    
    for film in film_koleksiyonu:
        if (anahtar_kelime.lower() in film['ad'].lower() or 
            anahtar_kelime.lower() in film['tur'].lower()):
            bulunan_filmler.append(film)
    
    return bulunan_filmler

def film_listele(film_koleksiyonu, tur=None, siralama='ad'):
    """Filmleri listeler"""
    if not film_koleksiyonu:
        print("🎬 Film koleksiyonu boş!")
        return
    
    # Filtrele
    if tur:
        filmler = [f for f in film_koleksiyonu if f['tur'] == tur]
    else:
        filmler = film_koleksiyonu
    
    # Sırala
    if siralama == 'puan':
        filmler.sort(key=lambda x: x['puan'], reverse=True)
    elif siralama == 'yil':
        filmler.sort(key=lambda x: x['yil'], reverse=True)
    else:
        filmler.sort(key=lambda x: x['ad'])
    
    # Görüntüle
    print(f"\n{'='*60}")
    print(f"🎬 FİLM KOLEKSİYONU ({len(filmler)} film)")
    print('='*60)
    
    for i, film in enumerate(filmler, 1):
        izlendi_durum = "✅" if film['izlendi'] else "⏳"
        print(f"{i}. {izlendi_durum} {film['ad']:25} ({film['yil']}) - {film['tur']:10} - ⭐{film['puan']:.1f}")

def istatistikler(film_koleksiyonu):
    """Koleksiyon istatistiklerini göster"""
    if not film_koleksiyonu:
        print("İstatistik hesaplanamıyor (koleksiyon boş)!")
        return
    
    toplam_film = len(film_koleksiyonu)
    izlenenler = sum(1 for f in film_koleksiyonu if f['izlendi'])
    en_yuksek_puan = max(film_koleksiyonu, key=lambda x: x['puan'])
    en_eski_film = min(film_koleksiyonu, key=lambda x: x['yil'])
    
    # Tür dağılımı
    tur_dagilimi = {}
    for film in film_koleksiyonu:
        tur_dagilimi[film['tur']] = tur_dagilimi.get(film['tur'], 0) + 1
    
    print("\n📊 KOLEKSİYON İSTATİSTİKLERİ")
    print(f"Toplam film: {toplam_film}")
    print(f"İzlenen filmler: {izlenenler} ({izlenenler/toplam_film*100:.1f}%)")
    print(f"En yüksek puanlı: {en_yuksek_puan['ad']} ({en_yuksek_puan['puan']})")
    print(f"En eski film: {en_eski_film['ad']} ({en_eski_film['yil']})")
    
    print("\nTür Dağılımı:")
    for tur, sayi in sorted(tur_dagilimi.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tur}: {sayi} film")

# Ana program
film_koleksiyonu = []

while True:
    try:
        print("\n1: Film Ekle")
        print("2: Film Ara")
        print("3: Tüm Filmleri Listele") 
        print("4: İstatistikler")
        print("5: Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            film_ekle(film_koleksiyonu)
        elif secim == '2':
            anahtar = input("Aranacak kelime: ")
            bulunan = film_ara(film_koleksiyonu, anahtar)
            film_listele(bulunan)
        elif secim == '3':
            film_listele(film_koleksiyonu)
        elif secim == '4':
            istatistikler(film_koleksiyonu)
        elif secim == '5':
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz seçim!")
            
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

print("Film koleksiyon yöneticisi kapatıldı.")