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

def automated_login_test():
    """
    Test sitesinde otomatik giriş yapma
    """
    driver = setup_driver()
    
    try:
        # Test login sitesine git
        driver.get("https://the-internet.herokuapp.com/login")
        print("✅ Login sayfası açıldı")
        
        # Kullanıcı adı alanını bul ve doldur
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("✅ Kullanıcı adı yazıldı")
        
        # Şifre alanını bul ve doldur
        password_field = driver.find_element(By.ID, "password") 
        password_field.send_keys("SuperSecretPassword!")
        print("✅ Şifre yazıldı")
        
        # Login butonunu bul ve tıkla
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("✅ Login butonuna tıklandı")
        
        # Giriş başarılı mı kontrol et
        time.sleep(2)
        
        if "secure" in driver.current_url:
            print("🎉 Başarılı giriş!")
            
            # Başarı mesajını kontrol et
            success_message = driver.find_element(By.ID, "flash")
            print(f"📢 Mesaj: {success_message.text}")
            
        else:
            print("❌ Giriş başarısız!")
            
        # Ekran görüntüsü al
        driver.save_screenshot("login_result.png")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
        driver.save_screenshot("login_error.png")
        
    finally:
        time.sleep(3)
        driver.quit()

# Çalıştır
automated_login_test()