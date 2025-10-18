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

from selenium.webdriver.common.action_chains import ActionChains

def mouse_keyboard_actions():
    """
    Mouse ve klavye aksiyonları
    """
    driver = setup_driver()
    
    try:
        driver.get("https://the-internet.herokuapp.com/hovers")
        
        # ActionChains oluştur
        actions = ActionChains(driver)
        
        # 1. Mouse hover (üzerine gelme)
        avatar = driver.find_element(By.CLASS_NAME, "figure")
        actions.move_to_element(avatar).perform()
        print("✅ Mouse hover yapıldı")
        
        time.sleep(2)
        
        # 2. Görünen yazıyı kontrol et
        caption = driver.find_element(By.CSS_SELECTOR, ".figcaption h5")
        print(f"📢 Hover sonrası: {caption.text}")
        
        # 3. Double click örneği
        driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")
        
        clickable = driver.find_element(By.ID, "clickable")
        actions.double_click(clickable).perform()
        print("✅ Double click yapıldı")
        
        # 4. Right click (sağ tık)
        actions.context_click(clickable).perform()
        print("✅ Right click yapıldı")
        
        # 5. Drag and drop (sürükle bırak)
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")
        
        actions.drag_and_drop(source, target).perform()
        print("✅ Drag and drop yapıldı")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
    finally:
        driver.quit()

# Çalıştır
mouse_keyboard_actions()