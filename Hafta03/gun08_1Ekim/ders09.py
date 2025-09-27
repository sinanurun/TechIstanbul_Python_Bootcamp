# MODÜLLER - ÖRNEK 9
# Kendi Modülümüzü Yazma - Hesap Makinesi Modülü

# Bu dosyayı "hesap_makinesi.py" olarak kaydedip aynı dizinde çalıştırabilirsiniz

print("=== KENDİ MODÜLÜMÜZÜ YAZALIM ===")

# Basit bir hesap makinesi modülü oluşturalım
class HesapMakinesi:
    """Basit bir hesap makinesi sınıfı"""
    
    def topla(self, a, b):
        """İki sayıyı toplar"""
        return a + b
    
    def cikar(self, a, b):
        """İki sayıyı çıkarır"""
        return a - b
    
    def carp(self, a, b):
        """İki sayıyı çarpar"""
        return a * b
    
    def bol(self, a, b):
        """İki sayıyı böler"""
        if b == 0:
            raise ValueError("Sıfıra bölme hatası!")
        return a / b
    
    def us_al(self, a, b):
        """a sayısının b. kuvvetini alır"""
        return a ** b
    
    def karekök(self, a):
        """Bir sayının karekökünü alır"""
        if a < 0:
            raise ValueError("Negatif sayıların karekökü alınamaz!")
        return a ** 0.5

# Modülü test edelim
try:
    # Hesap makinesi nesnesi oluştur
    hesap = HesapMakinesi()
    
    print("Hesap Makinesi Modülü Testi")
    print("=" * 30)
    
    # Test işlemleri
    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))
    
    print(f"\nToplama: {hesap.topla(sayi1, sayi2)}")
    print(f"Çıkarma: {hesap.cikar(sayi1, sayi2)}")
    print(f"Çarpma: {hesap.carp(sayi1, sayi2)}")
    
    try:
        print(f"Bölme: {hesap.bol(sayi1, sayi2)}")
    except ValueError as e:
        print(f"Bölme: {e}")
    
    print(f"Üs Alma: {hesap.us_al(sayi1, sayi2)}")
    
    try:
        print(f"Karekök ({sayi1}): {hesap.karekök(sayi1):.2f}")
    except ValueError as e:
        print(f"Karekök: {e}")
    
    # Ekstra: Liste ile işlemler
    print("\nListe İşlemleri:")
    sayilar = [sayi1, sayi2, 10, 20, 30]
    print(f"Sayılar: {sayilar}")
    print(f"Toplam: {sum(sayilar)}")
    print(f"Ortalama: {sum(sayilar)/len(sayilar):.2f}")

except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Modül testi tamamlandı.")