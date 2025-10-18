from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver yolunu belirt (kendi yolunuza göre güncelleyin)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()