# Örnek 26: Rastgele sayı üretip liste oluşturma (random modülü ön izleme)
import random

def rastgele_liste_olustur(uzunluk):
    """Belirtilen uzunlukta rastgele sayılardan oluşan bir liste oluşturur."""
    try:
        if uzunluk < 0:
            raise ValueError("Uzunluk negatif olamaz.")
        liste = [random.randint(1, 100) for _ in range(uzunluk)]
        return liste
    except ValueError as ve:
        print(ve)
        return []

liste = rastgele_liste_olustur(5)
print(f"Rastgele liste: {liste}")