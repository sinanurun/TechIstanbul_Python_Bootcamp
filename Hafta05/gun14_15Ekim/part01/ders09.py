import requests
from bs4 import BeautifulSoup

def simple_product_scraper():
    """
    Basit bir e-ticaret sitesinden ürün bilgileri çeker
    """
    # Test sitesi (scraping için uygun)
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ürün kartlarını bul
        products = soup.select(".thumbnail")
        
        print("🛒 ÜRÜN LİSTESİ:\n")
        
        for i, product in enumerate(products[:8], 1):
            try:
                # Ürün adı
                name = product.select_one(".title").text.strip()
                
                # Fiyat
                price = product.select_one(".price").text.strip()
                
                # Açıklama
                description = product.select_one(".description").text.strip()
                
                # Değerlendirme
                rating = product.select_one(".ratings p").text.strip()
                
                print(f"{i:2d}. {name}")
                print(f"    💰 {price}")
                print(f"    📝 {description}")
                print(f"    ⭐ {rating}")
                print("-" * 50)
                
            except AttributeError:
                continue
                
    except Exception as e:
        print(f"Hata: {e}")

# Çalıştır
simple_product_scraper()