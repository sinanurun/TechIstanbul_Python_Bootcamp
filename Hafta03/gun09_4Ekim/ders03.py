dosya_Adi = "deneme.txt"
# with open(dosya_Adi) as dosya:
#     print(dosya.readline())

#satır satır okuma
with open("deneme.txt") as f:
  print(f.readline())
  print(f.readline())

#satır satır okuma for döngülü
with open("deneme.txt") as f:
  for x in f:
    print(x)

dosya = open(dosya_Adi)
metin = dosya.read()
print(metin)
satirlar = metin.split("\n")
print(satirlar)

