import requests
from bs4 import BeautifulSoup
def product_scraper_with_images():
    """
    Ürün bilgileri + görseller
    """
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        products = soup.select(".thumbnail")
        
        print("📸 ÜRÜNLER VE GÖRSELLER:\n")
        
        for i, product in enumerate(products[:5], 1):
            try:
                name = product.select_one(".title").text.strip()
                price = product.select_one(".price").text.strip()
                
                # Görsel URL'si
                img = product.select_one("img")
                if img and img.get('src'):
                    image_url = "https://webscraper.io" + img['src']
                else:
                    image_url = "Görsel yok"
                
                print(f"{i}. {name}")
                print(f"   💰 {price}")
                print(f"   🖼️  {image_url}")
                print("-" * 60)
                
            except AttributeError:
                continue
                
    except Exception as e:
        print(f"Hata: {e}")

# Çalıştır
product_scraper_with_images()