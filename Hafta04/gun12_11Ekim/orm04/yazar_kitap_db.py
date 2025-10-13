"""
İlişkisel veritabanları tek bir tablodan ibaret değildir. 
Bilgileri düzenlemek için birden fazla tablo kullanırız ve bu tablolar arasında mantıksal bağlantılar kurarız. 
Buna ilişki (Relationship) denir.

Kütüphane örneğimize geri dönelim. Daha önce yazar adını her kitap kaydında tekrar ediyorduk. 
Bu, veritabanı tasarımında iyi bir uygulama değildir (verimli değil, veri tutarsızlığı riski var).

Şimdi, bu yapıyı İlişkisel ORM ile düzeltelim:

Yazar adında yeni bir tablo oluşturacağız.

Kitap tablosunu, Yazar tablosuna bağlayacağız (One-to-Many / Bire Çok İlişki).

SQLAlchemy ORM ile İlişkisel Veritabanı Yönetimi (One-to-Many)
Bu proje, bir yazarın birden fazla kitabı olabileceği, 
ancak bir kitabın sadece bir yazarı olabileceği (Bire Çok) ilişkisini modelleyecektir.

Proje Bilgisi
Özellik	        Açıklama
Amaç	        Yazar ve Kitap tabloları arasında Bire Çok ilişki kurmak.
Yeni Konular    Relationship, ForeignKey (Yabancı Anahtar) kullanımı.
Faydası	        Veri tekrarını önlemek ve yazar-kitap bağlantısını doğrudan Python nesneleri üzerinden yapmak.

"""

# 1. SQLAlchemy ve İlişkisel Model Tanımlamaları
# Bu örnekte, Relationship özelliğini kullanmak için relationship ve ForeignKey özelliklerini içeri aktarmamız gerekiyor.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship # Yeni import: relationship
from sqlalchemy.exc import IntegrityError
import sys

