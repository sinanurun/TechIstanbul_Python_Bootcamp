# ÖRNEK 3 ve 4'Ü BİRLEŞTİREN ENTEGRE ÖRNEK
# Öğrenci Not Sistemi - İlişkiler ve Transaction Yönetimi

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, and_, or_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# 1. TEMEL YAPILANDIRMA
Base = declarative_base()

# Veritabanı bağlantısı
engine = create_engine('sqlite:///entegre_ogrenci.db', echo=True)
Session = sessionmaker(bind=engine)

# 2. MODEL SINIFLARI (Örnek 3'ten)
class Ogrenci(Base):
    __tablename__ = 'ogrenciler'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ogrenci_no = Column(String(20), unique=True, nullable=False)
    ad = Column(String(50), nullable=False)
    soyad = Column(String(50), nullable=False)
    sinif = Column(String(10), nullable=False)
    kayit_tarihi = Column(DateTime, default=datetime.now)
    
    # İLİŞKİ: Bir öğrencinin birden fazla notu olabilir
    notlar = relationship("Not", back_populates="ogrenci", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Ogrenci({self.ad} {self.soyad}, No:{self.ogrenci_no})>"
    
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"
    
    def not_ortalamasi(self):
        """Öğrencinin tüm derslerdeki genel ortalamasını hesaplar"""
        if self.notlar:
            toplam = sum(not_kaydi.ortalama for not_kaydi in self.notlar)
            return toplam / len(self.notlar)
        return 0

class Ders(Base):
    __tablename__ = 'dersler'
    
    id = Column(Integer, primary_key=True)
    ders_kodu = Column(String(10), unique=True, nullable=False)
    ders_adi = Column(String(100), nullable=False)
    ogretmen = Column(String(100))
    kredi = Column(Integer, default=1)
    
    # İLİŞKİ: Bir derse birden fazla not kaydı olabilir
    notlar = relationship("Not", back_populates="ders")
    
    def __repr__(self):
        return f"<Ders({self.ders_kodu}: {self.ders_adi})>"

class Not(Base):
    __tablename__ = 'notlar'
    
    id = Column(Integer, primary_key=True)
    
    # FOREIGN KEY'ler - İlişkileri tanımlar
    ogrenci_id = Column(Integer, ForeignKey('ogrenciler.id', ondelete="CASCADE"))
    ders_id = Column(Integer, ForeignKey('dersler.id'))
    
    # Not bilgileri
    vize_notu = Column(Float, default=0)
    final_notu = Column(Float, default=0)
    ortalama = Column(Float, default=0)
    harf_notu = Column(String(2))
    donem = Column(String(10))
    
    # İLİŞKİLER - Diğer tablolara bağlantı
    ogrenci = relationship("Ogrenci", back_populates="notlar")
    ders = relationship("Ders", back_populates="notlar")
    
    def __repr__(self):
        return f"<Not({self.ogrenci.ad} - {self.ders.ders_adi}: {self.ortalama})>"
    
    def not_hesapla(self):
        """Not ortalamasını hesaplar ve harf notunu belirler"""
        self.ortalama = (self.vize_notu * 0.4) + (self.final_notu * 0.6)
        
        if self.ortalama >= 90: self.harf_notu = "AA"
        elif self.ortalama >= 85: self.harf_notu = "BA"
        elif self.ortalama >= 80: self.harf_notu = "BB"
        elif self.ortalama >= 75: self.harf_notu = "CB"
        elif self.ortalama >= 70: self.harf_notu = "CC"
        elif self.ortalama >= 65: self.harf_notu = "DC"
        elif self.ortalama >= 60: self.harf_notu = "DD"
        elif self.ortalama >= 50: self.harf_notu = "FD"
        else: self.harf_notu = "FF"
        
        return self.ortalama

# 3. VERİTABANI İŞLEMLERİ SINIFI
class OgrenciNotYoneticisi:
    """Öğrenci not sistemini yöneten sınıf - Örnek 3 ve 4'ü birleştirir"""
    
    def __init__(self):
        self.session = Session()
        self.tablolari_olustur()
        self.ornek_verileri_ekle()
    
    def tablolari_olustur(self):
        """Tabloları oluşturur"""
        Base.metadata.create_all(engine)
        print("✅ Tablolar oluşturuldu!")
    
    def ornek_verileri_ekle(self):
        """Örnek verileri ekler - TRANSACTION örneği"""
        try:
            # TRANSACTION BAŞLANGICI
            print("\n🔄 Örnek veriler ekleniyor (Transaction)...")
            
            # Öğrenciler
            ogrenciler = [
                Ogrenci(ogrenci_no="2023001", ad="Ali", soyad="Yılmaz", sinif="10-A"),
                Ogrenci(ogrenci_no="2023002", ad="Ayşe", soyad="Kaya", sinif="10-B"),
                Ogrenci(ogrenci_no="2023003", ad="Mehmet", soyad="Demir", sinif="10-A"),
            ]
            self.session.add_all(ogrenciler)
            self.session.flush()  # ID'leri al
            
            # Dersler
            dersler = [
                Ders(ders_kodu="MAT101", ders_adi="Matematik", ogretmen="Ahmet Hoca", kredi=4),
                Ders(ders_kodu="FIZ101", ders_adi="Fizik", ogretmen="Mehmet Hoca", kredi=3),
                Ders(ders_kodu="ING101", ders_adi="İngilizce", ogretmen="Zeynep Hoca", kredi=2),
            ]
            self.session.add_all(dersler)
            self.session.flush()
            
            # Notlar - İLİŞKİLERİ KULLANARAK
            notlar = [
                # Ali'nin notları
                Not(ogrenci_id=1, ders_id=1, vize_notu=75, final_notu=80, donem="2023-1"),
                Not(ogrenci_id=1, ders_id=2, vize_notu=65, final_notu=70, donem="2023-1"),
                
                # Ayşe'nin notları
                Not(ogrenci_id=2, ders_id=1, vize_notu=85, final_notu=90, donem="2023-1"),
                Not(ogrenci_id=2, ders_id=3, vize_notu=78, final_notu=82, donem="2023-1"),
                
                # Mehmet'in notları
                Not(ogrenci_id=3, ders_id=2, vize_notu=55, final_notu=60, donem="2023-1"),
                Not(ogrenci_id=3, ders_id=3, vize_notu=70, final_notu=75, donem="2023-1"),
            ]
            
            # Not ortalamalarını hesapla
            for not_kaydi in notlar:
                not_kaydi.not_hesapla()
            
            self.session.add_all(notlar)
            
            # TRANSACTION COMMIT
            self.session.commit()
            print("✅ Örnek veriler başarıyla eklendi!")
            
        except Exception as e:
            # HATA DURUMUNDA ROLLBACK
            self.session.rollback()
            print(f"❌ Hata! Transaction geri alındı: {e}")
    
    # 4. İLİŞKİLERİ KULLANAN SORGULAR (Örnek 3'ten)
    def ogrenci_detay_goster(self, ogrenci_no):
        """Öğrenci detaylarını ve notlarını gösterir - İLİŞKİ KULLANIMI"""
        print(f"\n📊 {ogrenci_no} NUMARALI ÖĞRENCİ DETAYLARI")
        print("=" * 50)
        
        ogrenci = self.session.query(Ogrenci).filter(
            Ogrenci.ogrenci_no == ogrenci_no
        ).first()
        
        if not ogrenci:
            print("❌ Öğrenci bulunamadı!")
            return
        
        # ÖĞRENCİ BİLGİLERİ
        print(f"👤 Ad Soyad: {ogrenci.tam_ad()}")
        print(f"🏫 Sınıf: {ogrenci.sinif}")
        print(f"📅 Kayıt Tarihi: {ogrenci.kayit_tarihi.strftime('%d/%m/%Y')}")
        print(f"📈 Genel Ortalama: {ogrenci.not_ortalamasi():.2f}")
        
        # NOTLARI GÖSTER - İLİŞKİ ÜZERİNDEN ERİŞİM
        print("\n📚 DERS NOTLARI:")
        print("-" * 40)
        
        for not_kaydi in ogrenci.notlar:  # İLİŞKİ: ogrenci.notlar
            print(f"  📖 {not_kaydi.ders.ders_adi:12} | "  # İLİŞKİ: not_kaydi.ders
                  f"Vize: {not_kaydi.vize_notu:3} | "
                  f"Final: {not_kaydi.final_notu:3} | "
                  f"Ort: {not_kaydi.ortalama:5.1f} | "
                  f"Harf: {not_kaydi.harf_notu}")
    
    def sinif_listesi_goster(self, sinif_adi):
        """Sınıf listesini ve ortalamalarını gösterir"""
        print(f"\n👥 {sinif_adi} SINIFI LİSTESİ")
        print("=" * 40)
        
        ogrenciler = self.session.query(Ogrenci).filter(
            Ogrenci.sinif == sinif_adi
        ).order_by(Ogrenci.ad).all()
        
        for ogrenci in ogrenciler:
            ortalama = ogrenci.not_ortalamasi()
            durum = "✅" if ortalama >= 70 else "⚠️ " if ortalama >= 50 else "❌"
            print(f"  {durum} {ogrenci.tam_ad():20} | Ort: {ortalama:5.1f}")
    
    def ders_istatistikleri(self, ders_kodu):
        """Ders bazlı istatistikleri gösterir - GELİŞMİŞ SORGULAR"""
        print(f"\n📈 {ders_kodu} DERSİ İSTATİSTİKLERİ")
        print("=" * 50)
        
        # GRUPLAMA VE İSTATİSTİK SORGUSU
        istatistik = self.session.query(
            func.count(Not.id).label('ogrenci_sayisi'),
            func.avg(Not.ortalama).label('ortalama'),
            func.min(Not.ortalama).label('min_not'),
            func.max(Not.ortalama).label('max_not'),
            func.sum(case((Not.harf_notu.in_(["AA", "BA", "BB", "CB", "CC"]), 1), else_=0)).label('gecen_sayisi'),
            func.sum(case((Not.harf_notu.in_(["DC", "DD", "FD", "FF"]), 1), else_=0)).label('kalan_sayisi')
        ).join(Ders).filter(Ders.ders_kodu == ders_kodu).first()
        
        if istatistik and istatistik.ogrenci_sayisi > 0:
            ogrenci_sayisi, ortalama, min_not, max_not, gecen, kalan = istatistik
            
            print(f"👥 Öğrenci Sayısı: {ogrenci_sayisi}")
            print(f"📊 Sınıf Ortalaması: {ortalama:.2f}")
            print(f"📉 En Düşük Not: {min_not:.1f}")
            print(f"📈 En Yüksek Not: {max_not:.1f}")
            print(f"✅ Geçen Öğrenci: {gecen}")
            print(f"❌ Kalan Öğrenci: {kalan}")
            print(f"🎯 Başarı Oranı: %{(gecen/ogrenci_sayisi)*100:.1f}")
        else:
            print("❌ Bu ders için veri bulunamadı!")
    
    # 5. TRANSACTION YÖNETİMİ (Örnek 4'ten)
    def yeni_ogrenci_ekle(self, ogrenci_no, ad, soyad, sinif):
        """Yeni öğrenci ekler - TRANSACTION YÖNETİMİ"""
        try:
            print(f"\n🔄 {ad} {soyad} öğrencisi ekleniyor...")
            
            # Yeni öğrenci oluştur
            yeni_ogrenci = Ogrenci(
                ogrenci_no=ogrenci_no,
                ad=ad,
                soyad=soyad,
                sinif=sinif
            )
            
            self.session.add(yeni_ogrenci)
            self.session.commit()  # TRANSACTION COMMIT
            
            print(f"✅ {ad} {soyad} başarıyla eklendi!")
            return yeni_ogrenci
            
        except Exception as e:
            self.session.rollback()  # HATA DURUMUNDA ROLLBACK
            print(f"❌ Öğrenci eklenemedi: {e}")
            return None
    
    def ogrenci_sil(self, ogrenci_no):
        """Öğrenciyi ve tüm notlarını siler - CASCADE DELETE"""
        try:
            print(f"\n🔄 {ogrenci_no} numaralı öğrenci siliniyor...")
            
            ogrenci = self.session.query(Ogrenci).filter(
                Ogrenci.ogrenci_no == ogrenci_no
            ).first()
            
            if not ogrenci:
                print("❌ Öğrenci bulunamadı!")
                return False
            
            # Öğrenciyi sil (CASCADE sayesinde notlar da silinecek)
            self.session.delete(ogrenci)
            self.session.commit()  # TRANSACTION COMMIT
            
            print(f"✅ {ogrenci.tam_ad()} ve tüm notları silindi!")
            return True
            
        except Exception as e:
            self.session.rollback()  # HATA DURUMUNDA ROLLBACK
            print(f"❌ Silme işlemi başarısız: {e}")
            return False
    
    def not_ekle(self, ogrenci_no, ders_kodu, vize, final, donem):
        """Yeni not ekler - TRANSACTION ve İLİŞKİ KULLANIMI"""
        try:
            print(f"\n🔄 {ogrenci_no} için {ders_kodu} notu ekleniyor...")
            
            # Öğrenci ve dersi bul
            ogrenci = self.session.query(Ogrenci).filter(
                Ogrenci.ogrenci_no == ogrenci_no
            ).first()
            
            ders = self.session.query(Ders).filter(
                Ders.ders_kodu == ders_kodu
            ).first()
            
            if not ogrenci or not ders:
                print("❌ Öğrenci veya ders bulunamadı!")
                return False
            
            # Yeni not kaydı oluştur
            yeni_not = Not(
                ogrenci_id=ogrenci.id,
                ders_id=ders.id,
                vize_notu=vize,
                final_notu=final,
                donem=donem
            )
            
            # Ortalamayı hesapla
            yeni_not.not_hesapla()
            
            self.session.add(yeni_not)
            self.session.commit()  # TRANSACTION COMMIT
            
            print(f"✅ {ogrenci.tam_ad()} - {ders.ders_adi} notu eklendi: {yeni_not.ortalama:.1f} ({yeni_not.harf_notu})")
            return True
            
        except Exception as e:
            self.session.rollback()  # HATA DURUMUNDA ROLLBACK
            print(f"❌ Not eklenemedi: {e}")
            return False
    
    def session_kapat(self):
        """Session'ı kapat"""
        self.session.close()
        print("\n🔒 Veritabanı bağlantısı kapatıldı.")

# 6. ANA PROGRAM - ÖRNEK 3 ve 4'Ü BİRLEŞTİREN KULLANIM
def main():
    print("🎓 ÖĞRENCİ NOT SİSTEMİ - ORM ENTEGRASYONU")
    print("=" * 55)
    
    # Sistem yöneticisini oluştur
    yonetici = OgrenciNotYoneticisi()
    
    try:
        # İLİŞKİLERİ GÖSTEREN SORGULAR
        print("\n1. 🔗 İLİŞKİLERİ KULLANAN SORGULAR")
        yonetici.ogrenci_detay_goster("2023001")  # Ali'nin detayları
        yonetici.sinif_listesi_goster("10-A")     # 10-A sınıfı
        yonetici.ders_istatistikleri("MAT101")    # Matematik istatistikleri
        
        # TRANSACTION YÖNETİMİ ÖRNEKLERİ
        print("\n2. 🔄 TRANSACTION YÖNETİMİ ÖRNEKLERİ")
        
        # Başarılı transaction - Yeni öğrenci
        yonetici.yeni_ogrenci_ekle("2023004", "Zeynep", "Şahin", "10-B")
        
        # Başarılı transaction - Yeni not
        yonetici.not_ekle("2023004", "ING101", 88, 92, "2023-1")
        
        # İlişkileri tekrar göster
        yonetici.ogrenci_detay_goster("2023004")
        
        # Silme işlemi - CASCADE DELETE testi
        print("\n3. 🗑️  SİLME İŞLEMİ (CASCADE TEST)")
        yonetici.ogrenci_sil("2023004")
        
        # Kompleks sorgu - Başarılı öğrenciler
        print("\n4. 🏆 BAŞARILI ÖĞRENCİLER (Ortalama >= 70)")
        basarili_ogrenciler = yonetici.session.query(Ogrenci).filter(
            Ogrenci.notlar.any(Not.ortalama >= 70)  # İLİŞKİ ÜZERİNDEN FİLTRELEME
        ).all()
        
        for ogrenci in basarili_ogrenciler:
            print(f"  ✅ {ogrenci.tam_ad()} - Ort: {ogrenci.not_ortalamasi():.1f}")
        
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
    finally:
        yonetici.session_kapat()

# SQLAlchemy case fonksiyonu için import
from sqlalchemy import case

if __name__ == "__main__":
    main()