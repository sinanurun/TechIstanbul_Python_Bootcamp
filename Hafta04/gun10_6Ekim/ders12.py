class Otomobil():
    teker = 4
    kapi = True
    def __init__(self,marka,model,renk):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.CalismaDurum = False

    def calistir(self):
        if self.CalismaDurum == False:
            self.CalismaDurum = True
            print(f"{self.marka} araba çalıştırıldı")
            self.hiz = 0
        else:
            print(f" {self.marka} Araba Zaten Çalışıyor")

    def durdur(self):
        if self.CalismaDurum == True:
            self.CalismaDurum = False
            print(f"{self.marka} araba durduruldu")
            self.hiz = 0
        else:
            print(f" {self.marka} Araba Zaten Duruyor")

    def hizArttir(self):
        if self.CalismaDurum == True:
            self.hiz += 10
        else:
            print(f" {self.marka} önce aracı çalıştırın")
        return self.hizGoster()

    def hizAzalt(self):
        if self.CalismaDurum == True and self.hiz > 0:
            self.hiz -=10
        elif self.hiz == 0:
            print(f" {self.marka} araç çalışıyor ama zaten duruyor")
        else:
            print(f" {self.marka} araba zaten çalışmıyor")
        return self.hizGoster()

    def hizGoster(self):
        if self.CalismaDurum == False:
            self.hiz = 0
        print(f" {self.marka} aracın hızı {self.hiz}")
        return self.hiz

    def cikis(self):
        print("Çıkış yapıldı")
        exit()

    def __str__(self):
        return f'{self.marka}, {self.model} Otomobil'


oto1 = Otomobil("Ford","Focus","Gri")
# oto1.calistir()
# oto1.calistir()
# print(oto1)
# oto2 = Otomobil("Audi","A4","Kırmızı")
# print(oto2)
# print(oto2.CalismaDurum)
# oto2.calistir()
# oto2.hizArttir()
# oto2.hizGoster()
# oto2.hizArttir()

while True:
    cevap = int(input("Çalıştır : 1 \t Durdur: 2\n, arttır: 3\t, Azatl : 4\n Hız Göster : 5\t, Çıkış 6 \n"))
    if cevap == 1:
        oto1.calistir()
    elif cevap == 2:
        oto1.durdur()
    elif cevap == 3:
        oto1.hizArttir()
    elif cevap == 4:
        oto1.hizAzalt()
    elif cevap == 5:
        oto1.hizGoster()
    elif cevap == 6:
        oto1.cikis()
    else:
        print("hatalı işlem girişi")