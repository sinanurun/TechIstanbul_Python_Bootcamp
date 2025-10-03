# CSV (Comma Separated Values), veri depolamak için yaygın kullanılan bir formattır.
#Excel, Google Sheets verileri genellikle .csv formatındadır.

import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "ogrenciler.csv"

with open(dosya_adi, "w") as f:
    f.write("isim,yas,bolum\n")
    f.write("Ali,22,Bilgisayar\n")
    f.write("Ayşe,21,Edebiyat\n")

with open(dosya_adi, "r") as f:
    for satir in f:
        print(satir.strip())  # boşlukları temizle

