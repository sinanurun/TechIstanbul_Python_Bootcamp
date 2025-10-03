isim = "Ali"
yas = 25
# Bu bilgiyi bir dosyaya yazalım ki, sonra da okuyabilelim

"""
 Üç temel dosya formatı: 

.txt → düz metin
.csv → virgülle ayrılmış değerler (Excel benzeri)
.json → yapılandırılmış veri (web, API’lerde çok kullanılır)
"""

# 
dosya = open("merhaba.txt", "w")  # yazma modu
dosya.write("Merhaba Dünya!")
dosya.close()