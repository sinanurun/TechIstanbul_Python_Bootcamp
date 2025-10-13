"""
veri tabanları üzerinde genel olarak 4 farklı tablo işlemi gerçekleştirebiliriz
CRUD (Create, Read, Update, Delete), bir veritabanı uygulamasının temel dört işlemidir.

İşlem	Anlamı	            SQL Komutu
Create	Veri Ekleme	        INSERT
Read	Veri Okuma	        SELECT
Update	Veri Güncelleme	    UPDATE
Delete	Veri Silme	        DELETE
"""

#  veri tabanına veri yazdırma
import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)
imlec = baglanti.cursor()

kitap_adi = "Sefiller"
yazar_adi = "Victor Hugo"

# Güvenli veri ekleme yöntemi (SQL Injection'ı engeller)
imlec.execute("INSERT INTO kitaplar VALUES (NULL, ?, ?)", (kitap_adi, yazar_adi))
# NULL: id otomatik artsın demek

baglanti.commit()
print(f"'{kitap_adi}' veritabanına eklendi.")
baglanti.close()