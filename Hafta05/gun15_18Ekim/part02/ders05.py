from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os # Resim yüklemek için gerekebilir

# setup_driver fonksiyonunuzun burada tanımlı olduğunu varsayıyorum 
# (içinde detach=True ve implicitly_wait(10) olmalı)

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
    # Betik bittiğinde tarayıcının açık kalmasını sağlar
    options.add_experimental_option("detach", True)
    
    # Driver'ı başlat
    driver = webdriver.Chrome(service=service, options=options)
    
    # Bekleme süresi ayarı
    driver.implicitly_wait(10)  # Element bulunana kadar max 10 saniye bekle
    
    return driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def explicit_wait_example():
    """
    Explicit wait ile akıllı bekleme
    """
    driver = setup_driver()
    
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        # Start butonunu bul ve tıkla
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()
        print("✅ Start butonuna tıklandı")
        
        # Explicit wait: Element görünene kadar bekle (max 10 saniye)
        wait = WebDriverWait(driver, 10)
        
        # Hello World yazısının görünmesini bekle
        hello_text = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        
        print(f"✅ Element bulundu: {hello_text.text}")
        
        # Farklı bekleme koşulları:
        # EC.presence_of_element_located()  # Element sayfada var
        # EC.element_to_be_clickable()      # Element tıklanabilir
        # EC.text_to_be_present_in_element() # Element belirli metni içeriyor
        # EC.invisibility_of_element()      # Element görünmez
        
    except Exception as e:
        print(f"❌ Hata: {e}")
    finally:
        driver.quit()

# Çalıştır
explicit_wait_example()