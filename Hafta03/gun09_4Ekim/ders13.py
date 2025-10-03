import json

# Python verilerini JSON'a dönüştürme
kullanici = {
    "ad": "Ahmet",
    "yas": 25,
    "sehir": "İstanbul",
    "hobiler": ["spor", "müzik", "seyahat"],
    "aktif": True
}

# JSON string'e dönüştürme
json_string = json.dumps(kullanici, ensure_ascii=False, indent=2)
print("JSON String:")
print(json_string)

# JSON dosyasına yazma
with open("kullanici.json", "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya, ensure_ascii=False, indent=2)

# JSON dosyasını okuma
with open("kullanici.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)
    print("\nOkunan veri:")
    print(veri)

# JSON string'den Python verisine dönüştürme
json_verisi = '{"isim": "Ayşe", "yas": 30}'
python_verisi = json.loads(json_verisi)
print(f"\nPython verisi: {python_verisi}")