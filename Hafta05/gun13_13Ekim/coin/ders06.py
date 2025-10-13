import requests

def kripto_fiyat(kripto_adi):
    # CoinGecko, kripto isimlerini küçük harf ve tire(-) ile kabul eder (örn: "ethereum", "binancecoin")
    # Ancak kullanıcı "Ethereum" veya "ETH" yazabilir → bu örnek sadece resmi isimleri destekler
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={kripto_adi.lower()}&vs_currencies=usd,try"
    
    try:
        response = requests.get(url, timeout=5)  # timeout ekledik
        if response.status_code == 200:
            data = response.json()
            # CoinGecko, geçersiz ID'lerde boş dict döner: {}
            if kripto_adi.lower() in data:
                usd = data[kripto_adi.lower()]["usd"]
                try_fiyat = data[kripto_adi.lower()]["try"]
                print(f"✅ {kripto_adi.capitalize()}: ${usd:,.2f} | ₺{try_fiyat:,.0f}")
            else:
                print(f"❌ '{kripto_adi}' bulunamadı. Lütfen doğru ismi girin (örn: bitcoin, ethereum).")
        else:
            print(f"⚠️ API hatası: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ İnternet bağlantınız yok veya API'ye ulaşılamıyor.")
    except requests.exceptions.Timeout:
        print("⏱️ İstek zaman aşımına uğradı.")
    except Exception as e:
        print(f"🚨 Beklenmeyen hata: {e}")

# --- Ana Program ---
print("🪙 Kripto Para Fiyat Takipçisine Hoşgeldiniz!")
print("Desteklenen örnekler: bitcoin, ethereum, cardano, solana, dogecoin\n")

while True:
    coin = input("Kripto para adı girin (çıkmak için 'q'): ").strip()
    if coin.lower() == 'q':
        print("Çıkış yapılıyor...")
        break
    if not coin:
        print("Lütfen bir değer girin.")
        continue
    kripto_fiyat(coin)