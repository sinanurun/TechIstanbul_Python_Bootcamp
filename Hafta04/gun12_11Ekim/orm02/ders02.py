# Örnek 1: SQLAlchemy Kurulumu ve Temel Bağlantı
"""
SQLALCHEMY KURULUMU:
pip install sqlalchemy

TEMEL BİLEŞENLER:
1. Engine: Veritabanı bağlantısı
2. Session: Veritabanı işlemleri
3. Base: Tüm modellerin temel sınıfı
4. Model: Veritabanı tablolarını temsil eden sınıflar
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# 1. BASE SINIFI OLUŞTURMA
# Tüm model sınıfları bu sınıftan türeyecek
Base = declarative_base()

# 2. VERİTABANI BAĞLANTISI (ENGINE)
# SQLite veritabanı oluştur
engine = create_engine('sqlite:///orm_ogrenci.db', echo=True)
# echo=True: SQL sorgularını terminalde gösterir (öğrenme için faydalı)

# 3. SESSION OLUŞTURUCU
# Veritabanı işlemleri için session factory
Session = sessionmaker(bind=engine)

print("✅ SQLAlchemy başarıyla yapılandırıldı!")