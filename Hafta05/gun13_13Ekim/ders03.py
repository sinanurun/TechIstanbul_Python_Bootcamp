"""
API'den hatalı yanıt gelmesi ihtimaline karşı try-except bloğu kullanmak profesyonel bir yaklaşımdır. 
Ayrıca, json modülünü kullanarak elle JSON işleme de yapılabilir, ancak requests kütüphanesi bunu bizim için halleder.

"""

import requests
import json

url = "https://jsonplaceholder.typicode.com/invalid-url" # Hata verecek bir URL

try:
    response = requests.get(url, timeout=5) # 5 saniye bekleme süresi (timeout)
    response.raise_for_status() # HTTP hata kodu varsa (4xx veya 5xx) istisna fırlat
    
    data = response.json()
    print("Veri başarıyla çekildi.")
    
except requests.exceptions.HTTPError as err_http:
    print(f"HTTP Hatası: {err_http}") # 404 Not Found gibi
except requests.exceptions.ConnectionError as err_conn:
    print(f"Bağlantı Hatası: {err_conn}") # İnternet bağlantısı yoksa
except requests.exceptions.Timeout as err_timeout:
    print(f"Zaman Aşımı Hatası: {err_timeout}")
except requests.exceptions.RequestException as err:
    print(f"Genel Hata: {err}")
except json.JSONDecodeError:
    print("Yanıt geçerli bir JSON formatında değil.") # Yanıt JSON değilse