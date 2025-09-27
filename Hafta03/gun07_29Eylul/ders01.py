# HATA YÖNETİMİ - ÖRNEK 1
# Temel try-except Kullanımı (Sıfıra Bölünme Hatası)

"""
Bu program, kullanıcıdan iki sayı alıp bölme işlemi yapar.
Eğer kullanıcı sıfıra bölme işlemi yapmaya çalışırsa,
program hata verip sonlanmak yerine, kullanıcıya anlamlı bir mesaj gösterir.
"""

print("=== BÖLME İŞLEMİ HESAPLAMA ===")

try:
    # Kullanıcıdan iki sayı alıyoruz
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    # Bölme işlemini yapıyoruz
    sonuc = sayi1 / sayi2
    
    # Sonucu ekrana yazdırıyoruz
    print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
    
except ZeroDivisionError:
    # Eğer sayi2 sıfır ise bu blok çalışır
    print("HATA: Bir sayıyı sıfıra bölemezsiniz!")
    
except ValueError:
    # Eğer kullanıcı sayı yerine metin girerse bu blok çalışır
    print("HATA: Lütfen geçerli bir sayı girin!")

print("Program normal şekilde sonlandı.")