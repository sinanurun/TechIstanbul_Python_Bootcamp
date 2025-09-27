# HATA YÖNETİMİ - ÖRNEK 11
# Kullanıcı Girişi Kontrolü 
# Bu program, kullanıcı adı ve şifre kontrolü yapar.
# Hatalı girişlerde anlamlı mesajlar verir.

print("=== GİRİŞ KONTROLÜ ===")

dogru_kullanici_adi = "admin"
dogru_sifre = "1234"

try:
    # Kullanıcıdan bilgileri al
    kullanici_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    
    # Boş kontrolü
    if not kullanici_adi or not sifre:
        raise Exception("Kullanıcı adı ve şifre boş olamaz!")
    
    # Giriş kontrolü
    if kullanici_adi == dogru_kullanici_adi and sifre == dogru_sifre:
        print("Giriş başarılı! Hoş geldiniz.")
    else:
        raise Exception("Kullanıcı adı veya şifre hatalı!")
        
except Exception as e:
    print(f"HATA: {e}")

print("Giriş işlemi tamamlandı.")