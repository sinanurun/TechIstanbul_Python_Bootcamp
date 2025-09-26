## Şifre güvenlik kontrolü
# Kullanıcıdan alınan şifrenin güvenli olup olmadığını kontrol eden fonksiyon
# Şifre en az 8 karakter olmalı, sadece sayılardan veya sadece harflerden oluşmamalı
# Fonksiyon, şifrenin güvenli olup olmadığını belirten bir mesaj döndürecek
# return ile değer döndürüyor
def sifre_kontrol(sifre):
    if len(sifre) < 8:
        return "Şifre çok kısa (en az 8 karakter)"
    elif sifre.isnumeric():
        return "Şifre sadece sayılardan oluşamaz"
    elif sifre.isalpha():
        return "Şifre sadece harflerden oluşamaz"
    else:
        return "Şifre güvenli!"

# Kullanım
sifre = "Python123"
print(sifre_kontrol(sifre))