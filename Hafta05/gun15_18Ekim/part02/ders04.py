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

def fill_contact_form():
    """
    İletişim formu doldurma örneği
    """
    driver = setup_driver()
    
    try:
        # Test form sitesine git
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        print("✅ Form sayfası açıldı")
        
        # 1. Text input doldur
        text_input = driver.find_element(By.NAME, "my-text")
        text_input.send_keys("Python Selenium Test")
        print("✅ Text input dolduruldu")
        
        # 2. Password input doldur
        password_input = driver.find_element(By.NAME, "my-password")
        password_input.send_keys("test123")
        print("✅ Password dolduruldu")
        
        # 3. Textarea doldur
        textarea = driver.find_element(By.NAME, "my-textarea")
        textarea.send_keys("Bu bir otomatik test mesajıdır.")
        print("✅ Textarea dolduruldu")
        
        # 4. Dropdown seçimi
        from selenium.webdriver.support.ui import Select
        
        dropdown = Select(driver.find_element(By.NAME, "my-select"))
        dropdown.select_by_visible_text("Two")
        print("✅ Dropdown seçildi")
        
        # 5. Date picker
        date_picker = driver.find_element(By.NAME, "my-date")
        date_picker.send_keys("12122024")
        print("✅ Tarih seçildi")
        
        # 6. Checkbox işaretle
        checkbox = driver.find_element(By.ID, "my-check-2")
        if not checkbox.is_selected():
            checkbox.click()
        print("✅ Checkbox işaretlendi")
        
        # 7. Radio button seç
        radio_button = driver.find_element(By.ID, "my-radio-2")
        radio_button.click()
        print("✅ Radio button seçildi")
        
        # 8. Submit butonuna tıkla
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        print("✅ Form gönderildi")
        
        # Sonuç kontrolü
        time.sleep(2)
        success_message = driver.find_element(By.ID, "message")
        print(f"📢 Sonuç: {success_message.text}")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
    finally:
        driver.quit()

# Çalıştır
fill_contact_form()