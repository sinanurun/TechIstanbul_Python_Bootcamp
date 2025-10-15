import time
from ders011_hata_yonetimi import safe_scraping

def polite_scraper(urls):
    """
    Sunucuyu yormadan scraping yapar
    """
    for i, url in enumerate(urls, 1):
        print(f"\n🔍 {i}/{len(urls)}. sayfa işleniyor: {url}")
        
        soup = safe_scraping(url)
        if soup:
            # Burada scraping işlemleri yapılır
            title = soup.title.text if soup.title else "Başlık yok"
            print(f"   📄 {title}")
        
        # Bir sonraki istekten önce bekle (1-3 saniye)
        wait_time = 2
        print(f"   ⏳ {wait_time} saniye bekleniyor...")
        time.sleep(wait_time)

# Örnek kullanım
urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/200", 
    "https://httpbin.org/status/200"
]
polite_scraper(urls)