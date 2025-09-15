3#tip dönüşümü casting ve input
#input() fonksiyonu kullanıcıdan veri almak için kullanılır
#input() fonksiyonu her zaman string veri tipi döndürür
#kullanıcıdan alınan veriyi istediğimiz veri tipine dönüştürmemiz gerekir
#int() float() str() bool()

print("adın nedir?")
ad = input()
print("memnun oldum", ad)
print(type(ad))
print("yaşın kaç",ad)
yas = int(input())
print("yasın", yas)