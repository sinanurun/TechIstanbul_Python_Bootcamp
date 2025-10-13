import json
import os # Dosya kontrolü için

# --------------------------
# 1. VARLIK SINIFI (MODEL)
# --------------------------
class Kitap:
    """Tek bir kitap nesnesini temsil eder."""
    
    def __init__(self, ad, yazar, sayfa, basim):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa
        self.basim = basim

    def __str__(self):
        # Kullanıcı dostu çıktı
        return f"{self.ad} ({self.basim}), Yazar: {self.yazar}, Sayfa: {self.sayfa}"

    def __repr__(self):
        # Geliştirici dostu çıktı (yeniden oluşturulabilir format)
        return f'Kitap("{self.ad}", "{self.yazar}", {self.sayfa}, {self.basim})'

    def to_dict(self):
        """Nesneyi JSON'a kaydetmek için sözlüğe çevirir."""
        # vars(self) yerine manuel döndürme daha güvenli ve açık.
        return {
            "ad": self.ad,
            "yazar": self.yazar,
            "sayfa": self.sayfa,
            "basim": self.basim
        }
    
    @classmethod
    def from_dict(cls, data):
        """Sözlükten Kitap nesnesi oluşturur."""
        return cls(data['ad'], data['yazar'], data['sayfa'], data['basim'])


# --------------------------
# 2. YÖNETİCİ SINIFI (CONTROLLER)
# --------------------------
class KutuphaneYoneticisi:
    """Kitap koleksiyonunu yönetir ve dosya işlemlerini kapsüller."""
    
    DOSYA_ADI = "kitaplar.json" # Sabit dosya adı
    
    def __init__(self):
        # Tüm kitap nesneleri bu listede tutulur.
        # Global kitap_listesi ve kitaplar listelerini kaldırdık.
        self.kitaplar = [] 
        self.kitaplari_yukle() # Başlangıçta kayıtlı kitapları belleğe yükle.

    def kitap_ekle(self, kitap):
        """Kitap nesnesini bellekteki listeye ekler."""
        if not isinstance(kitap, Kitap):
            raise TypeError("Sadece Kitap nesnesi eklenebilir.")
        self.kitaplar.append(kitap)

    def kitaplari_yukle(self):
        """JSON dosyasından tüm kitapları belleğe Kitap nesnesi olarak yükler."""
        if not os.path.exists(self.DOSYA_ADI):
            return

        try:
            with open(self.DOSYA_ADI, "r", encoding="utf-8") as file:
                veri_listesi = json.load(file)
        except (IOError, json.JSONDecodeError):
            # Dosya yoksa veya bozuksa, boş listeyle devam et.
            return
        
        # Dosyadan gelen sözlükleri Kitap nesnelerine çeviriyoruz (De-serileştirme)
        self.kitaplar = [Kitap.from_dict(veri) for veri in veri_listesi]
        
    def kitaplari_kaydet(self):
        """Bellekteki tüm kitapları JSON dosyasına kaydeder."""
        if not self.kitaplar:
            print("Kaydedilecek kitap yok.")
            return

        # Kitap nesnelerini sözlük listesine çeviriyoruz (Serileştirme)
        veri_listesi = [kitap.to_dict() for kitap in self.kitaplar]
        
        try:
            with open(self.DOSYA_ADI, "w", encoding="utf-8") as file:
                json.dump(veri_listesi, file, indent=4, ensure_ascii=False)
            print(f"Başarıyla {len(self.kitaplar)} kitap kaydedildi.")
        except IOError as e:
            print(f"HATA: Kayıt sırasında bir sorun oluştu: {e}")

    def tum_kitaplari_listele(self):
        """Bellekteki tüm kitapları listeler."""
        if not self.kitaplar:
            print("Kütüphanede kayıtlı kitap yok.")
            return

        print("\n--- KÜTÜPHANE İÇERİĞİ ---")
        for i, kitap in enumerate(self.kitaplar, 1):
            print(f"{i}. {kitap}")
        print("--------------------------\n")
        
    def yeni_kitap_olustur_ve_ekle(self):
        """Kullanıcıdan bilgi alıp yeni bir kitap nesnesi oluşturur ve ekler."""
        try:
            ad = input("Kitap Adı: ")
            yazar = input("Yazar: ")
            sayfa = int(input("Sayfa Sayısı: "))
            basim = int(input("Basım Yılı: "))
            
            yeni_kitap = Kitap(ad, yazar, sayfa, basim)
            self.kitap_ekle(yeni_kitap)
            print(f"'{ad}' başarıyla eklendi (Bellekte).")
        except ValueError:
            print("HATA: Sayfa veya yıl bilgisi geçerli bir sayı olmalıdır.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# --------------------------
# 3. ANA UYGULAMA DÖNGÜSÜ
# --------------------------
def menu(yonetici):
    while True:
        print("\n--- MENÜ ---")
        print("[E] Ekle (Yeni)")
        print("[L] Listele (Tüm Kitaplar)")
        print("[K] Kaydet (Dosyaya Yaz)")
        print("[Q] Çıkış")
        cevap = input("Seçiminiz: ").lower()

        if cevap == "e":
            yonetici.yeni_kitap_olustur_ve_ekle()
        elif cevap == "k":
            yonetici.kitaplari_kaydet()
        elif cevap == "l":
            yonetici.tum_kitaplari_listele()
        elif cevap == "q":
            print("Programdan çıkılıyor...")
            # İstenirse, çıkmadan önce kaydetme yapılabilir
            # yonetici.kitaplari_kaydet() 
            break
        else:
            print("Hatalı işlem girişi. Lütfen geçerli bir harf girin.")

if __name__ == "__main__":
    # Tüm uygulama yönetimi bu nesne üzerinden yürütülür.
    kutuphane = KutuphaneYoneticisi()
    menu(kutuphane)

"""
Tek Sorumluluk Prensibi (Single Responsibility Principle - SRP):

Kitap Sınıfı: Yalnızca tek bir kitapla ilgili veriyi tutmaktan ve kendini metin olarak temsil etmekten sorumludur (__str__, __repr__, to_dict).

KutuphaneYoneticisi Sınıfı: Kitap koleksiyonunu yönetmekten ve dosya I/O işlemlerini (kaydetme/yükleme) yürütmekten sorumludur.

Kapsülleme (Encapsulation):

Global değişkenler (kitap_listesi, kitaplar) kaldırıldı. Tüm kitap koleksiyonu, KutuphaneYoneticisi sınıfının içindeki self.kitaplar niteliğinde kapsüllendi. Dış kod, bu listeye direkt erişmek yerine yönetici sınıfının metotlarını kullanmak zorundadır.

Veri Serileştirme (Serialization):

vars(kitap) yerine, Kitap sınıfına to_dict() ve from_dict() metotları eklenerek, nesnenin JSON'a dönüştürülmesi (serileştirme) ve JSON'dan nesneye dönüştürülmesi (de-serileştirme) işlemleri, ilgili sınıfın sorumluluğuna verildi.

Kalıcılık (Persistence) Yönetimi:

Dosya yükleme (kitaplari_yukle) ve kaydetme (kitaplari_kaydet) mantığı tek bir sınıf içinde toplandı. Yükleme işleminin uygulama başladığında otomatik yapılması (__init__ içinde self.kitaplari_yukle()), kullanıcı deneyimini iyileştirdi ve veri akışını netleştirdi.

Kullanım Kolaylığı:

Kullanıcı girişi alma ve nesne oluşturma mantığı (yeni_kitap_olustur_ve_ekle) yönetici sınıfı içinde birleştirilerek, ana döngü (menu) daha basit tutuldu.

"""