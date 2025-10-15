# 1. Gerekli kütüphaneleri import edelim
import requests
from bs4 import BeautifulSoup

# 2. Basit bir web sitesinden veri çekelim
url = "https://google.com"

# 3. Web sitesine istek gönderelim
response = requests.get(url)

# 4. Durum kodunu kontrol edelim
print("Status Code:", response.status_code)  # 200 = Başarılı

# 5. İçeriği BeautifulSoup ile analiz edelim
soup = BeautifulSoup(response.text, "html.parser")

# 6. Sayfa başlığını alalım
print("Sayfa Başlığı:", soup.title.text)