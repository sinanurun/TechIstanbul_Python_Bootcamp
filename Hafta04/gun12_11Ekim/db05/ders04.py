# ders03 daha detaylı anlatımı ders sonrası tekrar için

"""
ÖĞRENCİ NOT SİSTEMİ - DETAYLI AÇIKLAMALI
Bu örnek, SQLite veritabanı kullanarak ilişkisel tabloların nasıl oluşturulduğunu
ve kullanıldığını gösterir. 3 ana tablo ve aralarında ilişkiler bulunur.
"""

# SQLite veritabanı kütüphanesini içe aktarıyoruz
import sqlite3
import os  # Dosya işlemleri için

class OgrenciNotSistemi:
    """
    ÖĞRENCİ NOT TAKİP SİSTEMİ SINIFI
    Bu sınıf, öğrenci, ders ve not bilgilerini yönetir.
    İlişkisel veritabanı kullanarak verileri saklar.
    """
    
    def __init__(self, db_adi="ogrenci_not.db"):
        """
        Yapıcı metot - Sınıf oluşturulduğunda çalışır
        db_adi: Veritabanı dosyasının adı (varsayılan: ogrenci_not.db)
        """
        self.db_adi = db_adi
        self.baglanti_olustur()  # Veritabanı bağlantısını başlat
    
    def baglanti_olustur(self):
        """
        VERİTABANI BAĞLANTISI OLUŞTURMA
        - Veritabanı dosyasına bağlanır (yoksa oluşturur)
        - Gerekli tabloları oluşturur
        - Hata durumlarını yönetir
        """
        try:
            # SQLite veritabanına bağlan
            # check_same_thread=False: Çoklu iş parçacığı desteği için
            self.baglanti = sqlite3.connect(self.db_adi)
            
            # SQL komutlarını çalıştırmak için imleç (cursor) oluştur
            self.imlec = self.baglanti.cursor()
            
            print("🔗 Veritabanı bağlantısı başlatılıyor...")
            
            # 1. TABLO: ÖĞRENCİLER
            # Öğrenci bilgilerini saklayacak ana tablo
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS ogrenciler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- Otomatik artan benzersiz numara
                    ogrenci_no TEXT UNIQUE NOT NULL,             -- Benzersiz öğrenci numarası
                    ad TEXT NOT NULL,                           -- Öğrenci adı
                    soyad TEXT NOT NULL,                        -- Öğrenci soyadı
                    sinif TEXT NOT NULL,                        -- Sınıf bilgisi (10-A, 11-B vb.)
                    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Otomatik kayıt tarihi
                )
            ''')
            print("✅ 'ogrenciler' tablosu hazır!")
            
            # 2. TABLO: DERSLER
            # Ders bilgilerini saklayacak tablo
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS dersler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- Otomatik artan benzersiz numara
                    ders_kodu TEXT UNIQUE NOT NULL,             -- Benzersiz ders kodu (MAT101, FIZ101 vb.)
                    ders_adi TEXT NOT NULL,                     -- Dersin adı
                    ogretmen TEXT NOT NULL,                     -- Dersin öğretmeni
                    kredi INTEGER DEFAULT 1                     -- Dersin kredi değeri
                )
            ''')
            print("✅ 'dersler' tablosu hazır!")
            
            # 3. TABLO: NOTLAR (İLİŞKİSEL TABLO)
            # Öğrenci ve ders tablolarını birleştiren, not bilgilerini saklayan tablo
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS notlar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- Otomatik artan benzersiz numara
                    ogrenci_id INTEGER,                         -- Öğrenci tablosuna referans
                    ders_id INTEGER,                            -- Dersler tablosuna referans
                    vize_notu REAL DEFAULT 0,                   -- Vize notu (ondalıklı sayı)
                    final_notu REAL DEFAULT 0,                  -- Final notu (ondalıklı sayı)
                    ortalama REAL DEFAULT 0,                    -- Hesaplanan ortalama
                    harf_notu TEXT,                             -- Harf notu (AA, BA, BB vb.)
                    donem TEXT,                                 -- Dönem bilgisi (2023-1, 2023-2 vb.)
                    
                    -- YABANCI ANAHTARLAR (FOREIGN KEYS) - İlişkileri tanımlar
                    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler (id),
                    FOREIGN KEY (ders_id) REFERENCES dersler (id),
                    
                    -- BİLEŞİK BENZERSİZLİK KISITI
                    -- Aynı öğrenci aynı ders ve dönemde birden fazla not kaydı olamaz
                    UNIQUE(ogrenci_id, ders_id, donem)
                )
            ''')
            print("✅ 'notlar' tablosu hazır!")
            
            # Tüm değişiklikleri veritabanına kaydet
            self.baglanti.commit()
            print("🎉 Tüm veritabanı tabloları başarıyla oluşturuldu!")
            
        except sqlite3.Error as hata:
            # Veritabanı hatası durumunda
            print(f"❌ Veritabanı hatası oluştu: {hata}")
    
    def ornek_verileri_ekle(self):
        """
        ÖRNEK VERİLERİ EKLEME
        Sistemin test edilmesi için örnek öğrenci, ders ve not kayıtları ekler
        """
        try:
            print("\n📝 Örnek veriler ekleniyor...")
            
            # 1. ÖĞRENCİ VERİLERİ
            # Her öğrenci için: (öğrenci_no, ad, soyad, sınıf)
            ogrenciler = [
                ("2023001", "Ali", "Yılmaz", "10-A"),
                ("2023002", "Ayşe", "Kaya", "10-B"),
                ("2023003", "Mehmet", "Demir", "10-A"),
                ("2023004", "Zeynep", "Şahin", "10-B")
            ]
            
            # Çoklu kayıt ekleme - executemany()
            self.imlec.executemany('''
                INSERT OR IGNORE INTO ogrenciler (ogrenci_no, ad, soyad, sinif)
                VALUES (?, ?, ?, ?)
            ''', ogrenciler)
            print("✅ Öğrenci verileri eklendi!")
            
            # 2. DERS VERİLERİ
            # Her ders için: (ders_kodu, ders_adi, ogretmen, kredi)
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
            print("✅ Ders verileri eklendi!")
            
            # 3. NOT VERİLERİ
            # Her not kaydı için: (ogrenci_id, ders_id, vize, final, ortalama, harf_notu, donem)
            notlar = [
                (1, 1, 75, 80, 0, "", "2023-1"),  # Ali - Matematik
                (1, 2, 65, 70, 0, "", "2023-1"),  # Ali - Fizik
                (2, 1, 85, 90, 0, "", "2023-1"),  # Ayşe - Matematik
                (2, 3, 78, 82, 0, "", "2023-1"),  # Ayşe - Kimya
                (3, 2, 55, 60, 0, "", "2023-1"),  # Mehmet - Fizik
                (3, 4, 70, 75, 0, "", "2023-1"),  # Mehmet - Biyoloji
                (4, 1, 92, 88, 0, "", "2023-1"),  # Zeynep - Matematik
                (4, 2, 88, 85, 0, "", "2023-1")   # Zeynep - Fizik
            ]
            
            self.imlec.executemany('''
                INSERT OR IGNORE INTO notlar (ogrenci_id, ders_id, vize_notu, final_notu, ortalama, harf_notu, donem)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', notlar)
            print("✅ Not verileri eklendi!")
            
            # Tüm eklemeleri veritabanına kaydet
            self.baglanti.commit()
            print("🎉 Tüm örnek veriler başarıyla eklendi!")
            
        except sqlite3.Error as hata:
            print(f"❌ Örnek veri ekleme hatası: {hata}")
    
    def not_hesapla_ve_guncelle(self):
        """
        NOT ORTALAMALARINI HESAPLAMA VE GÜNCELLEME
        - Vize ve final notlarından ortalamayı hesaplar
        - Ortalamaya göre harf notu belirler
        - Tüm kayıtları günceller
        """
        try:
            print("\n🧮 Not ortalamaları hesaplanıyor...")
            
            # Tüm not kayıtlarını veritabanından al
            # fetchall(): Tüm kayıtları liste olarak getirir
            self.imlec.execute("SELECT id, vize_notu, final_notu FROM notlar")
            not_kayitlari = self.imlec.fetchall()
            
            print(f"📊 {len(not_kayitlari)} adet not kaydı işlenecek...")
            
            # Her not kaydı için işlem yap
            for kayit in not_kayitlari:
                kayit_id, vize, final = kayit  # Kaydı parçalara ayır
                
                # ORTALAMA HESAPLAMA
                # Vize %40, Final %60 ağırlığında
                ortalama = (vize * 0.4) + (final * 0.6)
                
                # HARF NOTU BELİRLEME
                # Not aralıklarına göre harf notu atama
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
                
                # VERİTABANINI GÜNCELLE
                # Hesaplanan değerleri ilgili kayda yaz
                self.imlec.execute('''
                    UPDATE notlar 
                    SET ortalama = ?, harf_notu = ? 
                    WHERE id = ?
                ''', (ortalama, harf_notu, kayit_id))
                
                # İlerlemeyi göster (isteğe bağlı)
                print(f"  📝 Kayıt {kayit_id}: {vize}-{final} → {ortalama:.1f} ({harf_notu})")
            
            # Tüm güncellemeleri kaydet
            self.baglanti.commit()
            print("✅ Tüm not ortalamaları hesaplandı ve güncellendi!")
            
        except sqlite3.Error as hata:
            print(f"❌ Not hesaplama hatası: {hata}")
    
    def ogrenci_not_listesi(self, ogrenci_id=None):
        """
        ÖĞRENCİ NOT LİSTESİ GETİRME
        JOIN kullanarak 3 tablodan verileri birleştirir
        
        Args:
            ogrenci_id: Belirli bir öğrenci ID'si (None ise tüm öğrenciler)
        
        Returns:
            Liste içinde not kayıtları
        """
        try:
            if ogrenci_id:
                # BELİRLİ BİR ÖĞRENCİNİN NOTLARI
                print(f"\n👨‍🎓 Öğrenci ID {ogrenci_id} not listesi getiriliyor...")
                
                # JOIN SORGUSU - 3 tabloyu birleştir
                sorgu = '''
                    SELECT 
                        o.ogrenci_no, o.ad, o.soyad, o.sinif,          -- Öğrenci bilgileri
                        d.ders_kodu, d.ders_adi, d.ogretmen,           -- Ders bilgileri
                        n.vize_notu, n.final_notu, n.ortalama, n.harf_notu, n.donem  -- Not bilgileri
                    FROM notlar n
                    JOIN ogrenciler o ON n.ogrenci_id = o.id           -- Öğrenci tablosu ile birleştir
                    JOIN dersler d ON n.ders_id = d.id                 -- Dersler tablosu ile birleştir
                    WHERE o.id = ?                                     -- Filtre: Belirli öğrenci
                    ORDER BY d.ders_adi                                -- Sırala: Ders adına göre
                '''
                self.imlec.execute(sorgu, (ogrenci_id,))
                
            else:
                # TÜM ÖĞRENCİLERİN NOTLARI
                print("\n👥 Tüm öğrencilerin not listesi getiriliyor...")
                
                sorgu = '''
                    SELECT 
                        o.ogrenci_no, o.ad, o.soyad, o.sinif,
                        d.ders_kodu, d.ders_adi, d.ogretmen,
                        n.vize_notu, n.final_notu, n.ortalama, n.harf_notu, n.donem
                    FROM notlar n
                    JOIN ogrenciler o ON n.ogrenci_id = o.id
                    JOIN dersler d ON n.ders_id = d.id
                    ORDER BY o.ad, d.ders_adi  -- Önce öğrenci adı, sonra ders adı
                '''
                self.imlec.execute(sorgu)
            
            # Sorgu sonuçlarını al
            not_listesi = self.imlec.fetchall()
            print(f"✅ {len(not_listesi)} adet not kaydı bulundu.")
            
            return not_listesi
            
        except sqlite3.Error as hata:
            print(f"❌ Not listesi getirme hatası: {hata}")
            return []  # Hata durumunda boş liste döndür
    
    def ders_bazli_istatistik(self, ders_kodu):
        """
        DERS BAZLI İSTATİSTİKLER
        Belirli bir ders için detaylı istatistikler hesaplar
        
        Args:
            ders_kodu: İstatistiği hesaplanacak ders kodu
        
        Returns:
            İstatistik verileri (öğrenci sayısı, ortalama, min/max notlar vb.)
        """
        try:
            print(f"\n📈 {ders_kodu} dersi için istatistikler hesaplanıyor...")
            
            # KARMAŞIK SQL SORGUSU - Gruplama ve koşullu sayım
            sorgu = '''
                SELECT 
                    COUNT(*) as ogrenci_sayisi,                      -- Toplam öğrenci sayısı
                    AVG(n.ortalama) as ortalama,                    -- Sınıf ortalaması
                    MIN(n.ortalama) as min_not,                     -- En düşük not
                    MAX(n.ortalama) as max_not,                     -- En yüksek not
                    -- Koşullu sayım: Geçen öğrenciler (CC ve üstü)
                    SUM(CASE WHEN n.harf_notu IN ('AA', 'BA', 'BB', 'CB', 'CC') THEN 1 ELSE 0 END) as gecen_sayisi,
                    -- Koşullu sayım: Kalan öğrenciler (DC ve altı)
                    SUM(CASE WHEN n.harf_notu IN ('DC', 'DD', 'FD', 'FF') THEN 1 ELSE 0 END) as kalan_sayisi
                FROM notlar n
                JOIN dersler d ON n.ders_id = d.id
                WHERE d.ders_kodu = ?  -- Filtre: Belirli ders kodu
            '''
            
            self.imlec.execute(sorgu, (ders_kodu,))
            istatistik = self.imlec.fetchone()  # Tek satır sonuç
            
            if istatistik:
                print(f"✅ {ders_kodu} istatistikleri hesaplandı.")
            else:
                print(f"⚠️  {ders_kodu} dersi için veri bulunamadı.")
            
            return istatistik
            
        except sqlite3.Error as hata:
            print(f"❌ İstatistik hesaplama hatası: {hata}")
            return None
    
    def baglanti_kapat(self):
        """
        VERİTABANI BAĞLANTISINI KAPATMA
        Kaynakları serbest bırakmak için bağlantıyı kapatır
        """
        if self.baglanti:
            self.baglanti.close()
            print("\n🔒 Veritabanı bağlantısı güvenli şekilde kapatıldı.")


