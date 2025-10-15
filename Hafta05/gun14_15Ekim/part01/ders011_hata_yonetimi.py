import requests
from bs4 import BeautifulSoup

def safe_scraping(url):
    """
    Hata yönetimli güvenli scraping fonksiyonu
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
        
    except requests.exceptions.Timeout:
        print("⏰ Timeout: Sayfa çok yavaş")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Hatası: {e}")
        return None
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return None

# Kullanım
soup = safe_scraping("https://github.com")
if soup:
    print("Scraping başarılı!")