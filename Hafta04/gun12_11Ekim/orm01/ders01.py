"""
SQLAlchemy, veritabanı işlemlerini tamamen Python nesneleri ve sınıfları üzerinden yapmanızı sağlayarak, 
SQL yazma ihtiyacını neredeyse tamamen ortadan kaldırır.

SQLAlchemy ORM ile Kütüphane Yönetimi
1. ORM Nedir?
ORM (Object-Relational Mapping), Nesne-İlişkisel Eşleme anlamına gelir.

Amaç: Python'da yazdığınız sınıflar ve nesneler (Object) ile veritabanındaki tablolar ve 
satırlar (Relational) arasında bir köprü kurmaktır.

Faydası: SQL komutlarını (SELECT, INSERT, UPDATE, DELETE) doğrudan yazmak yerine, 
veritabanı işlemlerini sanki normal Python nesneleriyle uğraşıyormuş gibi yaparsınız. 
Bu, kodunuzu daha güvenli, okunaklı ve veritabanından bağımsız hale getirir.

2. SQLAlchemy Temelleri
Bu örnek için, SQLAlchemy'nin Declarative yapısını kullanacağız.

(Not: Başlamadan önce SQLAlchemy'nin kurulu olması gerekir: pip install sqlalchemy)

Adım A: Bağlantı ve Yapılandırma
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Veritabanı Bağlantısı (Engine) Oluşturma
# SQLite kullanıyoruz ve 'kutuphane_orm.db' adında bir dosya oluşturulacak.
engine = create_engine('sqlite:///kutuphane_orm.db')

# 2. Temel Sınıfı (Base) Tanımlama
# SQLAlchemy'nin tüm model sınıfları bu sınıftan türeyecektir.
Base = declarative_base()

# 3. Oturum (Session) Yapılandırması
# Oturum, veritabanına sorgu göndermek ve sonuçları almak için kullanılan ana araçtır.
Session = sessionmaker(bind=engine)
session = Session()

"""
Adım B: Model (Tablo) Sınıfını Tanımlama
Daha önce oluşturduğumuz Kitap sınıfını, SQLAlchemy'nin gerektirdiği şekilde yeniden tanımlayacağız. 
Bu sınıf, veritabanındaki kitaplar tablosuna karşılık gelir.

"""

class Kitap(Base):
    # Veritabanında kullanılacak tablo adı
    __tablename__ = 'kitaplar'

    # Sütun Tanımları (Veri Tipleri)
    id = Column(Integer, primary_key=True)
    ad = Column(String)
    yazar = Column(String)
    
    # OOP'deki __init__ metoduna gerek yoktur, Base sınıfı otomatik yapar.

    # Nesneyi yazdırırken okunur bir çıktı sağlamak için __repr__
    def __repr__(self):
        return f"Kitap(id={self.id}, ad='{self.ad}', yazar='{self.yazar}')"

# Oluşturduğumuz tüm modelleri (tabloları) veritabanına yansıtır.
Base.metadata.create_all(engine)

"""
3. CRUD İşlemlerini SQLAlchemy ile Güncelleme
Artık, daha önceki oturumdaki CRUD işlemlerini SQL yerine, SQLAlchemy Session metotlarını kullanarak yapabiliriz.

