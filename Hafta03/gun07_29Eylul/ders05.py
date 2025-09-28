# HATA YÖNETİMİ - ÖRNEK 5
# Birden Fazla Hata Türünü Yakalama

"""
Bu program, kullanıcıdan bir liste indeksi ve bölünecek sayı alır.
Aynı except bloğunda hem ValueError hem de ZeroDivisionError hatalarını yakalar.
"""

print("=== ÇOKLU HATA YÖNETİMİ ===")

# Örnek bir liste oluşturuyoruz
sayilar = [10, 20, 30, 40, 50]
print(f"Mevcut liste: {sayilar}")

try:
    # Kullanıcıdan liste indeksi alıyoruz
    indeks = int(input("Listeden hangi indeksteki sayıyı kullanmak istersiniz? (0-4): "))
    
    # Kullanıcıdan bölecek sayıyı alıyoruz
    bolen = int(input("Bu sayıyı kaça bölmek istersiniz? "))
    
    # Seçilen sayıyı listeden alıyoruz
    secilen_sayi = sayilar[indeks]
    
    # Bölme işlemini yapıyoruz
    sonuc = secilen_sayi / bolen
    
    # Sonucu ekrana yazdırıyoruz
    print(f"Sonuç: {secilen_sayi} / {bolen} = {sonuc}")
    
except (ValueError, ZeroDivisionError, IndexError) as hata:
    # Üç farklı hatayı aynı blokta yakalıyoruz
    print(f"HATA oluştu: {type(hata).__name__}")
    # isinstance ile kontrol yapıyoruz istance kullanım amacı : hatanın türünü kontrol etmek
    #Fonksiyon belirtilen nesnenin belirtilen tipte olup olmadığını, aksi takdirde . isinstance()döndürür .TrueFalse
    # True Eğer tip parametresi bir tuple ise, bu fonksiyon nesnenin tuple'daki tiplerden biri olup olmadığını döndürecektir .
    if isinstance(hata, ValueError):
        print("Lütfen geçerli bir tam sayı girin!")
    elif isinstance(hata, ZeroDivisionError):
        print("Bir sayıyı sıfıra bölemezsiniz!")
    elif isinstance(hata, IndexError):
        print("Geçersiz liste indeksi! Lütfen 0-4 arası bir sayı girin.")

print("Program devam ediyor...")