import requests
from bs4 import BeautifulSoup
import csv
import time

# 1. Web sayfasını getir
url = "https://uzmanpara.milliyet.com.tr/borsa/en-cok-artanlar/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

print("Sayfa yükleniyor...")
response = requests.get(url, headers=headers)
response.raise_for_status()  # Hata varsa durdur

# 2. BeautifulSoup ile HTML'i işle
soup = BeautifulSoup(response.text, "lxml")

# 3. Hisse tablosunu bul (incelerken tbody > tr yapısını gördük)
hisse_satirlari = soup.select("tbody tr")  # Tüm satırları seç

if not hisse_satirlari:
    print("❌ Hisse verisi bulunamadı! Sayfa yapısı değişmiş olabilir.")
    exit()

print(f"✅ Toplam {len(hisse_satirlari)} hisse satırı bulundu.")

# 4. Verileri topla
veriler = []
for satir in hisse_satirlari[:15]:  # İlk 15 hisseyi al
    hucreler = satir.find_all("td")
    if len(hucreler) < 6:
        continue  # Eksik satırı atla

    try:
        sembol = hucreler[0].text.strip()
        fiyat = hucreler[1].text.strip().replace(",", ".")
        degisim = hucreler[2].text.strip().replace("%", "").replace(",", ".")
        hacim = hucreler[5].text.strip().replace(".", "")  # Binlik ayıraçları kaldır

        # Sayısal değerlere çevir (isteğe bağlı, CSV için string de yeterli)
        # fiyat = float(fiyat) if fiyat else 0.0
        # degisim = float(degisim) if degisim else 0.0
        # hacim = int(hacim) if hacim.isdigit() else 0

        veriler.append([sembol, fiyat, degisim, hacim])
    except Exception as e:
        print(f"Hata: {e}")
        continue

    time.sleep(0.1)  # Sunucuya nazik ol

# 5. Sonuçları göster
print("\n📋 Çekilen Veriler:")
print("Hisse | Fiyat | Değişim(%) | Hacim")
print("-" * 40)
for v in veriler:
    print(f"{v[0]:<8} | {v[1]:<7} | {v[2]:<10} | {v[3]}")


# 6. CSV dosyasına yaz
dosya_adi = "bist_hisseler.csv"
with open(dosya_adi, mode="w", encoding="utf-8-sig", newline="") as dosya:
    yazici = csv.writer(dosya)
    # Başlık satırı
    yazici.writerow(["Hisse", "Fiyat (TL)", "Değişim (%)", "Hacim"])
    # Veri satırları
    yazici.writerows(veriler)

print(f"\n✅ Veriler '{dosya_adi}' dosyasına başarıyla kaydedildi.")
