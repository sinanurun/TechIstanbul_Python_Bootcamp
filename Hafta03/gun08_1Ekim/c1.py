#python da modüller import edilirken import anahtar kelimesi kullanılır.
#modül isimleri küçük harflerle yazılır.
import math
import random
import datetime
import os
import sys
import time
import json

#en çok kullanılan modüllerden bazıları:
#math modülü matematiksel işlemler için kullanılır. 
print("=== MATH MODÜLÜ ===")
print("Pi sayısı:", math.pi)
print("2'nin üssü 3:", math.pow(2, 3))
print("Karekök 16:", math.sqrt(16)) 
print("Mutlak değer -5:", abs(-5))
print("Yuvarlama 4.7:", round(4.7))
print("Yuvarlama 4.4:", round(4.4))
print("En yakın tam sayı 4.5:", round(4.5))
print("En yakın tam sayı 4.6:", round(4.6))
print("En yakın tam sayı 4.4:", round(4.4))

#random modülü rastgele sayılar üretmek için kullanılır.
print("\n=== RANDOM MODÜLÜ ===")    
print("0-1 arası rastgele sayı:", random.random())
print("1-10 arası rastgele sayı:", random.randint(1, 10))
print("1-100 arası rastgele sayı:", random.randint(1, 100))
print("1-5 arasında rastgele ondalıklı sayı türetme", random.uniform(1.0, 5.0))

renkler = ["kırmızı", "mavi", "yeşil"]
secilen = random.choice(renkler)
print("Seçilen renk:", secilen)

isimler = ["Ali", "Ayşe", "Mehmet"]
random.shuffle(isimler)
print(isimler)  # ['Mehmet', 'Ali', 'Ayşe']


#datetime modülü tarih ve saat işlemleri için kullanılır.
print("\n=== DATETIME MODÜLÜ ===")
simdi = datetime.datetime.now()
print("Şimdi:", simdi)
print("Yıl:", simdi.year)
print("Ay:", simdi.month)
print("Gün:", simdi.day)    
print("Saat:", simdi.hour)
print("Dakika:", simdi.minute)
print("Saniye:", simdi.second)
print("Mikrosaniye:", simdi.microsecond)
print("Haftanın günü (0-6):", simdi.weekday())  
print("Haftanın günü adı:", simdi.strftime("%A"))
print("Ay adı:", simdi.strftime("%B"))
print("Tarih formatı:", simdi.strftime("%d/%m/%Y")) 
print("Saat formatı:", simdi.strftime("%H:%M:%S"))
print("Tarih ve saat formatı:", simdi.strftime("%d/%m/%Y %H:%M:%S"))
print("ISO formatı:", simdi.isoformat())
print("Zaman damgası:", simdi.timestamp())
print("Yılın günü:", simdi.timetuple().tm_yday))
print("Haftanın günü (1-7):", simdi.isoweekday())
print("Haftanın günü adı (İngilizce):", simdi.strftime("%A"))
print("Ay adı (İngilizce):", simdi.strftime("%B"))
print("Haftanın günü adı (Türkçe):", simdi.strftime("%A").replace("Monday", "Pazartesi").replace("Tuesday", "Salı").replace("Wednesday", "Çarşamba").replace("Thursday", "Perşembe").replace("Friday", "Cuma").replace("Saturday", "Cumartesi").replace("Sunday", "Pazar"))
print("Ay adı (Türkçe):", simdi.strftime("%B").replace("January", "Ocak").replace("February", "Şubat").replace("March", "Mart").replace("April", "Nisan").replace("May", "Mayıs").replace("June", "Haziran").replace("July", "Temmuz").replace("August", "Ağustos").replace("September", "Eylül").replace("October", "Ekim").replace("November", "Kasım").replace("December", "Aralık"))
print("Yılın hafta sayısı:", simdi.isocalendar()[1])
print("Yılın hafta sayısı (alternatif):", simdi.strftime("%U"))

#os modülü işletim sistemi ile ilgili işlemler için kullanılır.
print("\n=== OS MODÜLÜ ===")
print("Geçerli çalışma dizini:", os.getcwd())
print("Tüm dosyalar:", os.listdir())
print("Dosya var mı (test.txt):", os.path.isfile("test.txt"))
print("Dizin var mı (test):", os.path.isdir("test"))
print("Yol ayırıcı:", os.sep)
print("Sistem bilgileri:", sys.version)
print("Zaman:", time.ctime())
print("JSON örneği:", json.dumps({"ad": "Ahmet", "yas": 30}))

#turtle modülü grafik çizimleri için kullanılır.
import turtle
print("\n=== TURTLE MODÜLÜ ===")
ok = turtle.Turtle()
ok.forward(100)
ok.right(90)        
ok.forward(100)
ok.right(90)
ok.forward(100)
ok.right(90)
ok.forward(100)
ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ok.forward(150)
ok.right(120)
ok.forward(150)
ok.right(120)
ok.forward(150)
ok.right(120)
ekran.exitonclick()  # Tıklamayı bekler
#ok.done() # Çizimi bitir


