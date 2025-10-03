# dosya oluşturma ve içine veri yazma
metin = "\nçok faydalı bir kurs oluyor bizler icin"
dosya = open("deneme.txt","a")
dosya.write(metin)
dosya.close()

#dosya açıp yazma
with open("deneme.txt", "a") as f: #a yerine w olursa içeriği silinir öyle eklenir
  f.write("içerik eklendi")

#içeriğine veri eklenen dosyayı açıp okuma
with open("deneme.txt") as f:
  print(f.read())