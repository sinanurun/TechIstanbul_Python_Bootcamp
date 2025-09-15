# koşullu ifadeler if
# koşullu ifadeler belirli bir koşulun doğru veya yanlış olmasına göre farklı işlemler yapmamızı sağlar
# if koşul:
#     koşul doğru ise yapılacak işlemler
# if koşul yanlış ise işlemler yapılmaz
# koşul doğru veya yanlış olma durumu mantıksal veri tipidir True veya False
# karşılaştırma operatörleri ile koşul oluşturulur
# karşılaştırma operatörleri ==, !=, <, <=, >, >=   
# örnek uygulama    

ad = "veli"
ad = input("adınızı giriniz : ")

if ad=="melike" :
    print("adaşız")
    print("memnun oldum")

if ad != "melike":
    print("adın melike değil")
    print("yine de memnun oldum")