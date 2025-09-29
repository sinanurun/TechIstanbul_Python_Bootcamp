#Kullanıcı uzunluk seçer, sistem karışık bir şifre üretir.

import random
import string

def sifre_uret(uzunluk):
    karakterler = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))

uzunluk = int(input("Şifre uzunluğu: "))
print("🔐 Şifreniz:", sifre_uret(uzunluk))