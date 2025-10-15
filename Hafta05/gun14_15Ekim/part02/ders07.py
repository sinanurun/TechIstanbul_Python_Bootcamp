import requests
from bs4 import BeautifulSoup
import csv

# 1. İstek gönder
url = "https://uzmanpara.milliyet.com.tr/altin-fiyatlari/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("🪙 Uzmanpara'dan altın fiyatları çekiliyor...\n")

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Sayfa yüklenemedi! HTTP {response.status_code}")
    exit()

# 2. BeautifulSoup ile HTML'i UTF-8 olarak işle
soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")

# 3. Altın bloklarını bul
altin_bloklari = soup.find_all("div", class_="realTimeBox")
if not altin_bloklari:
    print("❌ Altın verisi bulunamadı! Sayfa yapısı değişmiş olabilir.")
    exit()

# 4. Verileri topla ve konsola yazdır
veriler = []
print(f"{'Altın Türü':<20} | {'Alış (TL)':<12} | {'Satış (TL)':<12}")
print("-" * 52)

for blok in altin_bloklari:
    # Altın türünü al
    tur_etiketi = blok.find("span", class_="doviz")
    if not tur_etiketi:
        continue
    tur = tur_etiketi.text.strip()

    # Alış ve satış bloklarını al
    alis_blok = blok.find("div", class_="realTimeBoxL")
    satis_blok = blok.find("div", class_="realTimeBoxR")
    if not alis_blok or not satis_blok:
        continue

    # Metinden sadece rakamı çıkar
    alis = alis_blok.text.replace("ALIŞ (TL)", "").strip()
    satis = satis_blok.text.replace("SATIŞ (TL)", "").strip()

    # Virgül/nokta temizliği (sayı formatına uygun hale getir)
    alis_temiz = alis.replace(".", "").replace(",", ".")
    satis_temiz = satis.replace(".", "").replace(",", ".")

    # ✅ KONSOLA YAZDIR
    print(f"{tur:<20} | {alis_temiz:<12} | {satis_temiz:<12}")

    # Listeye ekle (CSV için)
    veriler.append([tur, alis_temiz, satis_temiz])

print("\n✅ Veriler başarıyla konsola yazdırıldı.")

# 5. CSV'ye kaydet (Türkçe karakterler düzgün gözüksün diye utf-8-sig)
with open("altin_fiyatlari.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Altın Türü", "Alış (TL)", "Satış (TL)"])
    writer.writerows(veriler)

print("💾 Veriler 'altin_fiyatlari.csv' dosyasına kaydedildi.")