"""
SQLITE TEMEL KAVRAMLARI:
- Veritabanı: Tek bir dosyada saklanan veri koleksiyonu
- Tablo: Verilerin satır ve sütunlarla düzenlendiği yapı
- Sütun: Belirli bir veri tipindeki alan
- Satır: Tek bir kayıt
- PRIMARY KEY: Benzersiz tanımlayıcı
"""

# Örnek 1: SQLite Veritabanı Bağlantısı ve Temel İşlemler
import sqlite3
import os

def basit_veritabani_ornegi():
    """SQLite veritabanı ile temel işlemleri gösterir"""
    
    # Veritabanı dosyasını sil (önceki çalışmaları temizle)
    if os.path.exists("ogrenciler.db"):
        os.remove("ogrenciler.db")
    
    try:
        # Veritabanına bağlan (dosya yoksa oluşturur)
        baglanti = sqlite3.connect("ogrenciler.db")
        imlec = baglanti.cursor()
        
        print("✅ Veritabanı bağlantısı başarılı!")
        
        # Tablo oluştur
        imlec.execute('''
            CREATE TABLE IF NOT EXISTS ogrenciler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL,
                soyad TEXT NOT NULL,
                numara TEXT UNIQUE NOT NULL,
                sinif TEXT NOT NULL,
                not_ortalamasi REAL DEFAULT 0.0,
                kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        print("✅ 'ogrenciler' tablosu oluşturuldu!")
        
        # Veri ekleme - 1. yöntem
        imlec.execute('''
            INSERT INTO ogrenciler (ad, soyad, numara, sinif, not_ortalamasi)
            VALUES (?, ?, ?, ?, ?)
        ''', ("Ali", "Yılmaz", "1001", "10-A", 85.5))
        
        # Veri ekleme - 2. yöntem
        ogrenci_verisi = ("Ayşe", "Kaya", "1002", "10-B", 92.0)
        imlec.execute('''
            INSERT INTO ogrenciler (ad, soyad, numara, sinif, not_ortalamasi)
            VALUES (?, ?, ?, ?, ?)
        ''', ogrenci_verisi)
        
        # Çoklu veri ekleme
        ogrenci_listesi = [
            ("Mehmet", "Demir", "1003", "10-A", 78.0),
            ("Zeynep", "Şahin", "1004", "10-B", 88.5),
            ("Can", "Aksoy", "1005", "10-C", 65.0)
        ]
        
        imlec.executemany('''
            INSERT INTO ogrenciler (ad, soyad, numara, sinif, not_ortalamasi)
            VALUES (?, ?, ?, ?, ?)
        ''', ogrenci_listesi)
        
        # Değişiklikleri kaydet
        baglanti.commit()
        print("✅ Öğrenci verileri eklendi!")
        
        # Verileri okuma
        print("\n--- TÜM ÖĞRENCİLER ---")
        imlec.execute("SELECT * FROM ogrenciler")
        ogrenciler = imlec.fetchall()
        
        for ogrenci in ogrenciler:
            print(f"ID: {ogrenci[0]}, Ad: {ogrenci[1]}, Soyad: {ogrenci[2]}, "
                  f"Numara: {ogrenci[3]}, Sınıf: {ogrenci[4]}, Not: {ogrenci[5]}")
        
        # Toplam kayıt sayısı
        imlec.execute("SELECT COUNT(*) FROM ogrenciler")
        kayit_sayisi = imlec.fetchone()[0]
        print(f"\n📊 Toplam kayıt sayısı: {kayit_sayisi}")
        
    except sqlite3.Error as hata:
        print(f"❌ Veritabanı hatası: {hata}")
    
    finally:
        # Bağlantıyı kapat
        if baglanti:
            baglanti.close()
            print("✅ Veritabanı bağlantısı kapatıldı.")

# Temel örneği çalıştır
print("=== SQLITE TEMEL İŞLEMLER ===")
basit_veritabani_ornegi()