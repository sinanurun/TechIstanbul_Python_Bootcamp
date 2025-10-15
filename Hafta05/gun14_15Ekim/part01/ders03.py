# Örnek HTML içeriği
from bs4 import BeautifulSoup
html_doc = """
<html>
<head><title>Öğrenci Listesi</title></head>
<body>
    <div class="students">
        <h1 id="class-title">10-A Sınıfı</h1>
        <ul>
            <li class="student">Ahmet Yılmaz</li>
            <li class="student">Ayşe Demir</li>
            <li class="student">Mehmet Kaya</li>
        </ul>
    </div>
</body>
</html>
"""

# BeautifulSoup ile analiz
soup = BeautifulSoup(html_doc, 'html.parser')

# Farklı şekillerde element bulma:
print("1. Tag ismi ile:", soup.title.text)
print("2. ID ile:", soup.find(id="class-title").text)
print("3. Class ile:", soup.find(class_="student").text)

# Tüm student'ları bulma
students = soup.find_all(class_="student")
for student in students:
    print("Öğrenci:", student.text)