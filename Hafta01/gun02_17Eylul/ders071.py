#yemek sipariş uygulaması
yemek = input("yemek bilgisi giriniz")
icecek = input("icecek bilgisi giriniz")
if yemek == "pide" and (icecek == "ayran" or icecek == "kola"):
    print(f"{yemek} ve {icecek} siparişi geçerli sipariş")
    print("afiyet olsun")
else:
    print(f"{yemek} ve {icecek} ikili siparişi doğru sipariş değil")