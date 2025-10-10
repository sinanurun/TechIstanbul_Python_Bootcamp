# Veritabanıyla konuşmak için önce bir bağlantı (connection) kurmalıyız.

#bir veri tabanına bağlandıktan sonra ver tabanı üzerinde işlemler yapmak için 
# bir işaretleyici - imleç yani cursor oluşturmamaız gerekir

# Bağlantıyı kurduk, şimdi veritabanına komutlar gönderecek bir işlemci (cursor) oluşturmalıyız. 
# İşlemci, veritabanına sorgu (SQL komutları) göndermek ve sonuçları almak için kullanılır.

import sqlite3

# 'kutuphane.db' adında bir veritabanı dosyasına bağlan.
# Eğer dosya yoksa, otomatik olarak oluşturulur.


import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)

# baglanti = sqlite3.connect('kutuphane.db')

imlec = baglanti.cursor() # İşlemci oluşturuldu
# ... sorgular burada çalışır ...
# Bağlantıyı bitir, bu önemli!
baglanti.close()