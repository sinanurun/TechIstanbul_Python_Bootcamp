#Bir sayının karesini 3 kez hesaplamak istiyoruz:

sayi = 5
print(sayi * sayi)

sayi = 8
print(sayi * sayi)

sayi = 12
print(sayi * sayi)


#Yukarıdaki işlemi fonksiyon kullanarak yapalım:
def kare_al(sayi):
    return sayi * sayi  
#fonksiyon tanımlama    
print(kare_al(5))
print(kare_al(8))
print(kare_al(12))
#fonksiyon çağırma

#Fonksiyonlar kodun tekrarını önler, kodu daha okunabilir ve yönetilebilir yapar.
#Ayrıca fonksiyonlar parametre alabilir ve değer döndürebilir.
#Fonksiyonlar programlamanın temel yapı taşlarındandır.
#Kendi fonksiyonlarımızı tanımlayabiliriz.
#Python'da birçok hazır fonksiyon vardır (print(), input(), len() gibi)
#Kendi fonksiyonlarımızı tanımlarken def anahtar kelimesi kullanılır.
#Fonksiyon isimleri anlamlı olmalıdır.
#Fonksiyon isimleri harf, rakam ve _ (alt çizgi) içerebilir, ancak rakamla başlayamaz.
#Fonksiyon isimleri küçük harflerle yazılır ve kelimeler _ ile ayrılır (snake_case).
#Fonksiyon tanımlandıktan sonra çağrılabilir.
#Fonksiyonlar parametre alabilir ve değer döndürebilir.
#Parametreler fonksiyonun içine veri aktarır.
#return ifadesi fonksiyondan değer döndürür ve fonksiyonun çalışmasını sonlandırır.
#Fonksiyonlar içinde başka fonksiyonlar çağrılabilir.
#Fonksiyonlar içinde değişkenler tanımlanabilir, bu değişkenler fonksiyonun dışından erişilemez (yerel değişkenler).
#Global değişkenler fonksiyonların içinde ve dışında erişilebilir.
#Fonksiyonlar programlamada kodun modülerliğini artırır.
#Fonksiyonlar hata ayıklamayı kolaylaştırır.
#Fonksiyonlar kodun tekrarını önler.
#Fonksiyonlar kodun okunabilirliğini artırır.
#Fonksiyonlar kodun yönetilebilirliğini artırır.
#Fonksiyonlar kodun test edilebilirliğini artırır.
#Fonksiyonlar kodun yeniden kullanılabilirliğini artırır.

