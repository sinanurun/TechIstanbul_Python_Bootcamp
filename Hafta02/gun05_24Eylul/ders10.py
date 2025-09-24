hafta_ici = {"pazartesi":1, "sali":2}
hafta_sonu = {"cumatersi":6, "pazar":7}

hafta_ici.update(hafta_sonu)
print("birlşeik günler", hafta_ici)


gun = "perşembe"

if gun in hafta_ici:
    print("gün kayıtlı")
else:
    print("kayıtlı gün değil")

print(len(hafta_ici))