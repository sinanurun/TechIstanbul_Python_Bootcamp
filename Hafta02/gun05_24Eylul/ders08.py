yemekler = {"Çorbalar":{"etli":["işkembe","kelle paça","tavuk suyu"],
                        "bakliyatli":["mercimek","ezoegelin"],
                        "sebzeli":["domates","brokoli"]},
            "Kebaplar":{"acılı":["adana","beyti"],
                        "acısız":["urfa","mardin"],
                        "dürümler":["ciger","adana"]},
            "icecekler":["çay","kahve"]
        }
# print(yemekler["Çorbalar"]["etli"])
yemekler["Çorbalar"]["etli"].append("Bayram Çorbası")
# print(yemekler["Çorbalar"]["etli"])
yemekler["Çorbalar"]["etli"]={"dana":["ayakpaça"],
                              "kuzu":["tirit"]}
serbetli_tatli = ["Baklava"]
yemekler["tatlilar"]= {"şerbetlitatlilar":serbetli_tatli}
# print(yemekler)
yemekler["tatlilar"]["sütlütatlılar"]=["puding"]
# print(yemekler)
serbetli_tatli.append("şeker pare")
# print(yemekler)
for anakategori in yemekler:
    print(anakategori)
    if type(yemekler[anakategori]) is dict:
        for altkategori in yemekler[anakategori]:
            print("\t",altkategori)
            if type(yemekler[anakategori][altkategori]) is dict:
                for altkategori2 in yemekler[anakategori][altkategori]:
                    print("\t\t",altkategori2)
                    for altkategori3 in yemekler[anakategori][altkategori][altkategori2]:
                        print("\t\t\t",altkategori3)
            else:
                print("\t\t",yemekler[anakategori][altkategori])
    else:
        print("\t",yemekler[anakategori])