#şanslı yedili

import random

semboller = [1,2,3,4,5,6,7]

while True:
    input("Oynamak için ENTER'a basın...")
    sonuc = [str(random.choice(semboller)) for _ in range(3)]
    print(" | ".join(sonuc))
    
    if sonuc[0] == sonuc[1] == sonuc[2]:
        print("🎉 JACKPOT!")
    else:
        print("Tekrar dene!")