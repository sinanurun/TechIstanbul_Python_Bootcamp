#sayı tahmin oyunu 

tutulan = 7

tahminler = []

while True:
    tahmin = int(input("Tahminin nedir? "))
    if tahmin == tutulan:
        print("🎉 Tebrikler! Bildin!")
        break
    else:
        print("Yanlış, tekrar dene.")
        tahminler.append(tahmin)
        print("Şimdiye kadar yaptığın tahminler:", tahminler)