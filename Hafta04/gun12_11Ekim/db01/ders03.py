"""
Veritabanına komutlar göndermek için SQL (Structured Query Language) denilen özel bir dil kullanılır.

Tablo Oluşturma (CREATE TABLE): Verilerimizi düzenli sütunlar (alanlar) halinde tutmak için bir "tablo" oluşturmalıyız.
"""
"""
CREATE TABLE kitaplar (
    kitap_id INTEGER PRIMARY KEY, -- Benzersiz numara
    isim TEXT,                     -- Kitap adı (Metin)
    yazar TEXT,                    -- Yazar adı (Metin)
    sayfa_sayisi INTEGER           -- Sayfa sayısı (Sayı)
)
"""

import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)
imlec = baglanti.cursor()

# Tablo oluşturma sorgusu
imlec.execute("""
CREATE TABLE IF NOT EXISTS kitaplar (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    yazar TEXT
)
""")

baglanti.commit() # Değişiklikleri kaydet eğer imleç aralıcığı ile gerçekleştirdiğimiz işlemler var ise
# 
baglanti.close()
print("Kitaplar tablosu oluşturuldu (veya zaten vardı).")