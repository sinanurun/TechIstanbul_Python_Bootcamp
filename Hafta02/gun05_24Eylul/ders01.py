ogrenci = ["Ali", 22, "Bilgisayar Müh.", 85]

ogrenci = {
    "isim": "Ali",
    "yas": 22,
    "bolum": "Bilgisayar Müh.",
    "not": 85
}

araba = {
    "marka": "Toyota",
    "model": "Corolla",
    "yil": 2020,
    "renk": "gri"
}

print(araba["marka"])  # Toyota
print(araba["yil"])     # 2020

araba["yil"] = 2022          # güncelle
araba["kilometre"] = 45000   # yeni ekle

del araba["renk"]