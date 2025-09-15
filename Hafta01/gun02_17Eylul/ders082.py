sinif = int(input("sınıf seviyesini yazınız"))
if sinif <1:
    print("sınıf 1den az olamaz")
elif sinif <=4:
    print("ilkokul öğrencisi")
elif sinif <= 8: # else + if => elif
    print("ortaokul öğrencisi")
elif sinif <= 12:
    print("lise öğrencisi")
else:
    print("geçerli sınıf seviyesi girilmedi")
    print("sınıf 12den büyük olamaz")
