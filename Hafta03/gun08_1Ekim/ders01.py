# MODÜLLER - ÖRNEK 1
# Math Modülü - Geometrik Hesaplamalar

import math

print("=== GEOMETRİK HESAPLAMALAR ===")

try:
    # Kullanıcıdan yarıçap al
    yaricap = float(input("Dairenin yarıçapını girin: "))
    
    if yaricap <= 0:
        raise ValueError("Yarıçap pozitif olmalıdır!")
    
    # Math modülü ile hesaplamalar
    daire_cevre = 2 * math.pi * yaricap
    daire_alan = math.pi * math.pow(yaricap, 2)
    
    print(f"\nDaire Bilgileri:")
    print(f"Yarıçap: {yaricap}")
    print(f"Çevre: {daire_cevre:.3f}")
    print(f"Alan: {daire_alan:.2f}")
    
    # Karekök ve üs hesapları
    karekok = math.sqrt(yaricap)
    karesi = math.pow(yaricap, 2)
    kupu = math.pow(yaricap, 3)
    
    print(f"\nDiğer Hesaplar:")
    print(f"Karekök: {karekok:.3f}")
    print(f"Karesi: {karesi:.2f}")
    print(f"Küpü: {kupu:.2f}")
    
    # Trigonometrik hesaplamalar
    aci = float(input("\nBir açı değeri girin (derece): "))
    aci_radyan = math.radians(aci)
    
    print(f"\nTrigonometrik Değerler:")
    print(f"Sinüs: {math.sin(aci_radyan):.3f}")
    print(f"Kosinüs: {math.cos(aci_radyan):.3f}")
    print(f"Tanjant: {math.tan(aci_radyan):.3f}")

except ValueError as e:
    print(f"HATA: {e}")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Hesaplamalar tamamlandı.")
