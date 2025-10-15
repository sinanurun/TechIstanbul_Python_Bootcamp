# CSS Selector Kullanımı:


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



# CSS selector ile element bulma
print("1. Class selector:", soup.select_one(".container h1").text)
print("2. ID selector:", soup.select_one("#description").text)
print("3. Tüm topic'ler:", soup.select(".topic"))
print("3. Tüm topic'ler:", soup.select(".topic")[0])
print("3. Tüm topic'ler:", soup.select(".topic")[0].text)

# CSS selector ile liste
all_topics = soup.select(".topic")
for topic in all_topics:
    print("Konu:", topic.text)