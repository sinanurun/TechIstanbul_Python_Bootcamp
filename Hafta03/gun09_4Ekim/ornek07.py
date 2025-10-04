"""
KULLANIM SENARYOSU:
CSV dosyalarından veri okuyup basit analizler yapmak.
Satış raporları, öğrenci notları gibi tablo verileri için.

NEDEN BU ÖRNEK:
- CSV DictReader kullanımı
- Veri filtreleme ve analiz
- Liste comprehensions
- Hata yönetimi
"""

import csv

def csv_analiz_et(dosya_adi, filtre=None):
    """
    CSV dosyasını analiz eder ve istatistikler döndürür
    
    Args:
        dosya_adi: Analiz edilecek CSV dosyası
        filtre: Sözlük formatında filtre (örn: {'bolum': 'Bilgisayar'})
    """
    
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            okuyucu = csv.DictReader(dosya)
            veriler = list(okuyucu)
        
        if not veriler:
            return {"hata": "Dosya boş veya geçersiz"}
        
        # Filtre uygula
        if filtre:
            for anahtar, deger in filtre.items():
                veriler = [v for v in veriler if v.get(anahtar) == deger]
        
        # İstatistikleri hesapla
        if 'not' in veriler[0]:
            notlar = [int(v['not']) for v in veriler if v['not'].isdigit()]
            istatistikler = {
                'kayit_sayisi': len(veriler),
                'ortalama': sum(notlar) / len(notlar) if notlar else 0,
                'maksimum': max(notlar) if notlar else 0,
                'minimum': min(notlar) if notlar else 0,
                'filtre': filtre
            }
        else:
            istatistikler = {
                'kayit_sayisi': len(veriler),
                'alanlar': list(veriler[0].keys()),
                'filtre': filtre
            }
        
        return istatistikler
        
    except FileNotFoundError:
        return {"hata": "Dosya bulunamadı"}
    except Exception as e:
        return {"hata": str(e)}

# Örnek CSV oluştur
with open("ogrenciler.csv", "w", newline="", encoding="utf-8") as f:
    yazici = csv.writer(f)
    yazici.writerow(["isim", "bolum", "not"])
    yazici.writerows([
        ["Ali", "Bilgisayar", "85"],
        ["Ayşe", "Matematik", "92"],
        ["Mehmet", "Bilgisayar", "78"],
        ["Zeynep", "Fizik", "88"]
    ])

# Analiz yap
sonuc = csv_analiz_et("ogrenciler.csv", filtre={"bolum": "Bilgisayar"})
print("Analiz Sonucu:", sonuc)