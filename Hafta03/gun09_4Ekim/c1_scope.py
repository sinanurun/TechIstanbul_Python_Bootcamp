# Scope, bir değişkenin, fonksiyonun veya nesnenin nerede tanımlandığı ve nerelerden erişilebildiği bilgisidir.
# Python’da her isim (değişken, fonksiyon, sınıf vb.) bir kapsam (scope) içinde yaşar.
# Bu kapsam, o ismin geçerli olduğu bölgeyi belirler.

# Python, isim araması yaparken LEGB kuralını takip eder:

# L Local Mevcut fonksiyon/metot içinde tanımlananlar
# E Enclosing İç içe fonksiyon varsa, dıştaki fonksiyonun scope’u
# G Global Modül (dosya) seviyesinde tanımlananlar
# B Built-in Python’un yerleşik isimleri (len,print,int, vs.)
#Python bir ismi ararken: Local → Enclosing → Global → Built-in sırasıyla bakar.

#local spoce

# def myfunc():
#   x = 300
#   print(x)

# myfunc()

#fonksiyonlar içinde scope
#bir fonksiyon içinde tanımlanan bir değişken alt fonksiyonlar tarafından da erişilebilir
#alt fonksiyon değişiklik yapamaz

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
# #    x = 55
#   myinnerfunc()

# myfunc()


#global scope
#global değişkenler ana kod alanında tanımlanır ve heryerden erişilebilir

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

#global ve yerel local değişkenler
# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)

#global keyword ile global değişkenlere erişim ve değişiklikler yapma

# x = 500

# def myfunc():
#   global x
#   x = 300

# print(x)
# myfunc()

# print(x)

#nonlocal keyword ile içerdeki fonksiyon versine dışardan erişim sağlama

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   print(x)
#   myfunc2()
#   print(x)
#   return x
# #print(x)
# print(myfunc1())
# #print(x)