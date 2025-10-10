"""
veri tabanları üzerinde genel olarak 4 farklı tablo işlemi gerçekleştirebiliriz
CRUD (Create, Read, Update, Delete), bir veritabanı uygulamasının temel dört işlemidir.

İşlem	Anlamı	            SQL Komutu
Create	Veri Ekleme	        INSERT
Read	Veri Okuma	        SELECT
Update	Veri Güncelleme	    UPDATE
Delete	Veri Silme	        DELETE
"""
# kitapları okumak için
import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)
imlec = baglanti.cursor()

# Tüm kitapları oku
imlec.execute("SELECT * FROM kitaplar")

# Tek bir sonuç almak için: imlec.fetchone()
# Tüm sonuçları almak için: imlec.fetchall() liste döndürür
kitaplar = imlec.fetchall()

for kitap in kitaplar:
    print(f"ID: {kitap[0]}, Ad: {kitap[1]}, Yazar: {kitap[2]}")

baglanti.close()