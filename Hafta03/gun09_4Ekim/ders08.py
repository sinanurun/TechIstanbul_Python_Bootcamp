import random
import os

bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = "oyun.txt"
dosya_adi = bulundugum_dizin + "/" + dosya_adi
if not (os.path.exists(dosya_adi)):
    dosya = open(dosya_adi, "x")
    dosya.close()

while True:
    cevap = int(input("oyun için 1,\tİstatistik için 2,\tÇıkış için 3"))
    if cevap == 1:
        dosya = open(dosya_adi, "a")
        rastgele = random.randrange(1,100)
        dosya.write(str(rastgele) + " + ")
        tahminSayisi = 10
        taban = 0
        tavan = 100
        while tahminSayisi >=1:
            tahmin = int(input("Bir Sayı Giriniz"))
            dosya.write(str(tahmin) + ",")
            if tahmin == rastgele:
                dosya.write("+ kazandınız \n")
                print("Tebrikler Kazandınız")
                dosya.close()
                break
            elif tahmin > rastgele:
                print("daha küçük bir değer giriniz")
                tavan = tahmin
            elif tahmin < rastgele:
                print("daha büyük bir sayı giriniz")
                taban = tahmin
            tahminSayisi -= 1
            print("kalan tahmin sayınız", tahminSayisi)
            if tahminSayisi == 0:
                dosya.write("Kaybettiniz \n")
                dosya.close()
    elif cevap == 2:
        dosya = open(dosya_adi)
        print(dosya.read())
        print(dosya.readlines())
        dosya.close()
    else: # elif cevap == 3:
        print("Sistemden Çıkış Yapıldı")
        break