# Örnek 27: Kullanıcı doğrulama senaryosu (Karar yapıları ve hata yönetimi)
kullanici_adi = "admin"
sifre = "1234"

def giris_yap():
    try:
        girilen_kullanici = input("Kullanıcı Adı: ")
        girilen_sifre = input("Şifre: ")

        if girilen_kullanici != kullanici_adi or girilen_sifre != sifre:
            raise Exception("Kullanıcı adı veya şifre hatalı!")

        print("Giriş başarılı! Hoş geldiniz.")

    except Exception as hata:
        print(hata)

# giris_yap()