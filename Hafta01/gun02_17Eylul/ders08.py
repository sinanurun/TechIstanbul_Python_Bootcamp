puan = int(input("ortalama puanınızı giriniz"))
if puan < 0:
    print("0 dan küçük puan girişi yaptınız hatalı")
else:
    if puan < 70:
        print("belge için yeterli puanınız yok")
    else:
        if puan < 85:
            print("teşekkür belgesi aldınız tebrikler")
        else:
            if puan <=100:
                print("takdir alabilirsiniz tebrikler")
            else:
                print("geçerli puan girişi sağlanamadı")