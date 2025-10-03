import csv
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "ogrenciler.csv"



# CSV dosyasına yazma
with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:
    yazici = csv.writer(dosya)
    yazici.writerow(["Ad", "Soyad", "Not"])  # Başlık satırı
    yazici.writerow(["Ali", "Yılmaz", 85])
    yazici.writerow(["Ayşe", "Kaya", 92])

# CSV dosyasını okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(satir)

# # Sözlük formatında CSV işlemleri
# with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:
#     alanlar = ["ad", "soyad", "not"]
#     yazici = csv.DictWriter(dosya, fieldnames=alanlar)
#     yazici.writeheader()
#     yazici.writerow({"ad": "Mehmet", "soyad": "Demir", "not": 78})

# CSV dosyasını okuma
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        print(satir)
#CSV’yi Sözlük Olarak Okumak  
with open(dosya_adi, "r",  encoding="utf-8") as f:
    basliklar = f.readline().strip().split(",")
    for satir in f:
        degerler = satir.strip().split(",")
        ogrenci = dict(zip(basliklar, degerler))
        print(ogrenci)