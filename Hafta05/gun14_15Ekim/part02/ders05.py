import requests
from bs4 import BeautifulSoup
import csv

# 1. Web sayfasını getir
url = "https://www.izko.org.tr/Home/GuncelKur"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("🌐 İZKO döviz kurları yükleniyor...")
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"❌ Sayfa yüklenemedi: {e}")
    exit()

# 2. HTML'i işle
soup = BeautifulSoup(response.text, "lxml")

# 3. Tabloyu bul
table = soup.find("table", {"class": "table table-bordered"})
if table is None:
    print("❌ Tablo bulunamadı! Sayfa yapısı değişmiş olabilir.")
    exit()

# 4. Satırları al (başlık hariç)
rows = table.find_all("tr")[1:]  # İlk satır başlık
if not rows:
    print("❌ Satır bulunamadı.")
    exit()

# 5. Verileri topla
kurlar = []
for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 3:
        doviz = cols[0].text.strip()
        alis = cols[1].text.strip().replace(",", ".")
        satis = cols[2].text.strip().replace(",", ".")
        kurlar.append([doviz, alis, satis])

# 6. Sonuçları ekrana yaz
print("\n✅ Güncel Döviz Kurları:")
print(f"{'Döviz':<8} | {'Alış':<10} | {'Satış':<10}")
print("-" * 30)
for k in kurlar:
    print(f"{k[0]:<8} | {k[1]:<10} | {k[2]:<10}")