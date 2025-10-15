import requests
from bs4 import BeautifulSoup
import csv
import time

# 1. Sayfayı getir
url = "https://uzmanpara.milliyet.com.tr/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("🌐 Uzmanpara döviz kurları yükleniyor...")
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"❌ Sayfa yüklenemedi: {e}")
    exit()

# 2. HTML'i işle
soup = BeautifulSoup(response.text, "lxml")

# 3. Döviz tablosunu bul
# İnceleme sonucu: tablo doğrudan <table> içinde ve class'sız olabilir
# Ama genellikle "döviz" kelimesiyle ilişkili bir yapı vardır.
# Güvenli yol: tüm tabloları tarayıp ilk 4 sütunlu olanı seç

tables = soup.find_all("table")
doviz_tablosu = None

for table in tables:
    rows = table.find_all("tr")
    if len(rows) > 1:
        first_row = rows[1]
        cols = first_row.find_all("td")
        if len(cols) >= 4 and "/" in cols[0].text:  # EUR/USD gibi içeriyorsa
            doviz_tablosu = table
            break

if doviz_tablosu is None:
    print("❌ Döviz tablosu bulunamadı!")
    exit()

# 4. Satırları işle
veriler = []
satirlar = doviz_tablosu.find_all("tr")[1:]  # Başlık hariç

for satir in satirlar:
    hucreler = satir.find_all("td")
    if len(hucreler) >= 4:
        doviz_cifti = hucreler[0].text.strip()
        alis = hucreler[1].text.strip().replace(",", ".")
        satis = hucreler[2].text.strip().replace(",", ".")
        degisim = hucreler[3].text.strip().replace("%", "").replace(",", ".").strip()

        veriler.append([doviz_cifti, alis, satis, degisim])

# 5. Ekrana yaz
print("\n✅ Güncel Döviz Kurları:")
print(f"{'Çift':<10} | {'Alış':<10} | {'Satış':<10} | {'Değişim(%)':<10}")
print("-" * 50)
for v in veriler:
    print(f"{v[0]:<10} | {v[1]:<10} | {v[2]:<10} | {v[3]:<10}")

time.sleep(1)  # Sunucuya nazik ol

# 6. CSV'ye kaydet
dosya_adi = "uzmanpara_doviz_kurlari.csv"
try:
    with open(dosya_adi, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Döviz Çifti", "Alış (TL)", "Satış (TL)", "Değişim (%)"])
        writer.writerows(veriler)
    print(f"\n💾 Veriler '{dosya_adi}' dosyasına kaydedildi.")
except Exception as e:
    print(f"❌ Dosya kaydedilemedi: {e}")