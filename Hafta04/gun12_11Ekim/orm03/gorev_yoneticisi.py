"""
SQLAlchemy ORM Destekli Kişisel Görev Yöneticisi (To-Do List)
Bu uygulama, kullanıcıların görev eklemesine, listelemesine, 
tamamlandı olarak işaretlemesine ve silmesine olanak tanır. 
Tüm görev verileri SQLAlchemy ORM aracılığıyla kalıcı olarak saklanır.

Proje Bilgisi
Özellik	Açıklama
Amaç	Komut satırı üzerinden çalışan bir Görev Yöneticisi oluşturmak.
Teknoloji	SQLAlchemy ORM ile kalıcı veri yönetimi.
Kullanılan Konular	OOP, ORM, while True döngüsü, if-elif-else, Hata Yönetimi (try-except).
Veritabanı	SQLite dosyası (gorev_yonetici.db).
"""

# 1. SQLAlchemy ve MODEL Tanımlamaları

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
import sys

# ----------------------------------------
# Veritabanı ve Model Tanımları
# ----------------------------------------

# Veritabanı Bağlantısı (Engine): Veritabanı dosyamızı tanımlarız.
engine = create_engine('sqlite:///gorev_yonetici.db')

# Temel Sınıf (Base): Tüm model sınıflarımızın türeyeceği temel yapı.
Base = declarative_base()

# MODEL SINIFI: Gorev (Veritabanındaki 'gorevler' tablosu)
class Gorev(Base):
    __tablename__ = 'gorevler'

    # Sütun Tanımları: Veritabanı şemasını (alanları) belirleriz.
    id = Column(Integer, primary_key=True)         # INTEGER PRIMARY KEY: Her görevin benzersiz kimliği.
    tanim = Column(String, nullable=False)         # TEXT NOT NULL: Görevin açıklaması, boş geçilemez.
    oncelik = Column(String, default='Orta')       # TEXT: 'Yuksek', 'Orta', 'Dusuk' olabilir, varsayılan 'Orta'.
    tamamlandi = Column(Boolean, default=False)    # BOOLEAN: Görevin yapılıp yapılmadığı, varsayılan False.

    # __repr__ metodu: Nesneyi print() ile yazdırdığımızda okunur bir çıktı sağlar.
    def __repr__(self):
        durum = "[TAMAMLANDI]" if self.tamamlandi else "[BEKLEMEDE]"
        return f"{durum:<12} | ID: {self.id:<4} | Öncelik: {self.oncelik:<7} | Görev: {self.tanim}"

# Tüm tabloları veritabanına yansıt: Tablolar henüz yoksa oluşturulur.
Base.metadata.create_all(engine)

# Oturum Fabrikası: Veritabanı ile iletişim kurmak için Oturum (Session) üretir.
Session = sessionmaker(bind=engine)

# 2. Görev Yöneticisi Sınıfı (İş Mantığı)

class GorevYoneticisi:
    """Uygulamanın tüm iş mantığını ve CRUD işlemlerini yöneten sınıf."""
    
    def __init__(self):
        # Sınıfın her kullanımında bir Oturum nesnesi başlatmaya hazırız.
        pass 

    def _get_session(self):
        """Her işlem için yeni bir oturum oluşturur ve döndürür."""
        return Session()

    # --- 1. GÖREV EKLEME (CREATE) ---
    def gorev_ekle(self):
        print("\n--- Yeni Görev Ekle ---")
        tanim = input("Görevi Tanımlayın: ").strip()
        
        if not tanim:
            print("HATA: Görev tanımı boş bırakılamaz.")
            return

        # Kullanıcıdan öncelik bilgisini al, yanlış girerse varsayılanı kullan
        oncelik = input("Öncelik (Yüksek/Orta/Düşük - Varsayılan Orta): ").strip().capitalize()
        if oncelik not in ['Yuksek', 'Orta', 'Dusuk']:
            oncelik = 'Orta'
            print(f"Geçersiz öncelik, 'Orta' olarak ayarlandı.")
            
        yeni_gorev = Gorev(tanim=tanim, oncelik=oncelik)
        
        session = self._get_session()
        try:
            session.add(yeni_gorev)
            session.commit()
            print(f"BAŞARILI: '{tanim}' (Öncelik: {oncelik}) eklendi.")
        except Exception as e:
            session.rollback() # Hata durumunda veritabanını önceki haline döndür
            print(f"HATA: Görev eklenirken beklenmedik bir hata oluştu: {e}")
        finally:
            session.close() # İşlem bitince oturumu kapat (önemli!)

    # --- 2. GÖREVLERİ LİSTELEME (READ) ---
    def gorevleri_listele(self, sadece_bekleyen=False):
        session = self._get_session()
        
        # Sorgu: Tüm görevleri al
        sorgu = session.query(Gorev)
        
        # Filtreleme (Koşullu Okuma): Eğer sadece_bekleyen True ise filtre ekle
        if sadece_bekleyen:
            sorgu = sorgu.filter(Gorev.tamamlandi == False)
            print("\n--- BEKLEYEN GÖREVLER ---")
        else:
            print("\n--- TÜM GÖREVLER ---")
        
        # Sıralama: Önceliğe göre ve sonra ID'ye göre sırala
        gorevler = sorgu.order_by(Gorev.oncelik, Gorev.id).all()
        
        if not gorevler:
            print("Kayıtlı görev bulunmamaktadır.")
        else:
            print(f"{'DURUM':<12} | {'ID':<4} | {'ÖNCELİK':<7} | {'GÖREV TANIMI'}")
            print("-" * 65)
            for gorev in gorevler:
                print(gorev)
        
        session.close()
        return gorevler # Güncelleme/Silme gibi işlemler için listeyi döndür

    # --- 3. GÖREVİ TAMAMLA/GÜNCELLE (UPDATE) ---
    def gorev_tamamla(self):
        # Önce sadece bekleyen görevleri göster ki kullanıcı ID seçebilsin
        bekleyen_gorevler = self.gorevleri_listele(sadece_bekleyen=True)
        if not bekleyen_gorevler:
            return

        try:
            gorev_id = int(input("\nTamamlandı olarak işaretlenecek görevin ID'si: "))
        except ValueError:
            print("HATA: Geçerli bir sayı girmelisiniz.")
            return

        session = self._get_session()
        # Belirli ID'ye sahip görevi bul
        gorev = session.query(Gorev).filter(Gorev.id == gorev_id).first()

        if gorev:
            # OOP Prensibi: Python nesnesinin özelliğini değiştir
            if not gorev.tamamlandi:
                gorev.tamamlandi = True
                session.commit() # Değişikliği veritabanına kaydet
                print(f"BAŞARILI: Görev ID {gorev_id} ('{gorev.tanim}') tamamlandı olarak işaretlendi.")
            else:
                 print(f"Uyarı: Görev ID {gorev_id} zaten tamamlanmış.")
        else:
            print(f"HATA: ID {gorev_id} ile kayıtlı görev bulunamadı.")
            
        session.close()

    # --- 4. GÖREVİ SİLME (DELETE) ---
    def gorev_sil(self):
        # Kullanıcının hangi görevi sileceğini bilmesi için tüm görevleri listele
        self.gorevleri_listele()
        
        try:
            gorev_id = int(input("\nSilmek istediğiniz görevin ID'si: "))
        except ValueError:
            print("HATA: Geçerli bir sayı girmelisiniz.")
            return

        session = self._get_session()
        gorev = session.query(Gorev).filter(Gorev.id == gorev_id).first()

        if gorev:
            onay = input(f"'{gorev.tanim}' görevini silmek istediğinizden emin misiniz? (E/H): ").upper()
            if onay == 'E':
                session.delete(gorev) # Oturumdan silme komutu
                session.commit()       # Veritabanında kalıcı silme
                print(f"BAŞARILI: Görev ID {gorev_id} silindi.")
            else:
                print("Silme işlemi iptal edildi.")
        else:
            print(f"HATA: ID {gorev_id} ile kayıtlı görev bulunamadı.")
            
        session.close()

