sebze = ["pataes", "soğan"]
meyve = ["elma", "armut"]
sark = ["peynir", "bal"]
yesillik = ["maydanoz", "roka","semiz otu"]
# pazar_listesi = sebze+meyve+sark+yesillik
# print(pazar_listesi)
# print(len(pazar_listesi))
pazar_listesi = [sebze, meyve, sark, yesillik]
print(pazar_listesi)
pazar_listesi.append("baklava")
print(len(pazar_listesi))
print(pazar_listesi[0])
print(pazar_listesi[0][1])
print(pazar_listesi[0][0])
for kategori in pazar_listesi:
    print(kategori)
    if type(kategori) != list:
        continue
    for urun in kategori:
        print("\t",urun)
