# Kullanıcının ismini, yaşını, hobilerini al, hem .txt, hem .json olarak kaydet.

import json

print("=== KİŞİSEL BİLGİ KAYIT ===")
isim = input("İsim: ")
yas = int(input("Yaş: "))
hobiler = input("Hobiler (virgülle ayır): ").split(",")

# Sözlük oluştur
kisi = {
    "isim": isim,
    "yas": yas,
    "hobiler": [hobi.strip() for hobi in hobiler]
}

# TXT olarak kaydet
with open("bilgi.txt", "w") as f:
    f.write(f"İsim: {isim}\n")
    f.write(f"Yaş: {yas}\n")
    f.write(f"Hobiler: {', '.join(hobiler)}\n")

# JSON olarak kaydet
with open("bilgi.json", "w") as f:
    json.dump(kisi, f, indent=4)

print("Bilgiler kaydedildi: bilgi.txt ve bilgi.json")