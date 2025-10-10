import sqlite3


import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"


class Kitap:
    """
    Veritabanındaki bir kitap kaydını (satırını) temsil eder.
    Bu, bir ORM'deki 'Model' kavramına benzer.
    """
    def __init__(self, ad, yazar, id=None):
        # id=None varsayılan değeri, kitap henüz veritabanına kaydedilmediğinde
        # ID'sinin olmadığını belirtir. Veritabanı bunu otomatik olarak verecektir.
        self.id = id
        self.ad = ad
        self.yazar = yazar
    
    # __str__ ve __repr__ metotları (4. Hafta 2. Oturum konusu) 
    # nesneyi yazdırırken anlaşılır çıktı vermemizi sağlar.
    def __str__(self): #kullanıcı için
        return f"Kitap ID: {self.id if self.id else 'Yeni'}, Ad: {self.ad}, Yazar: {self.yazar}"

    def __repr__(self): #geliştirici için
        return f"Kitap(id={self.id}, ad='{self.ad}', yazar='{self.yazar}')"

class KutuphaneYonetici:
    def __init__(self, db_adi=veritabanim):
        self.db_adi = db_adi
        self._tablo_olustur()

    def _baglanti_kur(self):
        """Veritabanı bağlantısını döndürür."""
        return sqlite3.connect(self.db_adi)

    def _tablo_olustur(self):
        """Kitaplar tablosu yoksa oluşturur."""
        baglanti = self._baglanti_kur()
        imlec = baglanti.cursor()
        imlec.execute("""
            CREATE TABLE IF NOT EXISTS kitaplar (
                id INTEGER PRIMARY KEY,
                ad TEXT NOT NULL,
                yazar TEXT NOT NULL
            )
        """)
        baglanti.commit()
        baglanti.close()
        
    # --- CRUD İŞLEMLERİ ---

    # C (Create) - Ekleme İşlemi
    def kitap_ekle(self, kitap_nesnesi: Kitap):
        """Bir Kitap nesnesini veritabanına kaydeder."""
        if kitap_nesnesi.id is not None:
            print("Uyarı: Kitap zaten kaydedilmiş gibi görünüyor, güncelleme kullanın.")
            return

        baglanti = self._baglanti_kur()
        imlec = baglanti.cursor()
        
        imlec.execute(
            "INSERT INTO kitaplar (ad, yazar) VALUES (?, ?)", 
            (kitap_nesnesi.ad, kitap_nesnesi.yazar)
        )
        
        # Yeni eklenen kaydın ID'sini alıp nesneye atıyoruz
        kitap_nesnesi.id = imlec.lastrowid
        
        baglanti.commit()
        baglanti.close()
        print(f"'{kitap_nesnesi.ad}' başarıyla veritabanına eklendi. (ID: {kitap_nesnesi.id})")
        return kitap_nesnesi

    # R (Read) - Tümünü Okuma İşlemi
    def tum_kitaplari_getir(self):
        """Veritabanındaki tüm kitapları Kitap nesneleri listesi olarak döndürür."""
        baglanti = self._baglanti_kur()
        imlec = baglanti.cursor()
        imlec.execute("SELECT id, ad, yazar FROM kitaplar")
        
        kitap_listesi = []
        for id, ad, yazar in imlec.fetchall():
            # Her bir veritabanı kaydını bir Kitap nesnesine dönüştürüyoruz
            kitap_listesi.append(Kitap(ad=ad, yazar=yazar, id=id))

        baglanti.close()
        return kitap_listesi

    # U (Update) - Güncelleme İşlemi
    def kitap_guncelle(self, kitap_nesnesi: Kitap):
        """Mevcut bir Kitap nesnesinin verilerini günceller."""
        if kitap_nesnesi.id is None:
            print("Hata: Güncelleme için Kitap nesnesinin bir ID'si olmalıdır.")
            return False

        baglanti = self._baglanti_kur()
        imlec = baglanti.cursor()
        
        imlec.execute(
            "UPDATE kitaplar SET ad = ?, yazar = ? WHERE id = ?",
            (kitap_nesnesi.ad, kitap_nesnesi.yazar, kitap_nesnesi.id)
        )
        
        baglanti.commit()
        baglanti.close()
        print(f"Kitap ID {kitap_nesnesi.id} güncellendi.")
        return True

    # D (Delete) - Silme İşlemi
    def kitap_sil(self, kitap_id: int):
        """Belirtilen ID'ye sahip kitabı siler."""
        baglanti = self._baglanti_kur()
        imlec = baglanti.cursor()
        
        imlec.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))
        
        baglanti.commit()
        silinen_sayisi = imlec.rowcount # Kaç satır silindiğini kontrol et
        baglanti.close()

        if silinen_sayisi > 0:
            print(f"Kitap ID {kitap_id} başarıyla silindi.")
            return True
        else:
            print(f"Hata: Kitap ID {kitap_id} bulunamadı.")
            return False
        

# 1. Kütüphane Yönetici nesnesini (Repository) oluştur.
# yonetici = KutuphaneYonetici()

# 2. C (Create) - Kitap Nesnesi Oluştur ve Kaydet
# print("\n--- EKLEME (CREATE) ---")
# yeni_kitap_1 = Kitap(ad="Python ile Yazılım Geliştirme", yazar="Sinan Hoca")
# yeni_kitap_2 = Kitap(ad="C Sharp", yazar="Mustafa Hoca")

# Ekleme metodu, Kitap nesnesini alıp ID'sini atıyor.
# yonetici.kitap_ekle(yeni_kitap_1)
# yonetici.kitap_ekle(yeni_kitap_2)

# Yeni Kitap-1'in ID'sini daha sonra güncellemek için saklayalım
# kitap_id_guncellenecek = yeni_kitap_1.id 
# print(yeni_kitap_1) # Nesneye ID otomatik olarak atanmıştır.

# 3. R (Read) - Tümünü Listele
# print("\n--- LİSTELEME (READ) ---")
# tum_kitaplar = yonetici.tum_kitaplari_getir()
# for kitap in tum_kitaplar:
#     print(kitap)

# 4. U (Update) - Mevcut Nesneyi Güncelle
# print("\n--- GÜNCELLEME (UPDATE) ---")
# Yeni Kitap-1'in ismini Python'un kurallarına göre değiştirelim
# yeni_kitap_1.ad = "80 Saatlik Python Eğitimi" 
# ID'si zaten nesnenin içinde kayıtlı (OOP!)

yonetici.kitap_guncelle(yeni_kitap_1)

# # Tekrar Listele (Güncellemeyi görmek için)
# print("\n--- GÜNCELLEME SONRASI LİSTELEME ---")
# for kitap in yonetici.tum_kitaplari_getir():
#     print(kitap)

# # 5. D (Delete) - Silme
# print("\n--- SİLME (DELETE) ---")
# # İkinci kitabı ID'si üzerinden silelim
# yonetici.kitap_sil(kitap_id_guncellenecek)

# # Son Listeleme
# print("\n--- SİLME SONRASI LİSTELEME ---")
# for kitap in yonetici.tum_kitaplari_getir():
#     print(kitap)