"""
Programın Özeti ve Öğrenilenler
Bu program, önceki ders konularını başarılı bir şekilde birleştirmiştir:

OOP (Nesne Yönelimli Programlama): Kitap ve Kutuphane sınıflarını kullandık. 
Tüm veritabanı mantığı Kutuphane sınıfının metotlarında gizlidir.

SQLAlchemy ORM: SQL komutları yazmadan, tamamen Python nesneleri üzerinden (Model Kitap ve Oturum session) CRUD işlemlerini yönettik.

Hata Yönetimi: try-except blokları (3. Hafta 1. Oturum konusu) kullanarak kullanıcıdan sayı beklediğimiz yerlerde oluşabilecek hataları yakaladık.

Temel Programlama: while True döngüsü ve if-elif-else yapısı (1. Hafta konuları) programın ana akışını yönetti.
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
import sys

# ----------------------------------------------------
# 1. SQLAlchemy ve MODEL (Veri Yapısı) Tanımlamaları
# ----------------------------------------------------

# Veritabanı Bağlantısı (Engine)
# 'kutuphane_cli.db' dosyasını oluşturur veya bağlanır
engine = create_engine('sqlite:///kutuphane_cli.db')

# Temel Sınıf (Base)
Base = declarative_base()

# MODEL SINIFI: Kitap (Veritabanındaki 'kitaplar' tablosu)
class Kitap(Base):
    __tablename__ = 'kitaplar'

    id = Column(Integer, primary_key=True)
    ad = Column(String)
    yazar = Column(String)

    def __repr__(self):
        return f"ID: {self.id:<4} | Ad: {self.ad:<30} | Yazar: {self.yazar}"

# Tüm tabloları veritabanına yansıt (Tablo yoksa oluşturulur)
Base.metadata.create_all(engine)

# Oturum Fabrikası
Session = sessionmaker(bind=engine)


# ----------------------------------------------------
# 2. KÜTÜPHANE YÖNETİCİ SINIFI (İş Mantığı)
# ----------------------------------------------------

class Kutuphane:
    """Tüm CRUD işlemlerini yöneten sınıf."""
    def __init__(self):
        # Her işlem için yeni bir oturum başlatmak iyi bir pratiktir.
        self.session = Session()

    def kitap_ekle(self):
        print("\n--- Yeni Kitap Ekle ---")
        ad = input("Kitap Adı: ").strip()
        yazar = input("Yazar Adı: ").strip()

        if not ad or not yazar:
            print("HATA: Kitap adı ve yazar adı boş bırakılamaz.")
            return

        yeni_kitap = Kitap(ad=ad, yazar=yazar)
        
        try:
            self.session.add(yeni_kitap)
            self.session.commit()
            print(f"BAŞARILI: '{yeni_kitap.ad}' (ID: {yeni_kitap.id}) eklendi.")
        except IntegrityError:
            self.session.rollback()
            print("HATA: Ekleme sırasında bir sorun oluştu.")
        finally:
            self.session.close() # İşlem bitince oturumu kapat

    def kitaplari_listele(self):
        print("\n--- Mevcut Kitaplar ---")
        self.session = Session() # Yeni oturum aç
        
        kitaplar = self.session.query(Kitap).order_by(Kitap.id).all()
        
        if not kitaplar:
            print("Kütüphanede kayıtlı kitap bulunmamaktadır.")
        else:
            print(f"{'ID':<4} | {'AD':<30} | {'YAZAR'}")
            print("-" * 50)
            for kitap in kitaplar:
                print(kitap)
        
        self.session.close()

    def kitap_guncelle(self):
        self.kitaplari_listele()
        if not self.session.query(Kitap).first():
            return

        try:
            kitap_id = int(input("\nGüncellemek istediğiniz kitabın ID'si: "))
        except ValueError:
            print("HATA: Geçerli bir sayı girmelisiniz.")
            return

        self.session = Session()
        kitap = self.session.query(Kitap).filter(Kitap.id == kitap_id).first()

        if kitap:
            print(f"Mevcut Kitap: {kitap}")
            yeni_ad = input(f"Yeni Kitap Adı ({kitap.ad}): ").strip()
            yeni_yazar = input(f"Yeni Yazar Adı ({kitap.yazar}): ").strip()

            if yeni_ad:
                kitap.ad = yeni_ad
            if yeni_yazar:
                kitap.yazar = yeni_yazar
            
            self.session.commit()
            print(f"BAŞARILI: Kitap ID {kitap_id} güncellendi.")
        else:
            print(f"HATA: ID {kitap_id} ile kayıtlı kitap bulunamadı.")
            
        self.session.close()

    def kitap_sil(self):
        self.kitaplari_listele()
        if not self.session.query(Kitap).first():
            return
            
        try:
            kitap_id = int(input("\nSilmek istediğiniz kitabın ID'si: "))
        except ValueError:
            print("HATA: Geçerli bir sayı girmelisiniz.")
            return

        self.session = Session()
        kitap = self.session.query(Kitap).filter(Kitap.id == kitap_id).first()

        if kitap:
            onay = input(f"'{kitap.ad}' kitabını silmek istediğinizden emin misiniz? (E/H): ").upper()
            if onay == 'E':
                self.session.delete(kitap)
                self.session.commit()
                print(f"BAŞARILI: Kitap ID {kitap_id} silindi.")
            else:
                print("Silme işlemi iptal edildi.")
        else:
            print(f"HATA: ID {kitap_id} ile kayıtlı kitap bulunamadı.")
            
        self.session.close()


# ----------------------------------------------------
# 3. ANA PROGRAM DÖNGÜSÜ
# ----------------------------------------------------

def ana_menu():
    print("\n" + "="*40)
    print("      KÜTÜPHANE YÖNETİM SİSTEMİ")
    print("="*40)
    print("1. Kitap Ekle")
    print("2. Kitapları Listele")
    print("3. Kitap Güncelle")
    print("4. Kitap Sil")
    print("5. Çıkış")
    print("-" * 40)

def main():
    kutuphane = Kutuphane()
    
    # Ana döngü (while döngüsü, 1. Hafta 3. Oturum konusu)
    while True:
        ana_menu()
        secim = input("Seçiminizi yapın (1-5): ").strip()
        
        if secim == '1':
            kutuphane.kitap_ekle()
        elif secim == '2':
            kutuphane.kitaplari_listele()
        elif secim == '3':
            kutuphane.kitap_guncelle()
        elif secim == '4':
            kutuphane.kitap_sil()
        elif secim == '5':
            print("Programdan çıkılıyor. Hoşça kalın!")
            sys.exit(0)
        else:
            print("HATA: Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()