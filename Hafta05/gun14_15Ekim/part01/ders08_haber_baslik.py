import requests
from bs4 import BeautifulSoup
import time

def scrape_bbc_news_updated():
    """
    Güncel BBC News scraper - CSS selector'lar güncellendi
    """
    url = "https://www.bbc.com/news"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    
    try:
        print("🔗 BBC News'e bağlanılıyor...")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code != 200:
            print(f"❌ Hata: Sayfa yüklenemedi. Status code: {response.status_code}")
            return
        
        print("✅ Sayfa başarıyla yüklendi!")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BBC News'in güncel CSS selector'ları
        # Birden fazla selector deneyelim
        selectors = [
            "h2[data-testid='card-headline']",  # Yeni BBC selector
            "a[data-testid='internal-link'] h2", # Alternatif selector
            "h3[class*='promo-heading']",       # Eski selector (yedek)
            "h2",                               # Tüm h2'ler (son çare)
        ]
        
        headlines = []
        
        for selector in selectors:
            headlines = soup.select(selector)
            if headlines:
                print(f"✅ '{selector}' selector ile {len(headlines)} başlık bulundu")
                break
            else:
                print(f"❌ '{selector}' selector çalışmadı")
        
        if not headlines:
            print("❌ Hiçbir selector çalışmadı. Sayfa yapısı değişmiş olabilir.")
            return
        
        print(f"\n📰 BBC HABER BAŞLIKLARI ({len(headlines)} tane bulundu)\n")
        print("=" * 80)
        
        # Başlıkları filtrele ve göster
        count = 0
        for i, headline in enumerate(headlines, 1):
            title = headline.get_text(strip=True)
            
            # Boş ve çok kısa başlıkları filtrele
            if title and len(title) > 10 and count < 15:
                count += 1
                print(f"{count:2d}. {title}")
        
        print("=" * 80)
        
    except requests.exceptions.Timeout:
        print("⏰ Timeout hatası: BBC sitesi çok yavaş yanıt veriyor")
    except requests.exceptions.RequestException as e:
        print(f"❌ Bağlantı hatası: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

# Çalıştır
scrape_bbc_news_updated()