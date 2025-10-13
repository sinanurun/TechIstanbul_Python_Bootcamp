import requests

def kripto_fiyat(kripto_adi):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={kripto_adi}&vs_currencies=usd,try"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if kripto_adi in data:
                usd = data[kripto_adi]["usd"]
                try_fiyat = data[kripto_adi]["try"]
                print(f"{kripto_adi.capitalize()}: ${usd} | ₺{try_fiyat:,.0f}")
            else:
                print("Kripto para bulunamadı. İsim doğru mu?")
        else:
            print("API hatası:", response.status_code)
    except Exception as e:
        print("Bağlantı hatası:", e)