# ----------------------------------------------------
# 3. ANA PROGRAM DÖNGÜSÜ
# ----------------------------------------------------

def ana_menu():
    """Kullanıcıya gösterilen ana menüyü yazdırır."""
    print("\n" + "═"*50)
    print("      KİŞİSEL GÖREV YÖNETİCİSİ (SQLALCHEMY)")
    print("═"*50)
    print("1. Yeni Görev Ekle")
    print("2. Tüm Görevleri Listele")
    print("3. Bekleyen Görevleri Listele")
    print("4. Görevi Tamamlandı Olarak İşaretle")
    print("5. Görev Sil")
    print("6. Çıkış")
    print("—" * 50)

def main():
    """Ana program akışını yöneten fonksiyon."""
    yonetici = GorevYoneticisi()
    
    # while True döngüsü programı sürekli çalışır durumda tutar.
    while True:
        ana_menu()
        secim = input("Seçiminizi yapın (1-6): ").strip()
        
        if secim == '1':
            yonetici.gorev_ekle()
        elif secim == '2':
            yonetici.gorevleri_listele()
        elif secim == '3':
            yonetici.gorevleri_listele(sadece_bekleyen=True)
        elif secim == '4':
            yonetici.gorev_tamamla()
        elif secim == '5':
            yonetici.gorev_sil()
        elif secim == '6':
            print("Program kapatılıyor. İyi çalışmalar!")
            sys.exit(0) # Programı güvenli bir şekilde sonlandırır.
        else:
            print("HATA: Geçersiz seçim. Lütfen 1 ile 6 arasında bir sayı girin.")

if __name__ == "__main__":
    main()

"""
Programın Özeti ve Öğrenilenler
Bu örnek, önceki kütüphane örneğinin temelini alarak, yeni özellikler ve daha karmaşık bir iş mantığı eklemiştir:

Yeni Veri Tipleri: Modelimize Boolean (tamamlandı durumu) ve 
String için varsayılan değerler (default='Orta') ekleyerek veri yapımızı zenginleştirdik.

Modüler Yapı (3. Hafta): Tüm veritabanı işlemlerini GorevYoneticisi sınıfında toplayarak, 
ana programı (main fonksiyonu) temiz tuttuk.

Dinamik Filtreleme: gorevleri_listele metoduna bir parametre (sadece_bekleyen=False) ekleyerek, 
tek bir metot ile hem tüm görevleri hem de sadece bekleyen görevleri listeleyebilmeyi sağladık. Bu, kod tekrarını önler.

OOP Güncelleme: gorev_tamamla işleminde, SQL komutu yazmak yerine, 
veritabanından aldığımız Gorev nesnesinin sadece tamamlandi özelliğini değiştirdik ve 
session.commit() diyerek değişikliği otomatik olarak kaydettik.

SQLAlchemy'nin Gücü: order_by(Gorev.oncelik, Gorev.id) kullanarak görevleri önce önceliğe, 
sonra ID'ye göre sıralama işlemini yine Python koduyla kolayca gerçekleştirdik.

"""