def toplama(a,b):
    return a + b
def fark(a,b):
    return a- b
def islemYap(islem,sayi1,sayi2):
    match islem:
        case "+":
            print(toplama(sayi1, sayi2))
        case "-":
            print(fark(sayi1, sayi2))
        case "x":
            exit()
        case _:
            print("hatali işlem seçimi")
def karsilama():
    islem = input("bir işlem seçiniz: +,-")
    def sayiAl():
        return int(input("sayi giriniz: "))
    sayi1 = sayiAl()
    sayi2 = sayiAl()
    islemYap(islem,sayi1,sayi2)
    return karsilama()

if __name__=="__main__":
    print("programa hosgeldin")
    karsilama()

"""
def toplama(a,b):
    sonuc = a + b
    return sonuc

def cikar(a,b):
    sonuc = a - b
    return sonuc

def carpma(a,b):
    sonuc = a * b
    return sonuc

def bolme(a,b):
    sonuc = a / b
    return sonuc

def yapIslemi(a,b, islem):
    if islem == "toplama":
        return toplama(a,b)
    elif islem == "cikarma":
        return cikar(a,b)
    elif islem == "carpma":
        return carpma(a,b)
    elif islem == "bolme":
        return bolme(a,b)
    else:
        return "Geçersiz işlem"

def karsilama():
    islem = input("yapmak istediğiniz işlemi giriniz (toplama, cikarma, carpma, bolme): ")
    def alSayi():
        return float(input("Sayıyı giriniz: "))
    a = alSayi()    
    b = alSayi()
    sonuc = yapIslemi(a,b,islem)    
    print(f"{a} {islem} {b} = {sonuc}")
    return karsilama()

if __name__ == "__main__":
    print("Hesap makinesi programına hoşgeldiniz")
    karsilama()
    
"""