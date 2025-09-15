#Kullanıcıdan not al, listeye ekle, 
# her adımda listeyi göster.

notlar = []

print("=== NOT DEFTERİ ===")
print("Çıkmak için 'çık' yazın")

while True:
    not_metni = input("Yeni not: ")
    
    if not_metni == "çık":
        print("Not defteri kapatılıyor.")
        break
    
    notlar.append(not_metni)
    print("Not eklendi. Mevcut notlar:")
    
    for notum in notlar:
        print(" - " + notum)