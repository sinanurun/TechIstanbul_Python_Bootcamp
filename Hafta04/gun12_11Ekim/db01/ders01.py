"""
1. Veritabanı Nedir ve Neden Gerekli? (30 Dakika)
Nedir?: Verilerin organize edilmiş bir koleksiyonudur. 
Tıpkı bir kütüphanenin kitapları düzenlemesi gibi, veritabanları da bilgileri düzenler.

Neden?: Programımız kapandığında kaybolmasını istemediğimiz bilgileri (kullanıcı bilgileri, ürün listesi, notlar vb.) 
kalıcı olarak saklamak için gereklidir.


SQLite Nedir?: Veritabanının tamamını tek bir dosyada saklayan, hafif ve kurulum gerektirmeyen bir veritabanı motorudur. 
Python ile kullanması çok kolaydır.
"""

# Python'da veritabanı işlemlerini yapmak için standart olarak gelen sqlite3 modülünü kullanılır.

# Veritabanıyla konuşmak için önce bir bağlantı (connection) kurmalıyız.

import sqlite3

# 'kutuphane.db' adında bir veritabanı dosyasına bağlan.
# Eğer dosya yoksa, otomatik olarak oluşturulur.


# import os
# bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
# veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
# baglanti = sqlite3.connect(veritabanim)

baglanti = sqlite3.connect('kutuphane.db')


# Bağlantıyı bitir, bu önemli!
baglanti.close()

# Dosya işlemlerinde de olduğu gibi bir veritabanı bağlantısı yaptığımız zaman muhakkak bağlantıyı kapatmalıyız