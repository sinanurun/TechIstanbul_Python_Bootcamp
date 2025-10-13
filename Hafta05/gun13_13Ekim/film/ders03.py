#Temel API Çağrısı ve Veri Alma
import requests
import json
from datetime import datetime

# Kullanıcıdan film adı al ve OMDb API'sinden veri çek
def film_ara_ve_kaydet_json(film_adi, api_key):
    # API endpoint'i: film adı ve API anahtarı ile istek yapılır
    url = f"http://www.omdbapi.com/?t={film_adi}&apikey={api_key}"
    
    try:
        # API'ye GET isteği gönder
        response = requests.get(url, timeout=10)
        
        # Eğer bağlantı başarılıysa (HTTP 200)
        if response.status_code == 200:
            veri = response.json()  # JSON'u Python sözlüğüne çevir
            
            # API, film bulunamazsa "Response":"False" döner
            if veri.get("Response") == "False":
                print(f"❌ '{film_adi}' adlı film bulunamadı.")
                return None
            
            # Başarılı yanıt: film bilgilerini ekrana yaz
            print(f"\n🎬 Film: {veri.get('Title', 'Bilinmiyor')}")
            print(f"📅 Yıl: {veri.get('Year', 'N/A')}")
            print(f"⭐ IMDB Puanı: {veri.get('imdbRating', 'N/A')}")
            print(f"🎭 Tür: {veri.get('Genre', 'N/A')}")
            print(f"📝 Özet: {veri.get('Plot', 'N/A')[:150]}...")
            
            return veri  # Veriyi döndür, dosyaya yazmak için kullanacağız
        
        else:
            print(f"⚠️ API isteği başarısız oldu. HTTP Kodu: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ İnternet bağlantısı yok.")
        return None
    except requests.exceptions.Timeout:
        print("⏱️ İstek zaman aşımına uğradı.")
        return None
    except Exception as e:
        print(f"🚨 Beklenmeyen hata: {e}")
        return None

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

# --- ANA PROGRAM ---
if __name__ == "__main__":
    # Öğrenciler kendi API anahtarlarını buraya yazmalı
    API_KEY = "eca634d5"  # ← BURAYI DEĞİŞTİRİN!
    
    if API_KEY == "eca634d5":
        print("❗ Lütfen geçerli bir OMDb API anahtarı girin.")
    else:
        print("🎥 Film Arama ve Arşivleme Uygulaması")
        print("Çıkmak için 'q' yazın.\n")
        
    while True:
        film = input("Film adı girin: ").strip()
        if film.lower() == 'q':
            print("Çıkış yapılıyor...")
            break
        if not film:
            print("Lütfen bir film adı girin.")
            continue
        
        # Film ara
        veri = film_ara_ve_kaydet_json(film, API_KEY)
        
        # Eğer film bulunduysa, JSON dosyasına kaydet
        if veri:
            json_dosyasina_kaydet(veri)