def daireAlan(r=1,pi=3.14):
    alan = pi*(r**2)
    return alan

dalan = daireAlan(4,3.45)
print(dalan)


# Varsayılan parametreli fonksiyon
# Mesaj parametresi opsiyonel, varsayılan "İyi günler!" olacak
# Kullanıcı mesaj verirse o kullanılacak, vermezse varsayılan kullanılacak
def selamla(isim, mesaj="İyi günler!"):
    print(f"Merhaba {isim}! {mesaj}")

# Kullanım
selamla("Ali")  # Varsayılan mesaj kullanılır
selamla("Ayşe", "Nasılsın?")  # Özel mesaj