ogrenci = {
    "isim": "Zeynep",
    "yas": 22,
    "bolum": "Bilgisayar"
}
print(ogrenci, type(ogrenci))
print(ogrenci["isim"])
print(ogrenci.get("yas"))   #aynı işi yapar
print(ogrenci.keys())
print(ogrenci.values())
print(ogrenci.items())

ogrenci["fakulte"] = "mühendislik"
print(ogrenci)