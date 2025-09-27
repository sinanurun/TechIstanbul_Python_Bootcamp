# Örnek 24: Kullanıcıdan sürekli geçerli sayı girmesini isteyen döngü
while True:
    try:
        sayi = int(input("Lütfen bir sayı girin (Çıkmak için 'q'): "))
        print(f"Girdiğiniz sayının karesi: {sayi ** 2}")
        break  # Geçerli sayı girilirse döngüden çık
    except ValueError:
        print("Geçersiz giriş! Lütfen bir tam sayı girin.")
        # 'q' girilirse çıkış yapalım (basit bir kontrol)
        if input("Çıkmak istiyor musunuz? (q): ").lower() == 'q':
            print("Program sonlandırıldı.")
            break