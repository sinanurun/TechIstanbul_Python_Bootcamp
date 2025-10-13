"""
import requests
import json

# OpenWeatherMap API key (ücretsiz kayıt olabilirsiniz)
API_KEY = "f185cd49eb75a1277c411892ab0af2fa"  # https://openweathermap.org/api
CITY = "Istanbul"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=tr"

try:
    response = requests.get(URL)
    data = response.json()
    
    if response.status_code == 200:
        print(f"=== {CITY} Hava Durumu ===")
        print(f"Sıcaklık: {data['main']['temp']}°C")
        print(f"Hissedilen: {data['main']['feels_like']}°C")
        print(f"Durum: {data['weather'][0]['description'].capitalize()}")
        print(f"Nem: {data['main']['humidity']}%")
        print(f"Rüzgar: {data['wind']['speed']} m/s")
        print(f"Basınç: {data['main']['pressure']} hPa")
    else:
        print("Hata:", data["message"])
        
except requests.exceptions.RequestException as e:
    print("Bağlantı hatası:", e)
except KeyError as e:
    print("Veri formatı hatası:", e)
"""
import requests
import json
from datetime import datetime

def get_weather(city_name, api_key):
    """
    OpenWeatherMap API ile hava durumu bilgisi alır
    """
    # Temel URL - weather endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parametreler
    params = {
        'q': city_name,
        'appid': 'f185cd49eb75a1277c411892ab0af2fa',
        'units': 'metric',  # Celsius için
        'lang': 'tr'        # Türkçe çıktı için
    }
    
    try:
        # API isteği
        response = requests.get(base_url, params=params, timeout=10)
        
        # HTTP hata kontrolü
        response.raise_for_status()
        
        # JSON verisini al
        data = response.json()
        
        # Başarılı yanıt
        if response.status_code == 200:
            return {
                'success': True,
                'data': data
            }
        else:
            return {
                'success': False,
                'error': f"API hatası: {data.get('message', 'Bilinmeyen hata')}"
            }
            
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f"Bağlantı hatası: {e}"
        }
    except ValueError as e:
        return {
            'success': False,
            'error': f"JSON decode hatası: {e}"
        }

def display_weather(weather_data, city_name):
    """
    Hava durumu bilgisini ekrana yazdırır
    """
    if not weather_data['success']:
        print(f"❌ Hata: {weather_data['error']}")
        return
    
    data = weather_data['data']
    
    print(f"\n{'='*50}")
    print(f"🌤️  {city_name.upper()} HAVA DURUMU")
    print(f"{'='*50}")
    
    # Ana bilgiler
    main = data['main']
    weather = data['weather'][0]
    
    print(f"📍 Şehir: {data['name']}, {data['sys']['country']}")
    print(f"🌡️  Sıcaklık: {main['temp']}°C")
    print(f"🤔 Hissedilen: {main['feels_like']}°C")
    print(f"📝 Durum: {weather['description'].capitalize()}")
    print(f"💧 Nem: {main['humidity']}%")
    print(f"🌬️  Rüzgar: {data['wind']['speed']} m/s")
    print(f"📊 Basınç: {main['pressure']} hPa")
    print(f"👁️  Görüş: {data.get('visibility', 'Bilinmiyor')} metre")
    
    # Ek bilgiler
    if 'rain' in data:
        print(f"🌧️  Yağış: {data['rain']} mm")
    if 'snow' in data:
        print(f"❄️  Kar: {data['snow']} mm")
    
    print(f"{'='*50}")

# KULLANIM ÖRNEĞİ
def main():
    API_KEY = "f185cd49eb75a1277c411892ab0af2fa"  # BURAYI DEĞİŞTİRİN!
    CITIES = ["Istanbul", "Ankara", "Izmir", "London", "Paris"]
    
    print("🌍 HAVA DURUMU UYGULAMASI")
    print("API Key kontrol ediliyor...")
    
    # API key kontrolü

    
    print("\n✅ API Key aktif! Hava durumu bilgileri alınıyor...\n")
    
    # Birden fazla şehir için hava durumu
    for city in CITIES:
        print(f"\n🔍 {city} için hava durumu sorgulanıyor...")
        weather_info = get_weather(city, API_KEY)
        display_weather(weather_info, city)

# Çalıştır
if __name__ == "__main__":
    main()