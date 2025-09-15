#tip dönüşümü casting
#veri tipleri arasında dönüşüm yapmak için kullanılır
#int() float() str() bool() 


#işlem için en önemli şey dönüştürülebilir olması verinin
sayi = 15
print(sayi*2, type(sayi))
sSayi = str(sayi)
print(sSayi*2, type(sSayi))
# tamIsım tam_isim tamisim firstName lastNAme last_name
s_ondalikli = "17.5"
ondalikli = float(s_ondalikli)
print(ondalikli*2, type(ondalikli))

smantik = "False"
mantiksal = bool(smantik)
print(mantiksal, type(mantiksal))

smantik = "fsdfsdf"
mantiksal = bool(smantik)
print(mantiksal, type(mantiksal))

smantik = str(mantiksal)
print(smantik, type(smantik))
