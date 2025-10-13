#json kaydetme
import ders01
def json_dosyasina_kaydet(film_verisi):
    """
    Aldığımız film verisini 'film_arşivi.json' dosyasına ekler.
    Dosya yoksa oluşturur, varsa mevcut veriyi koruyarak yeni filmi listeye ekler.
    """
    dosya_adi = "film_arşivi.json"
    
    # Dosyada mevcut filmleri oku (varsa)
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            mevcut_veriler = json.load(f)  # JSON'u Python listesine çevir
    except FileNotFoundError:
        # Dosya yoksa boş liste başlat
        mevcut_veriler = []
    except json.JSONDecodeError:
        # Dosya bozuksa (geçersiz JSON), yeni baştan oluştur
        print("⚠️ Dosya bozuk, yeni arşiv oluşturuluyor.")
        mevcut_veriler = []
    
    # Yeni filmi listeye ekle
    mevcut_veriler.append(film_verisi)
    
    # Güncellenmiş listeyi tekrar JSON olarak yaz
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Film '{dosya_adi}' dosyasına kaydedildi.")