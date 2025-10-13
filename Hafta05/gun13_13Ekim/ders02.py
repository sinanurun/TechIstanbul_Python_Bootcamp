#json verisini işleme


import requests

# Kullanıcı verisi çekme (örnek bir JSON API)
url = "https://jsonplaceholder.typicode.com/users/1" 

response = requests.get(url)

if response.status_code == 200:
    # JSON verisini Python sözlüğüne dönüştür
    user_data = response.json() 
    
    # Sözlük üzerinden verilere eriş
    print(f"Kullanıcı Adı: {user_data['name']}") 
    print(f"E-posta: {user_data['email']}")
    
    # İç içe geçmiş verilere erişim (address bir sözlük)
    print(f"Şehir: {user_data['address']['city']}") 

else:
    print("Veri çekilemedi.")