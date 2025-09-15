"""
Kullanıcı "python123" şifresini girene kadar sor, 
ama en fazla 3 deneme hakkı olsun."""
hak = 3
dogru_sifre = "python123"

while hak > 0:
    sifre = input("Şifre girin: ")
    if sifre == dogru_sifre:
        print("Giriş başarılı!")
        break
    else:
        hak -= 1
        print(f"Yanlış şifre! Kalan hak: {hak}")

if hak == 0:
    print("Hesabınız bloke edildi.")