import json
kitap_listesi = []
kitaplar = []
class Kitap():
    def __init__(self,ad,yazar,sayfa,basim):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa
        self.basim=basim
    def __str__(self):
        return self.ad

def kitapListesineEkle():
    kitap_adi = input("Kitap adı")
    kitap_yazar = input("yazar")
    kitap_sayfa = int(input("sayfa"))
    kitap_yili = int(input("yili"))
    kitap = Kitap(kitap_adi,kitap_yazar, kitap_sayfa, kitap_yili)
    degerler = vars(kitap)
    kitap_listesi.append(degerler)
    kitaplar.append(kitap)

def kitapListesiKaydet():
    try:
        with open("kitap.json","r") as file:
            kitap_listesi2 = list(json.loads(file.read()))
    except:
        kitap_listesi2 = []
    if len(kitap_listesi2) == 0:
        if len(kitap_listesi) > 0:
            y = json.dumps(kitap_listesi)
            with open("kitap.json","w") as file:
                file.write(y)
            kitap_listesi.clear()
            kitaplar.clear()
        else:
            print("Kaydedilecek Kitap Yok")
    else:
        if len(kitap_listesi) > 0:
            kitap_listesi2.extend(kitap_listesi)
            y = json.dumps(kitap_listesi2)
            with open("kitap.json","w") as file:
                file.write(y)
            kitap_listesi.clear()
            kitaplar.clear()
            del kitap_listesi2
        else:
            print("Kaydetmeyi Bekleyen Kitap Yok")

def kitapListele():
    if len(kitaplar)>0:
        for kitap in kitaplar:
            print(kitap)
    else:
        print("Kaydedilmeyi bekleyen kitap yok")

def kayitlikitapListele():
    try:
        with open("kitap.json", "r") as file:
            kitap_listesi2 = list(json.loads(file.read()))
    except:
        kitap_listesi2 = []
    if len(kitap_listesi2)>0:
        for kitap_bilgisi in kitap_listesi2:
            kitap_adi = kitap_bilgisi["ad"]
            kitap_yazar = kitap_bilgisi["yazar"]
            kitap_sayfa = kitap_bilgisi["sayfa"]
            kitap_yili = kitap_bilgisi["basim"]
            kitap = Kitap(kitap_adi, kitap_yazar, kitap_sayfa, kitap_yili)
            kitaplar.append(kitap)
        for kitap in kitaplar:
            print(kitap)
        kitaplar.clear()
    else:
        print("Kayıtlı kitap yok")
def menu():
    k_giris = input("Kaydet, Ekle, Çıkart, Listele, Dosya listele, Q")
    return k_giris
while True:
    cevap = menu()
    if cevap == "e":
        kitapListesineEkle()
    elif cevap == "k":
        kitapListesiKaydet()
    elif cevap == "q":
        print("programdan çıkıldı")
        exit()
    elif cevap == "l":
        kitapListele()
    elif cevap == "d":
        kayitlikitapListele()
    else:
        print("hatalı işlem girişi")

# kitap = Kitap("Python","Sinan Hoca",30, 2024)
#
# kitap_ekleme = kitapekle(kitap)
# if kitap_ekleme:
#     print("Kitap Ekleme Başarılı")
# else:
#     print("Kitap ekleme Başarısız")