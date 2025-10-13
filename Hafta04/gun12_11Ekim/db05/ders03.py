# Örnek 3: İlişkisel Tablolar - Öğrenci Not Sistemi
import sqlite3

class OgrenciNotSistemi:
    """Öğrenci not takip sistemi - İlişkisel tablo örneği"""
    
    def __init__(self, db_adi="ogrenci_not.db"):
        self.db_adi = db_adi
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        """Veritabanı bağlantısı oluşturur ve tabloları hazırlar"""
        try:
            self.baglanti = sqlite3.connect(self.db_adi)
            self.imlec = self.baglanti.cursor()
            
            # Öğrenciler tablosu
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS ogrenciler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ogrenci_no TEXT UNIQUE NOT NULL,
                    ad TEXT NOT NULL,
                    soyad TEXT NOT NULL,
                    sinif TEXT NOT NULL,
                    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Dersler tablosu
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS dersler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ders_kodu TEXT UNIQUE NOT NULL,
                    ders_adi TEXT NOT NULL,
                    ogretmen TEXT NOT NULL,
                    kredi INTEGER DEFAULT 1
                )
            ''')
            
            # Notlar tablosu (ilişkisel tablo)
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS notlar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ogrenci_id INTEGER,
                    ders_id INTEGER,
                    vize_notu REAL DEFAULT 0,
                    final_notu REAL DEFAULT 0,
                    ortalama REAL DEFAULT 0,
                    harf_notu TEXT,
                    donem TEXT,
                    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler (id),
                    FOREIGN KEY (ders_id) REFERENCES dersler (id),
                    UNIQUE(ogrenci_id, ders_id, donem)
                )
            ''')
            
            self.baglanti.commit()
            print("✅ Öğrenci not sistemi tabloları hazırlandı!")
            
        except sqlite3.Error as hata:
            print(f"❌ Veritabanı hatası: {hata}")
    
    def ornek_verileri_ekle(self):
        """Örnek verileri ekler"""
        try:
            # Öğrenci ekle
            ogrenciler = [
                ("2023001", "Ali", "Yılmaz", "10-A"),
                ("2023002", "Ayşe", "Kaya", "10-B"),
                ("2023003", "Mehmet", "Demir", "10-A"),
                ("2023004", "Zeynep", "Şahin", "10-B")
            ]
            
            self.imlec.executemany('''
                INSERT OR IGNORE INTO ogrenciler (ogrenci_no, ad, soyad, sinif)
                VALUES (?, ?, ?, ?)
            ''', ogrenciler)
            
            # Ders ekle
            dersler = [
                ("MAT101", "Matematik", "Ahmet Hoca", 4),
                ("FIZ101", "Fizik", "Mehmet Hoca", 3),
                ("KIM101", "Kimya", "Ayşe Hoca", 3),
                ("BIO101", "Biyoloji", "Zeynep Hoca", 2)
            ]
            
            self.imlec.executemany('''
                INSERT OR IGNORE INTO dersler (ders_kodu, ders_adi, ogretmen, kredi)
                VALUES (?, ?, ?, ?)
            ''', dersler)
            
            # Not ekle
            notlar = [
                (1, 1, 75, 80, 0, "", "2023-1"),
                (1, 2, 65, 70, 0, "", "2023-1"),
                (2, 1, 85, 90, 0, "", "2023-1"),
                (2, 3, 78, 82, 0, "", "2023-1"),
                (3, 2, 55, 60, 0, "", "2023-1"),
                (3, 4, 70, 75, 0, "", "2023-1"),
                (4, 1, 92, 88, 0, "", "2023-1"),
                (4, 2, 88, 85, 0, "", "2023-1")
            ]
            
            self.imlec.executemany('''
                INSERT OR IGNORE INTO notlar (ogrenci_id, ders_id, vize_notu, final_notu, ortalama, harf_notu, donem)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', notlar)
            
            self.baglanti.commit()
            print("✅ Örnek veriler eklendi!")
            
        except sqlite3.Error as hata:
            print(f"❌ Örnek veri ekleme hatası: {hata}")
    
    def not_hesapla_ve_guncelle(self):
        """Not ortalamalarını hesaplar ve harf notlarını günceller"""
        try:
            # Tüm not kayıtlarını al
            self.imlec.execute("SELECT id, vize_notu, final_notu FROM notlar")
            not_kayitlari = self.imlec.fetchall()
            
            for kayit in not_kayitlari:
                kayit_id, vize, final = kayit
                
                # Ortalama hesapla (vize %40, final %60)
                ortalama = (vize * 0.4) + (final * 0.6)
                
                # Harf notunu belirle
                if ortalama >= 90:
                    harf_notu = "AA"
                elif ortalama >= 85:
                    harf_notu = "BA"
                elif ortalama >= 80:
                    harf_notu = "BB"
                elif ortalama >= 75:
                    harf_notu = "CB"
                elif ortalama >= 70:
                    harf_notu = "CC"
                elif ortalama >= 65:
                    harf_notu = "DC"
                elif ortalama >= 60:
                    harf_notu = "DD"
                elif ortalama >= 50:
                    harf_notu = "FD"
                else:
                    harf_notu = "FF"
                
                # Güncelle
                self.imlec.execute('''
                    UPDATE notlar SET ortalama = ?, harf_notu = ? WHERE id = ?
                ''', (ortalama, harf_notu, kayit_id))
            
            self.baglanti.commit()
            print("✅ Not ortalamaları hesaplandı ve güncellendi!")
            
        except sqlite3.Error as hata:
            print(f"❌ Not hesaplama hatası: {hata}")
    
    def ogrenci_not_listesi(self, ogrenci_id=None):
        """Öğrencilerin not listesini getirir (JOIN kullanarak)"""
        try:
            if ogrenci_id:
                # Belirli bir öğrencinin notları
                sorgu = '''
                    SELECT 
                        o.ogrenci_no, o.ad, o.soyad, o.sinif,
                        d.ders_kodu, d.ders_adi, d.ogretmen,
                        n.vize_notu, n.final_notu, n.ortalama, n.harf_notu, n.donem
                    FROM notlar n
                    JOIN ogrenciler o ON n.ogrenci_id = o.id
                    JOIN dersler d ON n.ders_id = d.id
                    WHERE o.id = ?
                    ORDER BY d.ders_adi
                '''
                self.imlec.execute(sorgu, (ogrenci_id,))
            else:
                # Tüm öğrencilerin notları
                sorgu = '''
                    SELECT 
                        o.ogrenci_no, o.ad, o.soyad, o.sinif,
                        d.ders_kodu, d.ders_adi, d.ogretmen,
                        n.vize_notu, n.final_notu, n.ortalama, n.harf_notu, n.donem
                    FROM notlar n
                    JOIN ogrenciler o ON n.ogrenci_id = o.id
                    JOIN dersler d ON n.ders_id = d.id
                    ORDER BY o.ad, d.ders_adi
                '''
                self.imlec.execute(sorgu)
            
            return self.imlec.fetchall()
            
        except sqlite3.Error as hata:
            print(f"❌ Not listesi hatası: {hata}")
            return []
    
    def ders_bazli_istatistik(self, ders_kodu):
        """Ders bazlı istatistikleri hesaplar"""
        try:
            sorgu = '''
                SELECT 
                    COUNT(*) as ogrenci_sayisi,
                    AVG(n.ortalama) as ortalama,
                    MIN(n.ortalama) as min_not,
                    MAX(n.ortalama) as max_not,
                    SUM(CASE WHEN n.harf_notu IN ('AA', 'BA', 'BB', 'CB', 'CC') THEN 1 ELSE 0 END) as gecen_sayisi,
                    SUM(CASE WHEN n.harf_notu IN ('DC', 'DD', 'FD', 'FF') THEN 1 ELSE 0 END) as kalan_sayisi
                FROM notlar n
                JOIN dersler d ON n.ders_id = d.id
                WHERE d.ders_kodu = ?
            '''
            
            self.imlec.execute(sorgu, (ders_kodu,))
            istatistik = self.imlec.fetchone()
            
            return istatistik
            
        except sqlite3.Error as hata:
            print(f"❌ İstatistik hatası: {hata}")
            return None
    
    def baglanti_kapat(self):
        """Bağlantıyı kapatır"""
        if self.baglanti:
            self.baglanti.close()

# İlişkisel tablo kullanımı
print("\n=== İLİŞKİSEL TABLOLAR: ÖĞRENCİ NOT SİSTEMİ ===")

# Sistem nesnesi oluştur
not_sistemi = OgrenciNotSistemi()

# Örnek verileri ekle
not_sistemi.ornek_verileri_ekle()

# Notları hesapla ve güncelle
not_sistemi.not_hesapla_ve_guncelle()

# Öğrenci not listesi
print("\n--- ALİ YILMAZ'IN NOT LİSTESİ ---")
ali_notlari = not_sistemi.ogrenci_not_listesi(1)
for not_kaydi in ali_notlari:
    print(f"Ders: {not_kaydi[5]}, Vize: {not_kaydi[7]}, Final: {not_kaydi[8]}, "
          f"Ortalama: {not_kaydi[9]:.1f}, Harf: {not_kaydi[10]}")

# Tüm öğrencilerin notları
print("\n--- TÜM ÖĞRENCİLERİN NOT LİSTESİ ---")
tum_notlar = not_sistemi.ogrenci_not_listesi()
for not_kaydi in tum_notlar[:6]:  # İlk 6 kaydı göster
    print(f"Öğrenci: {not_kaydi[1]} {not_kaydi[2]}, Ders: {not_kaydi[5]}, "
          f"Ortalama: {not_kaydi[9]:.1f}, Harf: {not_kaydi[10]}")

# Ders bazlı istatistik
print("\n--- MATEMATİK DERSİ İSTATİSTİKLERİ ---")
mat_istatistik = not_sistemi.ders_bazli_istatistik("MAT101")
if mat_istatistik:
    print(f"Öğrenci Sayısı: {mat_istatistik[0]}")
    print(f"Sınıf Ortalaması: {mat_istatistik[1]:.2f}")
    print(f"En Düşük Not: {mat_istatistik[2]:.1f}")
    print(f"En Yüksek Not: {mat_istatistik[3]:.1f}")
    print(f"Geçen Öğrenci: {mat_istatistik[4]}")
    print(f"Kalan Öğrenci: {mat_istatistik[5]}")

# Bağlantıyı kapat
not_sistemi.baglanti_kapat()