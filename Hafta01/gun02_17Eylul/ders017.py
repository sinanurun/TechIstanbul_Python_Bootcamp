import random

tutulan_sayi = random.randint(1, 10)
tahmin = int(input("1-10 arasında bir sayı tahmin et: "))

if tahmin == tutulan_sayi:
    print("🎉 Tebrikler! Bildin!")
else:
    print(f"Yanlış! Tutulan sayı: {tutulan_sayi}")