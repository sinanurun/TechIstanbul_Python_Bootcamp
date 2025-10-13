#normal fonksiyonlar ile yazım

# def kare_al(liste):
#     liste2 = []
#     for eleman in liste:
#         liste2.append(eleman**2)
#     return liste2
#
# print(kare_al([1,2,3,4]))

# def ikiye_katla(katlanacaklar):
#     katlanmis=[]
#     for a in katlanacaklar:
#         katlanmis.append(a*2)
#     return katlanmis
# gonderilecek=[2,5,8,96]
# print(ikiye_katla(gonderilecek))

# map fonksiyonu kullanarak yapalım
# liste = [1,2,3,4]
# print(list(map(lambda x:x**2,liste)))

#iterasyonlu işlemler 1
# a = [2,4,6,8]
# b = [3,6,9,12]
# print(list(map(lambda x,y:x*y,a,b)))

# iterasyonlu işlemler 2
puanlama = [("ali",55),("veli",80),("can",95),("kamil",45)]
degerlendirme = lambda dizi:(dizi[0],"geçti" if dizi[1]>70 else "kaldı")
print(list(map(degerlendirme,puanlama)))
