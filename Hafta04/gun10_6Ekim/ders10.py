#decorator kavramı ve kullanımı
"""
Dekoratör Nedir?

Dekoratörler Python’da başka bir fonksiyonu sarmalayıp davranışını değiştiren fonksiyonlardır.

Yani bir fonksiyonun “önüne” veya “arkasına” ek özellik ekler.
"""

#dekorator olmadan
# def selamla():
#     print("Merhaba!")

# selamla()


#örnek01
#genel dekorator yapısı
# def dekorator(fonksiyon): #dokatörler bir fonksiyonu parametre olarak alır
#     def sarmal():
#         print("Fonksiyon çağrılmadan önce")
#         fonksiyon()
#         print("Fonksiyon çağrıldıktan sonra")
#     return sarmal

# @dekorator
# def selamla():
#     print("Merhaba")

# selamla()

#ornek02
# def log(fonksiyon):
#     def sarmal():
#         print("Log: Fonksiyon çalışıyor...")
#         fonksiyon()
#         print("Log: Fonksiyon bitti.")
#     return sarmal

# @log
# def selamla():
#     print("Merhaba!")

# selamla()

# @log ifadesi aslında şunu yaptı:

# selamla = log(selamla)

# Yani selamla() çağrıldığında aslında log() içindeki sarmal() çalıştı.

#decorator kullanımı farklı örnek
# def changecase(func):
#   def myinner():
#     # print(func().lower())
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Merhaba Dünya"

# @changecase
# def otherfunction():
#   return "Python Kursu"

# print(myfunction())
# print(otherfunction())


# Parametre Alan Fonksiyonlarla Kullanımı

# Eğer dekoratör uygulanacak fonksiyon parametre alıyorsa, sarmal fonksiyonunun da bu parametreleri alması gerekir.

# def log(fonksiyon):
#     def sarmal(*args, **kwargs): #*args, **kwargs sayesinde, kaç parametre olursa olsun çalışabiliyor.
#         print(f"{fonksiyon.__name__} fonksiyonu çağrılıyor...")
#         sonuc = fonksiyon(*args, **kwargs)
#         print(f"{fonksiyon.__name__} fonksiyonu bitti.")
#         return sonuc
#     return sarmal

# @log
# def topla(a, b):
#     print(f"Toplam: {a + b}")
#     return a + b

# topla(3, 4)

#arguman alan decorator tanımlama ve kullanma

# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())



#birden fazla decorator kullanmak
# Python dekoratörleri yukarıdan aşağıya okur
# ama uygulamayı alttan yukarıya doğru yapar.
# def birinci(f):
#     def sarmal():
#         print("Birinci dekoratör çalıştı")
#         f()
#     return sarmal

# def ikinci(f):
#     def sarmal():
#         print("İkinci dekoratör çalıştı")
#         f()
#     return sarmal

# @birinci
# @ikinci
# def mesaj():
#     print("Merhaba!")

# mesaj()
"""
| Aşama                       | Yön             | Açıklama                                            |
| --------------------------- | --------------- | --------------------------------------------------- |
| **Okuma**                   | Yukarıdan aşağı | Python kodu sırayla okur.                           |
| **Uygulama (sarma işlemi)** | Alttan yukarı   | Alt dekoratör önce uygulanır.                       |
| **Çalıştırma sırası**       | Yukarıdan aşağı | En dıştaki (üstteki) dekoratörün kodu önce çalışır. |

"""
#ornek 2
# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# def addgreeting(func):
#   def myinner():
#     return "Hello " + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreeting
# def myfunction():
#   return "Tobias"

# print(myfunction())

# Artık sınıflardaki @classmethod, @staticmethod, @property gibi şeylerin mantığı 
# çok daha açık olacak çünkü onlar da birer özel dekoratördür.

# class Ornek:
#     def normal(self):
#         print("Normal metod")

#     @classmethod
#     def sinif_metodu(cls):
#         print("Class method çalıştı")

#     @staticmethod
#     def statik_metod():
#         print("Static method çalıştı")

# class Ornek:
#     def normal(self):
#         print("Normal metod")

#     def sinif_metodu(cls):
#         print("Class method çalıştı")
#     sinif_metodu = classmethod(sinif_metodu)

#     def statik_metod():
#         print("Static method çalıştı")
#     statik_metod = staticmethod(statik_metod)
# #Yani @classmethod ve @staticmethod sadece Python’un bizim yerimize yaptığı kısa yazım.
"""
| Terim               | Açıklama                                               | Örnek                                 |
| ------------------- | ------------------------------------------------------ | ------------------------------------- |
| Dekoratör           | Başka bir fonksiyonu sarmalayıp davranışını değiştirir | `@log`, `@timeit`, `@classmethod`     |
| `@` işareti         | Fonksiyonu dekoratörle ilişkilendirir                  | `@log`                                |
| `*args, **kwargs`   | Tüm parametreleri alabilmek için kullanılır            | `def sarmal(*args, **kwargs):`        |
| Sınıf dekoratörleri | `@classmethod`, `@staticmethod`, `@property`           | Python’un yerleşik özel dekoratörleri |

"""

# import functools

# def changecase(func):
#     @functools.wraps(func)  # fonksiyon ismi ve dokümantasyonun korunmasını sağlar #kullanmadan da deneme
#     def myinner():
#         return func().upper()  # orijinal fonksiyonun çıktısını büyük harfe çevirir
#     return myinner

# @changecase
# def myfunction():
#     return "Have a great day!"

# print(myfunction())       # Fonksiyon çıktısı
# print(myfunction.__name__)  # Fonksiyon ismi

"""
Mantık Açıklaması

*changecase → dekoratör fonksiyon

İçine başka bir fonksiyon alır (func)

myinner adında sarmal bir fonksiyon döndürür.

*@functools.wraps(func)

Normalde dekoratör fonksiyonlar, orijinal fonksiyonun adını (__name__) ve dokümantasyonunu (__doc__) değiştirir.

wraps bunu korumamıza yarar.

*myinner fonksiyonu:

Orijinal fonksiyonu çağırır: func()

Çıktısını .upper() ile büyük harfe çevirir

Sonra bunu geri döndürür.

*@changecase → myfunction = changecase(myfunction)

Artık myfunction() çağrıldığında, içindeki myinner() çalışır.
"""

"""
Dekoratör = fonksiyonu sarmalayan ve davranışını değiştiren fonksiyon.

functools.wraps = dekoratör uygulanmış fonksiyonun isim ve dokümantasyonunu korur.

@changecase = kısaca myfunction = changecase(myfunction) demektir.
"""