"""
CSS seçici (selector) mantığı
select() ve select_one() kullanımı
Gerçek bir haber sitesinden başlık çekme (örnek: BBC, TRT, Hürriyet)

"""

"""
div Tüm <div>etiketleri
.title class="title" olanlar
#main id="main" olan
div.title class="title" olan div'ler
a[href] href özniteliği olan linkler
p > span p'nin doğrudan çocuğu olan span'lar
"""
import requests
from bs4 import BeautifulSoup
url = "https://www.trthaber.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# CSS seçici ile haber başlıklarını al
headlines = soup.select("div.title a")

for headline in headlines[:10]:  # İlk 10 başlık
    print(headline.text.strip())
    print("Link:", headline.get("href"))
    print("-" * 40)