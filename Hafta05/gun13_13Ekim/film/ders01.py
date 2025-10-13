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