#yemek sipariş uygulaması
yemek = input("yemek bilgisi giriniz")
if yemek == "pide":
    print(f"{yemek} siparişi geçerli sipariş")
    icecek = input("icecek bilgisi giriniz")
    if icecek == "ayran" or icecek == "kola":
        print("geçerli içeecek")
    else:
        print("geçersiz içecek")
        print("içecek iade olacak")
    print("afiyet olsun")
else:
    print("yemek siparişi doğru sipariş değil")