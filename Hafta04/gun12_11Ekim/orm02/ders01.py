"""
ORM (Object-Relational Mapping) NEDİR?
- Veritabanı tablolarını Python sınıflarına dönüştürme
- SQL sorguları yerine Python kodları yazma
- Veritabanı bağımsız çalışma

GELENEKSEL SQL vs ORM KARŞILAŞTIRMASI:

Geleneksel SQL:
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Ali", "ali@email.com"))

ORM ile:
user = User(name="Ali", email="ali@email.com")
session.add(user)
session.commit()

AVANTAJLAR:
1. Python syntax'ı kullanımı
2. Veritabanı bağımsızlığı
3. Kod okunabilirliği
4. Otomatik SQL injection koruması
5. İlişkilerin kolay yönetimi

DEZAVANTAJLAR:
1. Performans (bazı durumlarda)
2. Öğrenme eğrisi
3. Karmaşık sorgularda sınırlamalar
"""

