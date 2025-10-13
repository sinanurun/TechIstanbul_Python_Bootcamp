import requests
import sqlite3
from datetime import datetime

# Veritabanı ve tablo oluşturma
def veritabani_hazirla():
    conn = sqlite3.connect("kripto_takip.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sorgular (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kripto_adi TEXT NOT NULL,
            usd_fiyat REAL NOT NULL,
            try_fiyat REAL NOT NULL,
            tarih TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def kripto_fiyat_db(kripto_adi):
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

                # Veritabanına kaydet
                conn = sqlite3.connect("kripto_takip.db")
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO sorgular (kripto_adi, usd_fiyat, try_fiyat, tarih)
                    VALUES (?, ?, ?, ?)
                """, (kripto_adi.lower(), usd, try_fiyat, tarih))
                conn.commit()
                conn.close()
            else:
                print(f"❌ '{kripto_adi}' bulunamadı.")
        else:
            print(f"⚠️ API hatası: {response.status_code}")
    except Exception as e:
        print(f"🚨 Hata: {e}")

# --- Başlangıç ---
veritabani_hazirla()
print("🪙 SQLite'li Kripto Takipçi")

while True:
    coin = input("Kripto adı (çıkmak için 'q'): ").strip()
    if coin.lower() == 'q':
        break
    if coin:
        kripto_fiyat_db(coin)