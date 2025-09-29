yas = int(input("Yaşınız: "))  # Kullanıcı "yirmi" yazarsa → HATA!

try:
    # Riskli kod buraya yazılır
    pass
except:
    # Hata olursa burası çalışır
    pass

try:
    yas = int(input("Yaşınız: "))
    print("Gelecek yıl", yas + 1, "yaşında olacaksınız.")
except:
    print("Lütfen geçerli bir sayı girin!")

"""
ValueError int("abc")  gibi geçersiz dönüşüm
IndexError liste[10] ama listede 5 eleman var
TypeError "merhaba" + 5 gibi uyumsuz işlem
KeyError sozluk["olmayan_anahtar"]
ZeroDivisionError 5 / 0 gibi sıfıra bölme
AttributeError nesne.yok_ozellik gibi var olmayan özellik erişimi
Exception tüm hataların üst sınıfı
NameError tanımlanmamış_değişken gibi tanımsız değişken erişimi

"""

try:
    sayi = int(input("Bir sayı gir: "))
except ValueError:
    print("Sayı yerine metin girdiniz!")


try:
    sayi = int(input("Sayı: "))
except ValueError:
    print("Hatalı giriş!")
else:
    print("Giriş başarılı:", sayi)


try:
    dosya = open("veri.txt")
    print(dosya.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    print("➡️ Program sonlanıyor...")
    # Burada dosya kapatılabilir


yas = int(input("Yaşınız: "))

if yas < 0 or yas > 150:
    raise ValueError("Yaş 0-150 arasında olmalı!")
else:
    print("Yaşınız:", yas)

"""
⚠️ raise → manuel olarak hata tetikler
try-except ile birlikte kullanılırsa daha güçlü olur: 
"""

try:
    yas = int(input("Yaşınız: "))
    if yas < 0 or yas > 150:
        raise ValueError("Geçersiz yaş aralığı!")
except ValueError as e:
    print("Hata:", e)  # e → hata mesajı