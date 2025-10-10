# Örnek 2: CRUD İşlemleri - Kitap Kütüphanesi
class KutuphaneVeritabani:
    """Kütüphane veritabanı işlemlerini yöneten sınıf"""
    
    def __init__(self, db_adi="kutuphane.db"):
        self.db_adi = db_adi
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        """Veritabanı bağlantısı oluşturur ve tabloyu hazırlar"""
        try:
            self.baglanti = sqlite3.connect(self.db_adi)
            self.imlec = self.baglanti.cursor()
            
            # Kitaplar tablosunu oluştur
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS kitaplar (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbn TEXT UNIQUE NOT NULL,
                    baslik TEXT NOT NULL,
                    yazar TEXT NOT NULL,
                    yayin_yili INTEGER,
                    tur TEXT,
                    sayfa_sayisi INTEGER,
                    stok_adet INTEGER DEFAULT 1,
                    odunc_alindi INTEGER DEFAULT 0,
                    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Üyeler tablosunu oluştur
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS uyeler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uye_no TEXT UNIQUE NOT NULL,
                    ad TEXT NOT NULL,
                    soyad TEXT NOT NULL,
                    telefon TEXT,
                    email TEXT,
                    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Ödünç işlemleri tablosunu oluştur
            self.imlec.execute('''
                CREATE TABLE IF NOT EXISTS odunc_islemleri (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kitap_id INTEGER,
                    uye_id INTEGER,
                    odunc_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    planlanan_iade_tarihi TIMESTAMP,
                    gercek_iade_tarihi TIMESTAMP,
                    durum TEXT DEFAULT 'Ödünçte',
                    FOREIGN KEY (kitap_id) REFERENCES kitaplar (id),
                    FOREIGN KEY (uye_id) REFERENCES uyeler (id)
                )
            ''')
            
            self.baglanti.commit()
            print("✅ Veritabanı tabloları hazırlandı!")
            
        except sqlite3.Error as hata:
            print(f"❌ Veritabanı hatası: {hata}")
    
    # CREATE İşlemleri
    def kitap_ekle(self, isbn, baslik, yazar, yayin_yili, tur, sayfa_sayisi, stok_adet=1):
        """Yeni kitap ekler"""
        try:
            self.imlec.execute('''
                INSERT INTO kitaplar (isbn, baslik, yazar, yayin_yili, tur, sayfa_sayisi, stok_adet)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (isbn, baslik, yazar, yayin_yili, tur, sayfa_sayisi, stok_adet))
            
            self.baglanti.commit()
            print(f"✅ '{baslik}' kitabı eklendi!")
            return True
            
        except sqlite3.IntegrityError:
            print(f"❌ Bu ISBN numarası zaten kayıtlı: {isbn}")
            return False
        except sqlite3.Error as hata:
            print(f"❌ Kitap ekleme hatası: {hata}")
            return False
    
    def uye_ekle(self, uye_no, ad, soyad, telefon=None, email=None):
        """Yeni üye ekler"""
        try:
            self.imlec.execute('''
                INSERT INTO uyeler (uye_no, ad, soyad, telefon, email)
                VALUES (?, ?, ?, ?, ?)
            ''', (uye_no, ad, soyad, telefon, email))
            
            self.baglanti.commit()
            print(f"✅ '{ad} {soyad}' üyesi eklendi!")
            return True
            
        except sqlite3.IntegrityError:
            print(f"❌ Bu üye numarası zaten kayıtlı: {uye_no}")
            return False
        except sqlite3.Error as hata:
            print(f"❌ Üye ekleme hatası: {hata}")
            return False
    
    # READ İşlemleri
    def kitaplari_listele(self, filtre=None):
        """Tüm kitapları listeler"""
        try:
            if filtre:
                # Filtreli arama
                self.imlec.execute('''
                    SELECT * FROM kitaplar 
                    WHERE baslik LIKE ? OR yazar LIKE ? OR tur LIKE ?
                ''', (f'%{filtre}%', f'%{filtre}%', f'%{filtre}%'))
            else:
                # Tüm kitaplar
                self.imlec.execute("SELECT * FROM kitaplar ORDER BY baslik")
            
            kitaplar = self.imlec.fetchall()
            return kitaplar
            
        except sqlite3.Error as hata:
            print(f"❌ Kitap listeleme hatası: {hata}")
            return []
    
    def kitap_detay(self, kitap_id):
        """Belirli bir kitabın detaylarını getirir"""
        try:
            self.imlec.execute("SELECT * FROM kitaplar WHERE id = ?", (kitap_id,))
            kitap = self.imlec.fetchone()
            return kitap
        except sqlite3.Error as hata:
            print(f"❌ Kitap detay hatası: {hata}")
            return None
    
    # UPDATE İşlemleri
    def kitap_guncelle(self, kitap_id, **guncellemeler):
        """Kitap bilgilerini günceller"""
        try:
            set_bolumu = ", ".join([f"{anahtar} = ?" for anahtar in guncellemeler.keys()])
            degerler = list(guncellemeler.values())
            degerler.append(kitap_id)
            
            sorgu = f"UPDATE kitaplar SET {set_bolumu} WHERE id = ?"
            self.imlec.execute(sorgu, degerler)
            
            self.baglanti.commit()
            print(f"✅ Kitap bilgileri güncellendi!")
            return True
            
        except sqlite3.Error as hata:
            print(f"❌ Kitap güncelleme hatası: {hata}")
            return False
    
    # DELETE İşlemleri
    def kitap_sil(self, kitap_id):
        """Kitabı siler"""
        try:
            # Önce kitabın ödünç durumunu kontrol et
            self.imlec.execute("SELECT odunc_alindi FROM kitaplar WHERE id = ?", (kitap_id,))
            kitap = self.imlec.fetchone()
            
            if kitap and kitap[0] == 1:
                print("❌ Ödünç alınmış kitap silinemez!")
                return False
            
            self.imlec.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))
            self.baglanti.commit()
            print("✅ Kitap silindi!")
            return True
            
        except sqlite3.Error as hata:
            print(f"❌ Kitap silme hatası: {hata}")
            return False
    
    def baglanti_kapat(self):
        """Veritabanı bağlantısını kapatır"""
        if self.baglanti:
            self.baglanti.close()
            print("✅ Veritabanı bağlantısı kapatıldı.")

# CRUD işlemleri kullanımı
print("\n=== CRUD İŞLEMLERİ: KÜTÜPHANE SİSTEMİ ===")

# Veritabanı nesnesi oluştur
kutuphane_db = KutuphaneVeritabani()

# CREATE - Kitap ekleme
kutuphane_db.kitap_ekle("978-975-08-4521-1", "Suç ve Ceza", "Fyodor Dostoyevski", 1866, "Roman", 671, 3)
kutuphane_db.kitap_ekle("978-975-08-1234-5", "Savaş ve Barış", "Lev Tolstoy", 1869, "Roman", 1225, 2)
kutuphane_db.kitap_ekle("978-975-08-7890-1", "Matematik Tarihi", "Ali Matematikçi", 2020, "Bilim", 350, 1)

# CREATE - Üye ekleme
kutuphane_db.uye_ekle("U001", "Ali", "Yılmaz", "555-123-4567", "ali@email.com")
kutuphane_db.uye_ekle("U002", "Ayşe", "Kaya", "555-987-6543", "ayse@email.com")

# READ - Kitapları listeleme
print("\n--- TÜM KİTAPLAR ---")
kitaplar = kutuphane_db.kitaplari_listele()
for kitap in kitaplar:
    print(f"ID: {kitap[0]}, ISBN: {kitap[1]}, Başlık: {kitap[2]}, Yazar: {kitap[3]}, Stok: {kitap[7]}")

# READ - Filtreli arama
print("\n--- 'SAVAŞ' KELİMESİ İÇİN ARAMA ---")
filtreli_kitaplar = kutuphane_db.kitaplari_listele("savaş")
for kitap in filtreli_kitaplar:
    print(f"Başlık: {kitap[2]}, Yazar: {kitap[3]}")

# UPDATE - Kitap güncelleme
print("\n--- KİTAP GÜNCELLEME ---")
kutuphane_db.kitap_guncelle(1, stok_adet=5, tur="Klasik Roman")

# Güncel kitap listesi
print("\n--- GÜNCEL KİTAP LİSTESİ ---")
guncel_kitaplar = kutuphane_db.kitaplari_listele()
for kitap in guncel_kitaplar:
    print(f"ID: {kitap[0]}, Başlık: {kitap[2]}, Tür: {kitap[5]}, Stok: {kitap[7]}")

# Bağlantıyı kapat
kutuphane_db.baglanti_kapat()