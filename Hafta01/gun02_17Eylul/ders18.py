yas = int(input("Yaşınız: "))
egitim = input("Eğitim durumunuz (lise, üniversite, diğer): ")

if yas >= 18:
    if egitim == "lise" or egitim == "üniversite":
        print("Ehliyet alabilirsiniz.")
    else:
        print("Eğitim durumunuz yetersiz.")
else:
    print("Yaşınız ehliyet almak için yeterli değil.")