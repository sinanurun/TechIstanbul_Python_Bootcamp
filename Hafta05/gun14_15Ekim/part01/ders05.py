#2. find_all() - Tüm Elementleri Bulma:

# find_all() kullanımı

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



topics = soup.find_all("li")  # Tüm <li> elementleri
print("Toplam konu sayısı:", len(topics))

for i, topic in enumerate(topics, 1):
    print(f"{i}. {topic.text}")