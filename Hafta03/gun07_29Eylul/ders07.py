# HATA YÖNETİMİ - ÖRNEK 7
# try-except-else Kullanımı

print("=== KARESİNİ HESAPLA ===")

try:
    # Kullanıcıdan sayı al
    sayi = int(input("Bir sayı girin: "))
    
except ValueError:
    print("HATA: Lütfen geçerli bir tam sayı girin!")
    
else:
    # Hata olmazsa bu blok çalışır
    karesi = sayi * sayi
    print(f"{sayi} sayısının karesi: {karesi}")
    
print("İşlem tamamlandı.")