# ----------------------------------------
# Veritabanı ve Model Tanımları
# ----------------------------------------
engine = create_engine('sqlite:///kutuphane_iliskisel.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# MODEL 1: Yazar (Ebeveyn Tablo / One - Bir)
class Yazar(Base):
    __tablename__ = 'yazarlar'

    id = Column(Integer, primary_key=True)
    isim = Column(String, unique=True, nullable=False) # Yazar ismi benzersiz olsun

    # İlişki Tanımı (Relationship):
    # Bu özellik, SQLAlchemy'nin sihri! Yazar nesnesine erişince, 
    # bu yazarın tüm kitaplarını otomatik olarak getirir.
    kitaplar = relationship("Kitap", back_populates="yazar") 
    # "Kitap" modelini işaret eder, "Kitap" modelindeki "yazar" özelliği ile eşleşir.

    def __repr__(self):
        return f"Yazar(ID: {self.id}, İsim: {self.isim})"

# MODEL 2: Kitap (Çocuk Tablo / Many - Çok)
class Kitap(Base):
    __tablename__ = 'kitaplar'

    id = Column(Integer, primary_key=True)
    ad = Column(String, nullable=False)
    
    # YABANCI ANAHTAR (ForeignKey): İlişkinin kurulduğu nokta.
    # Kitap tablosunda, yazarın ID'sini tutan bir sütun oluşturulur ve
    # bu, yazarlar tablosundaki id sütununa bağlanır.
    yazar_id = Column(Integer, ForeignKey('yazarlar.id'), nullable=False)

    # İlişki Tanımı (Relationship):
    # Kitap nesnesine erişince, bu kitabın Yazar nesnesine erişim sağlar.
    yazar = relationship("Yazar", back_populates="kitaplar")

    def __repr__(self):
        # Artık yazar adına Kitap nesnesinden doğrudan erişebiliriz: self.yazar.isim
        yazar_ismi = self.yazar.isim if self.yazar else "Bilinmiyor"
        return f"Kitap(ID: {self.id}, Ad: {self.ad}, Yazar: {yazar_ismi})"

# Tabloları oluştur (yazarlar ve kitaplar)
Base.metadata.create_all(engine)

# 2. İlişkisel İşlemler ve Kullanım Senaryoları
# Şimdi bir oturum açıp, ilişkisel yapının gücünü görelim.

# Oturum Başlatma
session = Session()

# ----------------------------------------------------
# 1. YAZAR VE KİTAP EKLEME (CREATE)
# ----------------------------------------------------
print("\n--- 1. İlişkisel Ekleme (Yazar ve Kitap) ---")

# Yazar Nesnesi Oluşturma
yazar_dostoyevski = Yazar(isim="Fyodor Dostoyevski")
yazar_orwell = Yazar(isim="George Orwell")

# Yazar nesnelerini oturuma ekle ve kaydet (ID'leri oluşsun)
session.add_all([yazar_dostoyevski, yazar_orwell])
session.commit()
print("Yazarlar eklendi.")

# Kitap Nesneleri Oluşturma ve Yazar Atama (OOP ile)
# Yazar ID'sini manuel girmek yerine, Yazar nesnesini doğrudan Kitap nesnesine atıyoruz!
kitap_1 = Kitap(ad="Suç ve Ceza", yazar=yazar_dostoyevski)
kitap_2 = Kitap(ad="Budala", yazar=yazar_dostoyevski)
kitap_3 = Kitap(ad="1984", yazar=yazar_orwell)
kitap_4 = Kitap(ad="Hayvan Çiftliği", yazar=yazar_orwell)

# Kitapları kaydet
session.add_all([kitap_1, kitap_2, kitap_3, kitap_4])
session.commit()
print("Kitaplar ilişkilendirilerek eklendi.")


# ----------------------------------------------------
# 2. TERS YÖNLÜ ERİŞİM (Relationship Gücü)
# ----------------------------------------------------
print("\n--- 2. Ters Yönlü Erişim (Yazardan Kitaplara) ---")

# Dostoyevski nesnesini veritabanından yeniden al
dostoyevski = session.query(Yazar).filter(Yazar.isim == "Fyodor Dostoyevski").one()

print(f"Seçilen Yazar: {dostoyevski.isim}")

# **Sihir burada!** SQL sorgusu yazmadan yazarın kitaplarına erişiyoruz.
print("Kitapları:")
for kitap in dostoyevski.kitaplar:
    print(f"- {kitap.ad}")


# ----------------------------------------------------
# 3. İLİŞKİSEL FİLTRELEME (JOIN Kullanımı)
# ----------------------------------------------------
print("\n--- 3. İlişkisel Sorgulama (Yazar Adına Göre Kitap) ---")

# SQL: SELECT Kitap.ad FROM Kitap JOIN Yazar ON Kitap.yazar_id = Yazar.id WHERE Yazar.isim = 'George Orwell'
orwell_kitaplari = session.query(Kitap).join(Kitap.yazar).filter(Yazar.isim == "George Orwell").all()

print("George Orwell'ın Kitapları:")
for kitap in orwell_kitaplari:
    # Hem Kitap'ın bilgilerini hem de ilişkiyi kullanarak Yazar'ın bilgilerini yazdırabiliriz.
    print(f"- {kitap.ad} (Yazar ID: {kitap.yazar_id})")


# ----------------------------------------------------
# 4. İLİŞKİSEL GÜNCELLEME (Yazar Değiştirme)
# ----------------------------------------------------
print("\n--- 4. İlişkisel Güncelleme (Yazar Değiştirme) ---")

# Yeni Yazar Oluştur
yazar_tolstoy = Yazar(isim="Lev Tolstoy")
session.add(yazar_tolstoy)

# Suç ve Ceza kitabını bul
suc_ve_ceza = session.query(Kitap).filter(Kitap.ad == "Suç ve Ceza").one()

# Kitabın yazarını değiştir (Yine sadece Python nesnesini atayarak!)
suc_ve_ceza.yazar = yazar_tolstoy
session.commit()

print(f"'{suc_ve_ceza.ad}' kitabının yeni yazarı: {suc_ve_ceza.yazar.isim}")


# ----------------------------------------------------
# 5. İLİŞKİSEL SİLME (Yazar Silme ve Kaskat Davranış)
# ----------------------------------------------------
print("\n--- 5. İlişkisel Silme ---")

# George Orwell'ı silmeye çalışalım
orwell = session.query(Yazar).filter(Yazar.isim == "George Orwell").one()

# **NOT:** Varsayılan olarak, bir yazarın kitapları varken onu silmek hataya neden olur (Veritabanı Kısıtlaması). 
# Bu davranışı yönetmek için Relationship'e 'cascade' özellikleri eklemek gerekir. 
# Basitçe, önce kitapları silmeliyiz.

print(f"Silinmeden Önce Orwell'ın kitapları: {len(orwell.kitaplar)}")
for kitap in orwell.kitaplar:
    session.delete(kitap) # Önce kitapları siliyoruz

session.delete(orwell) # Şimdi yazarı silebiliriz.
session.commit()

# Kontrol
kalan_kitaplar = session.query(Kitap).all()
kalan_yazarlar = session.query(Yazar).all()

print(f"\nKalan Yazar Sayısı: {len(kalan_yazarlar)}")
print(f"Kalan Kitap Sayısı: {len(kalan_kitaplar)}")

session.close()

"""

Programın Özeti ve Öğrenilenler
Bu son örnekle, Python ile ilişkisel veritabanı yönetiminin en kritik adımlarını atmış olduk:

Tablo Ayrımı (Veri Normalizasyonu): Yazar adını her kitapta tekrarlamak yerine, Yazar tablosu oluşturuldu. 
Kitap tablosu artık sadece yazar_id'yi tutuyor (ForeignKey).

ForeignKey (Yabancı Anahtar): İki tablo arasındaki fiziksel bağlantıyı kuran 
SQL komutunu (yazar_id = Column(Integer, ForeignKey('yazarlar.id'))) tanımladık.

Relationship (İlişki): SQLAlchemy'nin en güçlü özelliği. Bu, veritabanı seviyesindeki karmaşık bağlantıyı alıp, 
Python seviyesinde basit bir nesne erişimine (yazar_dostoyevski.kitaplar veya kitap_1.yazar.isim) dönüştürdü.

İlişkisel Sorgulama: .join(Kitap.yazar) kullanarak iki tabloyu tek bir sorguda birleştirmeyi ve 
bu birleşik veri üzerinde filtreleme yapmayı öğrendik.

Bu yapılar, müfredatınızdaki Flask ve SQLite ile yapacağınız 
final projesinin (Kişisel blog ve not uygulaması) temelini oluşturacaktır. 
Artık ORM'nin hem temelini hem de ilişkisel gücünü kavramış durumdasınız!

"""