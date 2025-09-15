# if True:
#     pass
"""
for dd in range(25):
    ad = input("Enter name")
    if ad == "yemre":
        print("yemre bulundu")
        break
"""

for dd in range(25):
    ad = input("Enter name")
    if ad == "yemre":
        print("yemre kayıt edilemez")
        continue
    soyad = input("Enter surname")
    print(f"{ad} {soyad} sisteme kaydedildi")

