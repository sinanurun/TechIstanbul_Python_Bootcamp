# Örnek 23: Liste işlemleri ve hata yönetimi
def liste_ortalama(liste):
    """Listedeki sayıların ortalamasını hesaplar."""
    try:
        if not liste:  # Liste boş mu?
            raise ValueError("Liste boş, ortalama hesaplanamaz.")
        toplam = sum(liste)
        ortalama = toplam / len(liste)
        return ortalama
    except TypeError:
        return "Liste yalnızca sayılardan oluşmalıdır."
    except ZeroDivisionError:  # Bu aslında boş liste kontrolü ile önlendi, yine de güvenlik için.
        return "Liste boş olamaz."

# Test
print(liste_ortalama([1, 2, 3, 4, 5]))
print(liste_ortalama([]))
print(liste_ortalama([1, 2, 'a']))