#Birden fazla ürünün bilgilerini saklamak istiyoruz.

urunler = [
    {"ad": "Laptop", "fiyat": 15000, "stok": 10},
    {"ad": "Mouse", "fiyat": 250, "stok": 50},
    {"ad": "Klavye", "fiyat": 800, "stok": 20}
]

for urun in urunler:
    print(f"{urun['ad']} - {urun['fiyat']} TL")