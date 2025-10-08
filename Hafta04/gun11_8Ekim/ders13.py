# Örnek 6: Özel Metotlar - Öğrenci Listesi
class OgrenciListesi:
    """Öğrenci listesi sınıfı - Özel metot örneği"""
    
    def __init__(self):
        self._ogrenciler = []
        self._index = 0
    
    def ogrenci_ekle(self, ogrenci):
        """Listeye öğrenci ekler"""
        self._ogrenciler.append(ogrenci)
    
    def __getitem__(self, index):
        """[] operatörü için: liste[index]"""
        return self._ogrenciler[index]
    
    def __setitem__(self, index, value):
        """[] atama için: liste[index] = değer"""
        self._ogrenciler[index] = value
    
    def __delitem__(self, index):
        """del operatörü için: del liste[index]"""
        del self._ogrenciler[index]
    
    def __len__(self):
        """len() fonksiyonu için"""
        return len(self._ogrenciler)
    
    def __contains__(self, ogrenci):
        """in operatörü için: ogrenci in liste"""
        return ogrenci in self._ogrenciler
    
    def __iter__(self):
        """for döngüsü için"""
        self._index = 0
        return self
    
    def __next__(self):
        """for döngüsü için sonraki öğe"""
        if self._index < len(self._ogrenciler):
            result = self._ogrenciler[self._index]
            self._index += 1
            return result
        raise StopIteration
    
    def __str__(self):
        """String gösterimi"""
        return f"OgrenciListesi({len(self)} öğrenci)"
    
    def __repr__(self):
        """Geliştirici string gösterimi"""
        return f"OgrenciListesi({self._ogrenciler})"

class Ogrenci:
    """Basit öğrenci sınıfı"""
    
    def __init__(self, ad, numara):
        self.ad = ad
        self.numara = numara
    
    def __str__(self):
        return f"{self.ad} ({self.numara})"
    
    def __repr__(self):
        return f"Ogrenci('{self.ad}', '{self.numara}')"

# Özel metot kullanımı
print("\n=== ÖZEL METOTLAR: ÖĞRENCİ LİSTESİ ===")

# Öğrenci listesi oluşturma
liste = OgrenciListesi()

# Öğrenciler ekleme
liste.ogrenci_ekle(Ogrenci("Ali", "1001"))
liste.ogrenci_ekle(Ogrenci("Ayşe", "1002"))
liste.ogrenci_ekle(Ogrenci("Mehmet", "1003"))

# __getitem__ kullanımı
print(f"İlk öğrenci: {liste[0]}")
print(f"İkinci öğrenci: {liste[1]}")

# __setitem__ kullanımı
liste[2] = Ogrenci("Zeynep", "1004")
print(f"Güncellenen öğrenci: {liste[2]}")

# __len__ kullanımı
print(f"Toplam öğrenci sayısı: {len(liste)}")

# __contains__ kullanımı
test_ogrenci = Ogrenci("Ali", "1001")
print(f"Ali listede mi? {test_ogrenci in liste}")

# __iter__ ve __next__ kullanımı (for döngüsü)
print(f"\n--- Tüm Öğrenciler (for döngüsü) ---")
for ogrenci in liste:
    print(f"  - {ogrenci}")

# __delitem__ kullanımı
print(f"\n--- Öğrenci Silme ---")
print(f"Silinmeden önce: {len(liste)} öğrenci")
del liste[0]
print(f"Silindikten sonra: {len(liste)} öğrenci")

# Güncel liste
print(f"\n--- Güncel Liste ---")
for i, ogrenci in enumerate(liste, 1):
    print(f"{i}. {ogrenci}")