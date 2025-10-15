import csv
import json

def save_scraped_data():
    """
    Scraping verilerini dosyaya kaydeder
    """
    # Örnek veri
    products = [
        {"name": "Python Kitabı", "price": "50 TL", "rating": "4.5"},
        {"name": "JavaScript Kitabı", "price": "45 TL", "rating": "4.2"},
        {"name": "HTML/CSS Kitabı", "price": "40 TL", "rating": "4.0"}
    ]
    
    # CSV dosyasına kaydet
    with open('urunler.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    
    print("✅ Veriler urunler.csv dosyasına kaydedildi")
    
    # JSON dosyasına kaydet
    with open('urunler.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(products, jsonfile, ensure_ascii=False, indent=2)
    
    print("✅ Veriler urunler.json dosyasına kaydedildi")

# Çalıştır
save_scraped_data()