puan = int(input("ortalama puanınızı giriniz"))
if puan < 0:
    print("0 dan küçük puan girişi yaptınız hatalı")
elif puan < 70: # else + if => elif
    print("belge için yeterli puanınız yok")
elif puan < 85:
    print("teşekkür belgesi aldınız tebrikler")
elif puan <=100:
    print("takdir alabilirsiniz tebrikler")
else:
    print("geçerli puan girişi sağlanamadı")