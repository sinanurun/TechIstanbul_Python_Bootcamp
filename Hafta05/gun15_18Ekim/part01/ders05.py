"""
find_element vs find_elements
find_element: İlk eşleşen elementi döndürür (tekil)
find_elements: Tüm eşleşen elementleri liste olarak döndürür
"""
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
    # Betik bittiğinde tarayıcının açık kalmasını sağlar
    options.add_experimental_option("detach", True)
    
    # Driver'ı başlat
    driver = webdriver.Chrome(service=service, options=options)
    
    # Bekleme süresi ayarı
    driver.implicitly_wait(10)  # Element bulunana kadar max 10 saniye bekle
    



    return driver


def element_finding_methods():
    """
    Farklı element bulma yöntemleri
    """
    driver = setup_driver()
    
    try:
        driver.get("https://www.hepsiburada.com/")

        try:
            kabul_et_butonu = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            kabul_et_butonu.click()
            print("✅ Çerez kabul butonu tıklandı.")
        except Exception:
            # Buton bulunamazsa veya tıklanamazsa devam et (bazen pop-up çıkmayabilir)
            print("⚠️ Çerez kabul butonu bulunamadı/gerek kalmadı, devam ediliyor.")
            pass
            
        time.sleep(2) # Pop-up kapandıktan sonra sayfanın stabil hale gelmesini bekle
        
        # FARKLI ELEMENT BULMA YÖNTEMLERİ:
        
        # 1. ID ile bulma
        # element = driver.find_element(By.ID, "element-id")
        # element = driver.find_element(By.ID, "seo-root")
        # print(element.text)

        # 2. Name ile bulma
        # element = driver.find_element(By.NAME, "element-name")
        # element = driver.find_element(By.NAME, "element-name")
        
        # 3. Class Name ile bulma
        # element = driver.find_element(By.CLASS_NAME, "class_name")
        # element = driver.find_element(By.CLASS_NAME, "productCard-module_article__HJ97o")
        # print(element.text)
    
        # 4. Tag Name ile bulma
        # element = driver.find_element(By.TAG_NAME, "h1")
        # element = driver.find_element(By.TAG_NAME, "h1")
        # print(element.text)
        
        # 5. CSS Selector ile bulma
        # element = driver.find_element(By.CSS_SELECTOR, "div.class-name")

        # element = driver.find_element(By.CSS_SELECTOR, "div.qYMgrDY_H1477kqFiDOb")
        # print(element.text)
        # print("/"*50)
        # time.sleep(2)
        # element2 = driver.find_element(By.CSS_SELECTOR, "div.productCard-module_productCardRoot__Yf7qs")
        # print(element2.text)

        # element3 = driver.find_element(By.CSS_SELECTOR, "article.productCard-module_article__HJ97o")
        # print(element3.text)
        # time.sleep(2)
        
        # 6. XPath ile bulma
        # element = driver.find_element(By.XPATH, "//div[@id='main']")
        # element = driver.find_element(By.XPATH, '//*[@id="container"]/main/div[1]/div/section[3]/div/div[2]/div/article[3]/a/div')
        # print(element.text)
        # time.sleep(2)

        #6.1 manuel xpath yazma

        # element = driver.find_element(By.XPATH, '//h2[@class="title-module_titleRoot__dNDiZ"]')
        # print(element.text)
        # time.sleep(5)

        # 7. Link Text ile bulma
        # element = driver.find_element(By.LINK_TEXT, "Tıkla")
        # element = driver.find_element(By.LINK_TEXT, "Hakkımızda")
        # print(element.get_attribute("href"))
        # time.sleep(2)
        
        # 8. Partial Link Text ile bulma
        # element = driver.find_element(By.PARTIAL_LINK_TEXT, "Tık")
        # element = driver.find_element(By.PARTIAL_LINK_TEXT, "Gücü")
        # print(element.get_attribute("href"))
        # time.sleep(2)
        # element.click()
        # time.sleep(10)

        # ÖRNEK: Tüm başlıkları bul
        # headings = driver.find_elements(By.TAG_NAME, "h2")
        # print(f"📊 {len(headings)} tane h2 başlığı bulundu")
        
        # for i, heading in enumerate(headings, 1):
        #     print(f"{i}. {heading.text}")

        # time.sleep(3)
        
        # basliklar= driver.find_elements(By.CSS_SELECTOR, "span.title-module_titleText__8FlNQ")
        # print(f"📊 {len(basliklar)} tane h2 başlığı bulundu")
        
        # for i, baslik in enumerate(basliklar, 1):
        #     print(f"{i}. {baslik.text}")
        
        # time.sleep(2)

        element = driver.find_element(By.LINK_TEXT, "Hakkımızda")
        print(element.get_attribute("href"))
        element.click()
        driver.implicitly_wait(10)

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        # pass
        driver.quit()

# Çalıştır
element_finding_methods()