# adet = int(input("kaç tane zerzevat alacaksın"))
# zerzevat = []
# for i in range(adet):
#     print(i+1,". ne alacaksın")
#     urun = input("urun: ")
#     zerzevat.append(urun)
#
# for urun in zerzevat:
#     print(urun)

#versiyon 2 pazar listesi
mesaj = """Pazar Listesi Oluşturma Programına Hoşgeldiniz
Programdan Çıkmak için X'e basınız"""
print(mesaj)
zerzevat = []
while True:
    urun = input("Ürün girişi yapınız")
    if urun.lower() == "x":
        print("pazar listeniz", zerzevat)
        break
    elif urun == "":
        continue
    else:
        zerzevat.append(urun)