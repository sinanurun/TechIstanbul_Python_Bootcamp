from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

import time

def setup_driver():
    """
    Chrome driver'ı otomatik kurar ve ayarlar
    """
    # WebDriver Manager ile otomatik ChromeDriver kurulumu
    service = Service(ChromeDriverManager().install())
    
    # Chrome options (ayarlar)
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Pencereyi büyüt
    options.add_argument('--disable-notifications')  # Bildirimleri kapat
    
    # Driver'ı başlat
    driver = webdriver.Chrome(service=service, options=options)
    
    # Bekleme süresi ayarı
    driver.implicitly_wait(10)  # Element bulunana kadar max 10 saniye bekle
    
    return driver

def first_selenium_test():
    """
    İlk Selenium testimiz - Google'da arama yapma
    """
    driver = setup_driver()
    
    try:
        # 1. Google ana sayfasına git
        driver.get("https://www.google.com")
        print("✅ Google açıldı")
        
        # 2. Arama kutusunu bul
        search_box = driver.find_element(By.NAME, "q")
        print("✅ Arama kutusu bulundu")
        
        
        # 3. Arama kutusuna yazı yaz
        search_box.send_keys("Python programlama")
        print("✅ Arama terimi yazıldı")
        
        # 4. Enter tuşuna bas
        search_box.send_keys(Keys.RETURN)
        print("✅ Arama yapıldı")
        
        # 5. Sonuçları bekle
        time.sleep(3)
        
        # 6. Sayfa başlığını yazdır
        print(f"📄 Sayfa başlığı: {driver.title}")
        
        # 7. Ekran görüntüsü al
        driver.save_screenshot("google_search.png")
        print("📸 Ekran görüntüsü alındı")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
    
    finally:
        # Tarayıcıyı kapat
        time.sleep(2)
        driver.quit()
        print("🔚 Tarayıcı kapatıldı")

# Çalıştır
first_selenium_test()