# === PROGRAMIN ANA ÇALIŞMA KISMI ===
if __name__ == "__main__":
    """
    BU KISIM PROGRAM ÇALIŞTIĞINDA OTOMATİK OLARAK ÇALIŞIR
    Tüm fonksiyonları test eder ve sonuçları gösterir
    """
    
    print("=" * 60)
    print("🎓 ÖĞRENCİ NOT SİSTEMİ - İLİŞKİSEL VERİTABANI ÖRNEĞİ")
    print("=" * 60)
    
    # 1. SİSTEM NESNESİ OLUŞTURMA
    print("\n1️⃣  SİSTEM BAŞLATILIYOR...")
    not_sistemi = OgrenciNotSistemi()
    
    # 2. ÖRNEK VERİLERİ EKLEME
    print("\n2️⃣  ÖRNEK VERİLER EKLENİYOR...")
    not_sistemi.ornek_verileri_ekle()
    
    # 3. NOT ORTALAMALARINI HESAPLAMA
    print("\n3️⃣  NOT ORTALAMALARI HESAPLANIYOR...")
    not_sistemi.not_hesapla_ve_guncelle()
    
    # 4. BELİRLİ BİR ÖĞRENCİNİN NOTLARINI GÖSTERME
    print("\n4️⃣  ÖĞRENCİ NOT LİSTESİ GÖSTERİLİYOR...")
    print("-" * 50)
    print("📚 ALİ YILMAZ'IN NOT LİSTESİ")
    print("-" * 50)
    
    ali_notlari = not_sistemi.ogrenci_not_listesi(1)  # Ali'nin ID'si: 1
    
    for not_kaydi in ali_notlari:
        # not_kaydi içindeki indeksler:
        # 0: ogrenci_no, 1: ad, 2: soyad, 3: sinif
        # 4: ders_kodu, 5: ders_adi, 6: ogretmen
        # 7: vize_notu, 8: final_notu, 9: ortalama, 10: harf_notu, 11: donem
        print(f"📖 {not_kaydi[5]:15} | Vize: {not_kaydi[7]:3} | Final: {not_kaydi[8]:3} | "
              f"Ortalama: {not_kaydi[9]:5.1f} | Harf: {not_kaydi[10]:2}")
    
    # 5. TÜM ÖĞRENCİLERİN NOTLARINI GÖSTERME (KISITLI)
    print("\n5️⃣  TÜM ÖĞRENCİLERİN NOTLARI (İLK 6 KAYIT)")
    print("-" * 70)
    
    tum_notlar = not_sistemi.ogrenci_not_listesi()
    
    # Sadece ilk 6 kaydı göster (çok uzun olmaması için)
    for i, not_kaydi in enumerate(tum_notlar[:6]):
        print(f"{i+1:2}. {not_kaydi[1]} {not_kaydi[2]:10} | {not_kaydi[5]:15} | "
              f"Ort: {not_kaydi[9]:5.1f} | Harf: {not_kaydi[10]:2}")
    
    # 6. DERS BAZLI İSTATİSTİKLER
    print("\n6️⃣  DERS BAZLI İSTATİSTİKLER")
    print("-" * 50)
    print("📊 MATEMATİK DERSİ İSTATİSTİKLERİ")
    print("-" * 50)
    
    mat_istatistik = not_sistemi.ders_bazli_istatistik("MAT101")
    
    if mat_istatistik:
        # istatistik içindeki indeksler:
        # 0: ogrenci_sayisi, 1: ortalama, 2: min_not, 3: max_not
        # 4: gecen_sayisi, 5: kalan_sayisi
        print(f"👥 Öğrenci Sayısı: {mat_istatistik[0]}")
        print(f"📈 Sınıf Ortalaması: {mat_istatistik[1]:.2f}")
        print(f"📉 En Düşük Not: {mat_istatistik[2]:.1f}")
        print(f"📊 En Yüksek Not: {mat_istatistik[3]:.1f}")
        print(f"✅ Geçen Öğrenci: {mat_istatistik[4]}")
        print(f"❌ Kalan Öğrenci: {mat_istatistik[5]}")
        
        # Başarı yüzdesini hesapla
        if mat_istatistik[0] > 0:
            basari_yuzdesi = (mat_istatistik[4] / mat_istatistik[0]) * 100
            print(f"🎯 Başarı Yüzdesi: %{basari_yuzdesi:.1f}")
    
    # 7. BAĞLANTIYI KAPATMA
    print("\n7️⃣  PROGRAM SONLANDIRILIYOR...")
    not_sistemi.baglanti_kapat()
    
    print("\n" + "=" * 60)
    print("🎉 ÖĞRENCİ NOT SİSTEMİ BAŞARIYLA TAMAMLANDI!")
    print("=" * 60)

"""

ÖNEMLİ KAVRAMLARIN ÖZETİ:
1. İlişkisel Veritabanı Nedir?
Tablolar arasında ilişkiler kuran veritabanı türü

Örnek: Öğrenci ↔ Not ↔ Ders ilişkisi

2. FOREIGN KEY (Yabancı Anahtar)
Bir tablodaki sütunun başka bir tablonun PRIMARY KEY'ine referans vermesi

Veri bütünlüğünü sağlar

3. JOIN İşlemleri
Birden fazla tablodan verileri birleştirerek getirme

INNER JOIN: Sadece eşleşen kayıtları getirir

4. SQL Sorgu Türleri
SELECT: Veri okuma

INSERT: Veri ekleme

UPDATE: Veri güncelleme

DELETE: Veri silme

5. Transaction (İşlem) Yönetimi
commit(): Değişiklikleri kalıcı hale getirir

rollback(): Hata durumunda değişiklikleri geri alır

Bu örnek, gerçek hayattaki bir okul not sisteminin basitleştirilmiş halidir ve 
ilişkisel veritabanlarının temel konseptlerini öğretmektedir.

"""