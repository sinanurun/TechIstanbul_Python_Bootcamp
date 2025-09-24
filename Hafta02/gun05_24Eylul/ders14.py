okul = {
    "9A": [
        {"ad": "Ali", "numara": "101"},
        {"ad": "Ayşe", "numara": "102"}
    ],
    "10B": [
        {"ad": "Mehmet", "numara": "201"},
        {"ad": "Zeynep", "numara": "202"}
    ]
}

# Sınıfları ve öğrencileri listele
for sinif, ogrenci_listesi in okul.items():
    print(f"\n{sinif} Sınıfı:")
    for ogrenci in ogrenci_listesi:
        print(f"  - {ogrenci['ad']} (No: {ogrenci['numara']})")