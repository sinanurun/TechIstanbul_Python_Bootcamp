#Web siteleri, mobil uygulamalar veriyi genellikle JSON formatında taşır.
import json

ogrenci = {
    "isim": "Zeynep",
    "yas": 23,
    "bolum": "Matematik"
}

with open("ogrenci.json", "w") as f:
    json.dump(ogrenci, f, indent=4)  # güzel format

with open("ogrenci.json", "r") as f:
    veri = json.load(f)
    print(veri["isim"])  # Zeynep

"""
json.load() → dosyadan okur
json.loads() → string’den okur
json.dump() → dosyaya yazar
json.dumps() → string’e çevirir 
"""