from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
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
    # Betik bittiğinde tarayıcının açık kalmasını sağlar
    options.add_experimental_option("detach", True)
    
    # Driver'ı başlat
    driver = webdriver.Chrome(service=service, options=options)
    
    # Bekleme süresi ayarı
    driver.implicitly_wait(10)  # Element bulunana kadar max 10 saniye bekle
    
    return driver

def form_doldurma():
    driver = setup_driver()
    
    try:
        driver.get("https://demoqa.com/automation-practice-form")


        
        # FARKLI ELEMENT BULMA YÖNTEMLERİ:
        
        # 1. firssstalanı  doldurma
        firstName = driver.find_element(By.ID, "firstName")
        firstName.send_keys("Tech")
        time.sleep(1)

        # 2. lastname alanı  doldurma
        lastName = driver.find_element(By.ID, "lastName")
        lastName.send_keys("Istanbul")
        time.sleep(1)

        # 3. lastname alanı  doldurma
        userEmail = driver.find_element(By.ID, "userEmail")
        userEmail.send_keys("info@techistanbul.com")
        time.sleep(1)

        #4 gender seçimi
        radiogender = driver.find_element(By.ID, "gender-radio-1")
        if not radiogender.is_selected():
            radiogender.click()

        time.sleep(1)




    except Exception as e:
        print(f"Hata: {e}")
    finally:
        # pass
        driver.quit()

# Çalıştır
form_doldurma() 


