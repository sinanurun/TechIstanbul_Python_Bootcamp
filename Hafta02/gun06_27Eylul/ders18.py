# Faktoriyel Hesaplama
# Bir sayının faktoriyelini hesaplayan fonksiyon
# Faktoriyel: n! = n * (n-1) * (n-2) * ... * 1 (örn: 5! = 5*4*3*2*1 = 120)
# Fonksiyon, faktoriyel değerini return ile döndürecek
def faktoriyel(sayi):
    if sayi < 0:
        return "Negatif sayıların faktoriyeli hesaplanamaz"
    elif sayi == 0 or sayi == 1:
        return 1
    else:
        sonuc = 1
        for i in range(2, sayi + 1):
            sonuc *= i
        return sonuc

# Kullanım
for i in range(6):
    print(f"{i}! = {faktoriyel(i)}")