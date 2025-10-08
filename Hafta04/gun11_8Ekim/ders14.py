import datetime
bugun = datetime.date.today()


print(bugun)
print(repr(bugun)) #tekrar nesne oluşturmaya uygun geliştirici için
print(str(bugun))# kullanıcı için açıklayıcı 
tarih = datetime.date(2018, 9, 2)
print(type(tarih))
print(tarih)

tarihs = eval(repr(bugun))
print(tarihs, type(tarihs))