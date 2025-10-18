"""
Web Elementlerini Bulma Yöntemleri
📌 2.1 Element Bulma Stratejileri
Selenium, HTML elementlerini bulmak için 8 temel yöntem sunar:

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.CLASS_NAME, "class")
find_element(By.TAG_NAME, "div")
find_element(By.XPATH, "//input[@name='q']")
find_element(By.CSS_SELECTOR, "input[name='q']")
find_element(By.LINK_TEXT, "Gmail")
find_element(By.PARTIAL_LINK_TEXT, "Gma")
⚠️ By modülünü import etmeyi unutmayın: 

python

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium") # seçilen eleman içine veri eklenen bir eleman ise içine veri ekleme için
search_box.submit()  # Enter tuşuna basar

driver.implicitly_wait(5)  # Sayfanın yüklenmesi için bekle
print(driver.title)
driver.quit()