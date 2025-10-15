#element bulma yöntemleri

#1. find() - Tek Element Bulma:

import requests
from bs4 import BeautifulSoup

# Örnek HTML
html_content = """
<div class="container">
    <h1>Python Kursu</h1>
    <p id="description">Python programlama dili eğitimi</p>
    <ul>
        <li class="topic">Değişkenler</li>
        <li class="topic">Fonksiyonlar</li>
        <li class="topic">Döngüler</li>
    </ul>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# find() kullanım örnekleri:
print("1. Tag ile:", soup.find("h1").text)
print("2. ID ile:", soup.find(id="description").text)
print("3. Class ile:", soup.find(class_="topic").text)
print("4. Attribute ile:", soup.find(attrs={"class": "container"}).text)
print("4. Attribute ile:", soup.find(attrs={"class": "container"}).text[:20])