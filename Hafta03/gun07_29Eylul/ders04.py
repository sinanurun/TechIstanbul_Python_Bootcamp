# HATA YÖNETİMİ - ÖRNEK 4
# Birden Fazla Hata Yakalama

print("=== HESAP MAKİNESİ ===")

try:
    # Kullanıcıdan verileri al
    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))
    islem = input("İşlem (+, -, *, /): ")
    
    # İşlemi yap
    if islem == '+':
        sonuc = sayi1 + sayi2
    elif islem == '-':
        sonuc = sayi1 - sayi2
    elif islem == '*':
        sonuc = sayi1 * sayi2
    elif islem == '/':
        sonuc = sayi1 / sayi2
    else:
        print("HATA: Geçersiz işlem! Sadece +, -, *, / kullanın.")
        sonuc = None
    
    if sonuc is not None:
        print(f"Sonuç: {sayi1} {islem} {sayi2} = {sonuc}")
        
except ValueError:
    print("HATA: Lütfen geçerli sayılar girin!")
except ZeroDivisionError:
    print("HATA: Bir sayıyı sıfıra bölemezsiniz!")

print("Program bitti.")