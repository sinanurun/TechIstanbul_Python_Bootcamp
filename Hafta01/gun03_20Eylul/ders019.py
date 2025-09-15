#KKullanıcıdan bir metin al, onu tersten yazdır.

metin = input("Bir metin gir: ")
ters = ""

for harf in metin:
    ters = harf + ters  # her harfi başa ekle

print("Tersi:", ters)