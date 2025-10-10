import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kullanicilar.db"
baglanti = sqlite3.connect(veritabanim)

# Kullanıcılar tablosunu oluştur
def kullanici_tablosu_olustur():
    baglanti = sqlite3.connect(veritabanim)
    imlec = baglanti.cursor()
    imlec.execute("""
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id INTEGER PRIMARY KEY,
        kullanici_adi TEXT UNIQUE, -- Kullanıcı adı benzersiz olmalı
        sifre TEXT
    )
    """)
    baglanti.commit()
    baglanti.close()

kullanici_tablosu_olustur()

def kullanici_kaydi(ad, sifre):
    try:
        baglanti = sqlite3.connect(veritabanim)
        imlec = baglanti.cursor()
        imlec.execute("INSERT INTO kullanicilar VALUES (NULL, ?, ?)", (ad, sifre))
        baglanti.commit()
        print(f"Kullanıcı '{ad}' kaydedildi.")
    except sqlite3.IntegrityError:
        print(f"HATA: '{ad}' kullanıcı adı zaten mevcut.")
    finally:
        if 'baglanti' in locals() and baglanti:
            baglanti.close()

kullanici_kaydi("ali", "1234")
# kullanici_kaydi("ali", "4321") # İkinci denemede hata verir