Örnek 1: C (Create) - Kitap Ekleme
Bir Python nesnesi oluşturup, oturuma ekleyerek ve commit() ile kaydederek ekleme yapılır.
"""

# print("\n--- 1. EKLEME (CREATE) ---")

# # Python Nesneleri Oluşturma
# kitap_1 = Kitap(ad="Python Temelleri", yazar="Ali")
# kitap_2 = Kitap(ad="Flask Web Geliştirme", yazar="veli")
# kitap_3 = Kitap(ad="SQLAlchemy Kılavuzu", yazar="Can")

# # Oturuma Ekleme (Henüz veritabanına gitmedi)
# session.add(kitap_1)
# session.add_all([kitap_2, kitap_3]) # Birden fazla ekleme

# # Değişiklikleri Veritabanına Kaydetme (COMMIT)
# session.commit()

# print(f"Kitaplar eklendi. ID'ler: {kitap_1.id}, {kitap_2.id}, {kitap_3.id}")

"""
Örnek 2: R (Read) - Tümünü Okuma
session.query(Model) ile sorgu oluşturulur. .all() ile tüm sonuçlar nesne listesi olarak alınır.
"""

# print("\n--- 2. TÜMÜNÜ OKUMA (READ ALL) ---")

# # Tüm Kitapları Sorgulama
# tum_kitaplar = session.query(Kitap).all()

# for kitap in tum_kitaplar:
#     print(kitap)

"""
Örnek 3: R (Read) - Koşullu Okuma (Filtreleme)
.filter() metodu, SQL'deki WHERE koşulunu Pythonic bir şekilde yazmamızı sağlar.
"""

print("\n--- 3. KOŞULLU OKUMA (FILTER) ---")

# Yazar 'Ali' olan kitapları sorgula
ali_kitaplari = session.query(Kitap).filter(Kitap.yazar == 'Ali').all()

print("Ali'nin Kitapları:")
for kitap in ali_kitaplari:
    print(f"- {kitap.ad}")

# ID'si 2 olan tek bir kitabı alma (SELECT * FROM kitaplar WHERE id = 2 LIMIT 1)
kitap_id_2 = session.query(Kitap).filter(Kitap.id == 2).one_or_none()

if kitap_id_2:
    print(f"\nID 2 olan kitap: {kitap_id_2}")

"""
Örnek 4: U (Update) - Güncelleme
Önce nesne sorguyla alınır, sonra Python'da özniteliği değiştirilir ve commit() yapılır.
"""

print("\n--- 4. GÜNCELLEME (UPDATE) ---")

# ID'si 1 olan kitabı bul
kitap_guncellenecek = session.query(Kitap).filter(Kitap.id == 1).first()

if kitap_guncellenecek:
    print(f"Güncellemeden önce: {kitap_guncellenecek.ad}")
    
    # Python nesnesinin özniteliğini değiştirme (SQLAlchemy bunu takip eder)
    kitap_guncellenecek.ad = "Python ve Data Science Giriş"
    
    # Değişikliği veritabanına kaydetme
    session.commit()
    print(f"Güncelleme sonrası: {kitap_guncellenecek.ad}")
"""
Örnek 5: D (Delete) - Silme
Önce nesne sorguyla alınır, sonra session.delete() metodu kullanılır ve commit() yapılır.
"""

print("\n--- 5. SİLME (DELETE) ---")

# Yazar 'Bob' olan kitabı bul
kitap_silinecek = session.query(Kitap).filter(Kitap.yazar == 'Bob').first()

if kitap_silinecek:
    print(f"'{kitap_silinecek.ad}' siliniyor.")
    
    # Oturumdan silme komutu
    session.delete(kitap_silinecek)
    
    # Değişikliği veritabanına kaydetme
    session.commit()
    print("Silme başarılı.")

# Silme sonrası kontrol
kalan_kitaplar = session.query(Kitap).all()
print("\nKalan Kitaplar:")
for kitap in kalan_kitaplar:
    print(kitap)

"""
Örnek 6: Toplamsal İşlemler (Aggregate)
SQL'deki COUNT, SUM, AVG gibi toplamsal (aggregate) fonksiyonları kullanma.

""" 

from sqlalchemy import func

print("\n--- 6. TOPLAMSAL İŞLEMLER (COUNT) ---")

# Veritabanındaki toplam kitap sayısını bul
toplam_kitap_sayisi = session.query(func.count(Kitap.id)).scalar()
print(f"Veritabanındaki toplam kitap sayısı: {toplam_kitap_sayisi}")

# Yazar ismine göre gruplayarak her yazarın kaç kitabı olduğunu bul (GROUP BY)
kitap_sayilari_yazara_gore = session.query(Kitap.yazar, func.count(Kitap.id)).group_by(Kitap.yazar).all()

print("\nYazarlara göre kitap sayıları:")
for yazar, sayi in kitap_sayilari_yazara_gore:
    print(f"- {yazar}: {sayi} kitap")