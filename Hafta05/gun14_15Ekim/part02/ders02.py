import requests
from bs4 import BeautifulSoup

url = "https://tech.istanbul/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# Sayfa başlığını al
title = soup.find("title").text
print("Sayfa Başlığı:", title)

# Tüm paragrafları al
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)

"""
Temel Metotlar:
soup.find("tag", class_="class-adi")
soup.find_all("tag", {"class": "class-adi"})
.get("href") → bağlantı almak için
.text → etiket içi metni almak için
💡 Not: class Python'da ayrılmış kelime olduğu için class_ (alt çizgili) yazılır. 

"""