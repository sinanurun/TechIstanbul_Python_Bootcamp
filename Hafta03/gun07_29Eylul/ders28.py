def en_buyuk_cift(liste):
    try:
        # Liste içindeki çift sayıları filtrele
        cift_sayilar = [x for x in liste if x % 2 == 0]
        if not cift_sayilar:
            raise ValueError("Listede çift sayı bulunamadı.")
        return max(cift_sayilar)
    except (ValueError, TypeError) as e:
        return f"Hata: {e}"

print(en_buyuk_cift([1, 3, 5, 7, 9]))  # Hata verecek
print(en_buyuk_cift([1, 4, 3, 8, 5]))  # 8 dönecek
print(en_buyuk_cift([1, 2, 'üç', 4]))  # Hata verecek
print(en_buyuk_cift([]))               # Hata verecek   
print(en_buyuk_cift([2, 4, 6, 8]))     # 8 dönecek