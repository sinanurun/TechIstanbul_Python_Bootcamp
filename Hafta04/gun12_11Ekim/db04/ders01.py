# db amacı verileri yapılandırmılmış şekilde saklamaz ve sonrasında düzenlemek

# SQLite → küçük, hızlı, dosya tabanlı bir veritabanı
# Hiçbir sunucuya ihtiyaç yok! 

import sqlite3

baglanti = sqlite3.connect("rehber.db")
cursor = baglanti.cursor()
#part 1
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS kisiler (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         isim TEXT NOT NULL,
#         telefon TEXT UNIQUE,
#         email TEXT
#     )
# ''')

# baglanti.commit()  # değişiklikleri kaydet


#part2
# isim = "Ali"
# telefon = "555 123 45 67"
# email = "ali@email.com"

# cursor.execute('''
#     INSERT INTO kisiler (isim, telefon, email)
#     VALUES (?, ?, ?)
# ''', (isim, telefon, email))

# baglanti.commit()

#part 3

# cursor.execute("SELECT * FROM kisiler")
# kayitlar = cursor.fetchall()

# for kayit in kayitlar:
#     print(f"ID: {kayit[0]}, İsim: {kayit[1]}, Telefon: {kayit[2]}")

# part 4

# aranan = "Ali"
# cursor.execute("SELECT * FROM kisiler WHERE isim=?", (aranan,))
# sonuc = cursor.fetchone()

# if sonuc:
#     print(f"Bulundu: {sonuc[1]} - {sonuc[2]}")
# else:
#     print("Kişi bulunamadı.")

# part 5

# yeni_telefon = "555 999 88 77"
# isim = "Ali"

# cursor.execute('''
#     UPDATE kisiler SET telefon=? WHERE isim=?
# ''', (yeni_telefon, isim))

# baglanti.commit()

# if cursor.rowcount == 0:
#     print("Güncellenecek kişi bulunamadı.")
# else:
#     print("Güncelleme başarılı.")

# part 6 

# isim = "Ali"

# cursor.execute("DELETE FROM kisiler WHERE isim=?", (isim,))
# baglanti.commit()

# if cursor.rowcount == 0:
#     print("Silinecek kişi bulunamadı.")
# else:
#     print(f"{isim} rehberden silindi.")