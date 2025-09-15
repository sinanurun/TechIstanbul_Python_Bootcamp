ogrenciler = {"ali","veli","can","kadir","kaan"}
print(ogrenciler)
print(ogrenciler.pop())
print(ogrenciler)
for ogrenci in ogrenciler:
    print(ogrenci)

if "can" in ogrenciler:
    ogrenciler.remove("can")
    print(ogrenciler)