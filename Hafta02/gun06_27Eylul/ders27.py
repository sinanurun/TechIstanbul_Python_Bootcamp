# Sözlük + Fonksiyon: Sınıf Raporu
# Bir sınıftaki öğrencilerin notlarını ve ortalamalarını içeren bir rapor oluşturan fonksiyon
# Fonksiyon, her öğrencinin notlarını ve ortalamasını içeren bir sözlük return ile döndürecek
def sinif_raporu(sinif):
    rapor = {}
    
    for ogrenci in sinif:
        ad = ogrenci["ad"]
        notlar = ogrenci["notlar"]
        ortalama = sum(notlar) / len(notlar)
        
        rapor[ad] = {
            "notlar": notlar,
            "ortalama": ortalama,
            "durum": "Geçti" if ortalama >= 50 else "Kaldı"
        }
    
    return rapor

# Kullanım
sinif = [
    {"ad": "Ali", "notlar": [70, 80, 90]},
    {"ad": "Ayşe", "notlar": [45, 60, 55]},
    {"ad": "Mehmet", "notlar": [30, 40, 35]}
]

rapor = sinif_raporu(sinif)
for ogrenci, bilgi in rapor.items():
    print(f"{ogrenci}: {bilgi}")