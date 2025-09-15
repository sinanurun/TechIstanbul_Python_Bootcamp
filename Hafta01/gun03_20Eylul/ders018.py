#Kullanıcıdan bir cümle al, kaç tane 'a' harfi olduğunu say.

cumle = input("Bir cümle yaz: ")
sayac = 0

for harf in cumle:
    if harf == 'a' or harf == 'A':  # küçük/büyük harf duyarlılığı
        sayac += 1

print(f"Cümlede {sayac} tane 'a' harfi var.")