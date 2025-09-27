# Örnek 25: Basit bir hesap makinesi (Fonksiyonlar, Koşullar, Hata Yönetimi)
def hesap_makinesi():
    try:
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        islem = input("İşlem seçin (+, -, *, /): ")

        if islem == '+':
            sonuc = sayi1 + sayi2
        elif islem == '-':
            sonuc = sayi1 - sayi2
        elif islem == '*':
            sonuc = sayi1 * sayi2
        elif islem == '/':
            if sayi2 == 0:
                raise ZeroDivisionError("Sıfıra bölme hatası!")
            sonuc = sayi1 / sayi2
        else:
            raise ValueError("Geçersiz işlem operatörü!")

        print(f"Sonuç: {sonuc}")

    except ValueError as ve:
        print(f"Geçersiz giriş: {ve}")
    except ZeroDivisionError as ze:
        print(ze)
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

# hesap_makinesi()  # Çalıştırmak için yorum satırını kaldırın.