import requests
from datetime import datetime

def kripto_fiyat_dosya(kripto_adi):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={kripto_adi.lower()}&vs_currencies=usd,try"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if kripto_adi.lower() in data:
                usd = data[kripto_adi.lower()]["usd"]
                try_fiyat = data[kripto_adi.lower()]["try"]
                tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"✅ {kripto_adi.capitalize()}: ${usd:,.2f} | ₺{try_fiyat:,.0f}")

                # Dosyaya yaz
                with open("kripto_gecmisi.txt", "a", encoding="utf-8") as f:
                    f.write(f"[{tarih}] {kripto_adi.capitalize()}: ${usd:,.2f} | ₺{try_fiyat:,.0f}\n")
            else:
                print(f"❌ '{kripto_adi}' bulunamadı.")
        else:
            print(f"⚠️ API hatası: {response.status_code}")
    except Exception as e:
        print(f"🚨 Hata: {e}")

# --- Ana Program ---
print("🪙 Dosyaya Kaydeden Kripto Takipçi")
while True:
    coin = input("Kripto adı (çıkmak için 'q'): ").strip()
    if coin.lower() == 'q':
        break
    if coin:
        kripto_fiyat_dosya(coin)