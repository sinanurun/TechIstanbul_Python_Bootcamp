ad1 = "cansel"
ad2 = "büşra"
ad3 = "barış"

print(ad1+ad2+ad3)
print(f"{ad1} {ad2} {ad3}")

metin = "Merhaba sayın {} Kursumuza hoşgeldin"
print(metin.format(ad1))
print(metin.format(ad2))
print(metin.format(ad3))
print("hoşgeldin {}".format(ad1))

metin2 = "yarışmamızın başarı listesi {}, {}, {}"
print(metin2.format(ad1, ad2, ad3))
print(metin2.format(ad2, ad3, ad1))

metin3 = "{k1},Merhaba {k1}, {k2}, {k3}".format(k1=ad1, k2=ad2, k3=ad3)
print(metin3)
print(metin3.capitalize())
print(metin3.count("an"))
print(metin3.count("an"))