"""
veri tabanları üzerinde genel olarak 4 farklı tablo işlemi gerçekleştirebiliriz
CRUD (Create, Read, Update, Delete), bir veritabanı uygulamasının temel dört işlemidir.

İşlem	Anlamı	            SQL Komutu
Create	Veri Ekleme	        INSERT
Read	Veri Okuma	        SELECT
Update	Veri Güncelleme	    UPDATE
Delete	Veri Silme	        DELETE
"""
import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)
imlec = baglanti.cursor()

yeni_ad = "Python"
kitap_id = 1
imlec.execute("UPDATE kitaplar SET ad = ? WHERE id = ?", (yeni_ad, kitap_id))

baglanti.commit()
baglanti.close()
print(f"ID {kitap_id} olan kitabın adı '{yeni_ad}' olarak güncellendi.")