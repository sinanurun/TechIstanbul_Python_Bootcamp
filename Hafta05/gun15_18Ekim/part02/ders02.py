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

def fill_demoqa_form():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)
    
    FORM_URL = "https://demoqa.com/automation-practice-form"
    
    try:
        driver.get(FORM_URL)
        print("Sayfa yüklendi: DemoQA Pratik Formu.")
        
        # Sayfayı kaydırma (scrolling) ve görünürlük ayarlaması için JavaScript Executor
        # Bazı butonlar footer veya reklamlardan dolayı görünmez olabilir.
        driver.execute_script("window.scrollTo(0, 300);")
        
        # --- 1. Temel Bilgileri Doldurma ---
        
        # Ad (First Name)
        wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Deniz")
        
        # Soyad (Last Name)
        driver.find_element(By.ID, "lastName").send_keys("Yılmaz")
        
        # Email
        driver.find_element(By.ID, "userEmail").send_keys("deniz.yilmaz@testmail.com")
        
        # --- 2. Radyo Butonlarını Seçme (Gender) ---
        
        # 'Male' radyo butonunu seçme
        # Radyo butonu elementinin kendisi genellikle gizlidir, bu yüzden 
        # etiketi (label) aracılığıyla tıklamak veya JavaScript kullanmak gerekir.
        try:
            # label'ın 'for' özelliği ID'ye eşit olanı bul (veya CSS seçici kullan)
            gender_label = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
            gender_label.click()
            print("✅ Cinsiyet (Male) seçildi.")
        except Exception:
            # Alternatif olarak JavaScript ile tıklama (en güvenilir yol)
            driver.execute_script("document.getElementById('gender-radio-1').click();")
            
        # --- 3. Cep Telefonu (Mobile) ---
        driver.find_element(By.ID, "userNumber").send_keys("5551234567")

        # --- 4. Takvim (Date of Birth) ---
        # Takvim kutusunu tıklayarak açıyoruz
        date_input = driver.find_element(By.ID, "dateOfBirthInput")
        date_input.click()
        
        # Yıl Seçimi (Örn: 1990)
        driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").click()
        driver.find_element(By.XPATH, "//option[text()='1990']").click()
        
        # Ay Seçimi (Örn: Eylül)
        driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").click()
        driver.find_element(By.XPATH, "//option[text()='September']").click()
        
        # Gün Seçimi (Örn: 15)
        # Class adına göre günü buluyoruz
        driver.find_element(By.XPATH, "//div[text()='15']").click() 
        print("✅ Doğum Tarihi seçildi (15 Sep 1990).")

        # --- 5. Konular (Subjects) ---
        subjects_input = driver.find_element(By.ID, "subjectsInput")
        
        # İlk konuyu yazıp Enter'a basıyoruz
        subjects_input.send_keys("Comp") 
        subjects_input.send_keys(Keys.ENTER)
        
        # İkinci konuyu yazıp Enter'a basıyoruz
        subjects_input.send_keys("Maths")
        subjects_input.send_keys(Keys.ENTER)
        print("✅ Konular seçildi.")

        # --- 6. Onay Kutuları (Hobbies) ---
        
        # Spor (Sports) onay kutusunu seçme (ID: 'hobbies-checkbox-1')
        # Onay kutuları da genellikle gizlidir, label veya JavaScript ile tıklanır.
        
        # JavaScript ile Sports'a tıklama
        driver.execute_script("document.getElementById('hobbies-checkbox-1').click();")
        
        # Okuma (Reading) onay kutusunu seçme
        driver.execute_script("document.getElementById('hobbies-checkbox-2').click();")
        print("✅ Hobiler seçildi.")

        driver.find_element(By.ID, "hobbies-checkbox-3").click()

        # --- 7. Resim Yükleme (Picture Upload) ---
        # NOTE: Bu kısım sadece yerel makinenizde bir dosya varsa çalışır.
        # Bu dosyanın tam yolunu buraya yazmalısınız.
        resim_yolu = os.path.abspath("test_image.jpg") 
        driver.find_element(By.ID, "uploadPicture").send_keys(resim_yolu)
        
        # --- 8. Adres (Current Address) ---
        driver.find_element(By.ID, "currentAddress").send_keys("Deneme Mahallesi, Test Sokak No: 123, İzmir")
        
        # --- 9. Eyalet ve Şehir Seçimi (State and City) ---
        
        # Sayfayı aşağı kaydırarak son elementlerin görünür olmasını sağlıyoruz
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        
        # Eyalet (State) seçimi
        state_input = driver.find_element(By.ID, "react-select-3-input")
        state_input.send_keys("NCR")
        state_input.send_keys(Keys.ENTER)
        
        # Şehir (City) seçimi
        city_input = driver.find_element(By.ID, "react-select-4-input")
        city_input.send_keys("Delhi")
        city_input.send_keys(Keys.ENTER)
        print("✅ Eyalet ve Şehir seçildi.")

        # --- 10. Formu Gönderme ---
        
        # Submit (Gönder) butonuna tıklıyoruz
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        
        print("\nForm başarıyla gönderildi!")
        
        # Modal penceresinin açılmasını ve sonuçların görünmesini bekle
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        
        print("Sonuçlar Modal Penceresinde Görünüyor.")
        time.sleep(10) # Sonuçları görmeniz için bekletiyoruz

    except Exception as e:
        print(f"Form doldurma sırasında hata oluştu: {e}")
    finally:
        pass
        # driver.quit() # detach=True olduğu için açık kalır.

# Çalıştır
fill_demoqa_form()