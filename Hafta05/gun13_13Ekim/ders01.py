"""
1. API Nedir, Neden Kullanılır? 
API (Application Programming Interface - Uygulama Programlama Arayüzü): İki farklı yazılımın birbirleriyle konuşmasını sağlayan aracıdır.

Basit Benzetme: API'yi bir restorandaki garson gibi düşünebiliriz. 
Siz (istemci) mutfaktan (sunucudan) istediğiniz yemeği (veriyi) garson (API) aracılığıyla sipariş edersiniz. 
Garson siparişi mutfağa iletir ve size yanıtı (yemeği) geri getirir.
Gerçek hayattan örnek: Restoran menüsü → sipariş ver (request) → mutfak hazırlar → servis gelir (response).


Neden Kullanılır?

Veri Alışverişi: Bir uygulamanın, başka bir uygulamanın verisine güvenli ve kontrollü bir şekilde erişmesini sağlar (Örn: Twitter verileri, hava durumu, döviz kurları).

İşlevsellik Paylaşımı: Başka bir servisin fonksiyonlarını kendi uygulamamızda kullanmamızı sağlar (Örn: Ödeme sistemleri, harita hizmetleri).
"""

"""

1. API Nedir, Neden Kullanılır? 
API (Application Programming Interface - Uygulama Programlama Arayüzü): İki farklı yazılımın birbirleriyle konuşmasını sağlayan aracıdır.

Basit Benzetme: API'yi bir restorandaki garson gibi düşünebiliriz. Siz (istemci) mutfaktan (sunucudan) istediğiniz yemeği (veriyi) garson (API) aracılığıyla sipariş edersiniz. Garson siparişi mutfağa iletir ve size yanıtı (yemeği) geri getirir.

Neden Kullanılır?

Veri Alışverişi: Bir uygulamanın, başka bir uygulamanın verisine güvenli ve kontrollü bir şekilde erişmesini sağlar (Örn: Twitter verileri, hava durumu, döviz kurları).

İşlevsellik Paylaşımı: Başka bir servisin fonksiyonlarını kendi uygulamamızda kullanmamızı sağlar (Örn: Ödeme sistemleri, harita hizmetleri).


API (Application Programming Interface): Uygulamaların birbiriyle konuşmasını sağlayan arayüz

REST API: HTTP protokolü üzerinden çalışan, JSON/XML formatında veri dönen API yapısı

HTTP Metodları: GET (veri al), POST (veri gönder), PUT (güncelle), DELETE (sil)

"""

"""
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/2")

print(response)

print(response.status_code)  # 200 → başarılı

# .status_code: 200 = OK, 404 = Not Found, 500 = Server Error

print(response.text) #gelen vernin text hali

print(response.json())       # JSON verisini dict olarak al
#data_json = response.json()

#for data in data_json:
#    print(f"{data}:\t{data_json[data]}")

"""


import requests

# İstek atılacak URL
url = "https://api.github.com" 

# GET isteği gönder
response = requests.get(url)

# Gelen yanıtın durum kodunu yazdır
print(f"Durum Kodu: {response.status_code}") 

# Durum Kodu Kontrolü: 200 başarılı demektir.
if response.status_code == 200:
    print("İstek Başarılı!")
else:
    print("İstek Başarısız. Hata kodu:", response.status_code)


